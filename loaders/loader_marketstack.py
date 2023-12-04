# -*- coding: utf-8 -*-

import requests
import json
import datetime
import csv
from s3skywalker import S3Skywalker 
from rdsskywalkercore import RDSSkywalker
from rdsskywalkercore import RDSImportLog

params = {
  'access_key': '6a880b8488561bdb2b89c8f0482ff77b'
}


class Loader_MarketStack_Generic:
    
    def urlExtenion(self):
        return('exchanges')
    
    def importTableName(self):
        return('marketstack_import_exchanges')
    
    def outFileExtension(self):
        return(self.urlExtenion())
    
    def __init__(self, additionalParams={}):
        self.url = 'http://api.marketstack.com/v1/'+self.urlExtenion()
        self.params = {'access_key': '6a880b8488561bdb2b89c8f0482ff77b'}
        self.params.update(additionalParams)
        self.params.update({'limit':1000})
        self.params.update({'offset':0})
        
        #print (self.url)
        #print (self.params
        
    def flatten_record(self, record):
        return(['base class output not defined',1,5,'strong with , comma'])
        
    def save_csv(self):
        
        now = datetime.datetime.today().strftime('%Y%m%d%H%M%S%f')
        
        basename = self.outFileExtension()
        fname = 'C:\\projects\\data\\'+basename+'\\'+basename+now+'.csv'
        keyname = basename+'/'+basename+now+'.csv'
        #print (fname)
        validRecordCount = 0
        with open(fname, "w", newline='') as outfile:
            spamwriter = csv.writer(outfile, dialect='excel')
            for record in self.response['data']:
                flat_record = self.flatten_record(record)
                if flat_record is not None:
                    spamwriter.writerow(flat_record)
                    validRecordCount = validRecordCount + 1
        
        if validRecordCount > 0:
            s3 = S3Skywalker()
            s3.upload_file(fname, keyname, basename)

    def save_json_multiple_entries(self):
        # Writing to sample.json
        now = datetime.datetime.today().strftime('%Y%m%d%H%M%S%f')
        
        basename = self.outFileExtension()
        fname = 'C:\\projects\\data\\'+basename+'\\'+basename+now+'.json'
        print (fname)
        with open(fname, "w") as outfile:
            for record in self.response['data']:
                json_string = json.dumps(record, indent=4)
                #print (json_string)
                outfile.write(json_string)
                outfile.write('\n')
        
        
        
    def fetchNextPage(self):
        self.result = requests.get(self.url,self.params)
        self.response = self.result.json()
        
        #print (self.result)
        #print (self.response)
        
        try:
            pageObj = self.response['pagination']
            print (".",end="", flush=True)
        except:
            print ("ERROR locating pagination record")
            print (self.url)
            print (self.params)
            print (self.response)
            return(False)

        #self.save_json_multiple_entries()
        self.save_csv()
        
        if (pageObj['count'] < pageObj['limit']):
            return(False)
        else:
            self.params['offset'] = self.params['offset']+self.params['limit']
            return(True)
        
    def fetchAllPages(self):
        while (self.fetchNextPage()):
            continue
        
    def copyS3FileToDB(self, fileKey, tableName):
        sqlString = "SELECT aws_s3.table_import_from_s3(" + \
                    "'public." + tableName + "', " + \
                    "'', " + \
                    "'(format csv)'," + \
                    "'s3-skywalker', " + \
                    "'" + fileKey + "', " + \
                    "'us-east-2'" + \
                    ");"
        #print (sqlString)
        rdsSkywalker = RDSSkywalker()
        try:
            rdsSkywalker.connectAndRunSQL(sqlString)
        except:
            print("ERROR copying file to DB: "+sqlString)
        
        rdsImportLog = RDSImportLog()
        rdsImportLog.setProcessedToTrue(fileKey)
        
    def copyAllNewFilesToDB(self):
        loader = self.outFileExtension()
        
        importLog = RDSImportLog()         
        fileList = importLog.getListOfUnprocessedFiles(loader)
        
        tableName = self.importTableName()
        
        for fileKey in fileList:
            self.copyS3FileToDB(fileKey, tableName)
            print("*",end="", flush=True)

        
class Loader_MarketStack_Tickers(Loader_MarketStack_Generic):
    
     def flatten_record(self, record):
         
         #Only accept short and simple symbols (no OTC, preferred, warrants or other variants)
         try:
             f1 = record['name'].encode(encoding = 'ascii')[:1023]
         except:
             f1 = ''
         
         f2 = record['symbol']
         if len(f2) > 5:
            return(None)
        
         if ('-' in f2) or ('.' in f2) or (' ' in f2):
            return(None)
        
         try:
             f5 = record['country'].encode(encoding = 'ascii')[:31]
         except:
             f5 = ''

         
         mylist = [
            f1, f2,
            record['has_intraday'],
            record['has_eod'],
            f5,
            record['stock_exchange']['mic']
             ]
         return(mylist)
    
     def urlExtenion(self):
         return('tickers')
     
     def importTableName(self):
         return('marketstack_import_tickers')
     
class Loader_MarketStack_Intraday(Loader_MarketStack_Generic):
     def urlExtenion(self):
         return('intraday')
     
     def outFileExtension(self):
         return(self.urlExtenion()+self.params['interval'])
     

        
if __name__ == '__main__':
    loader = Loader_MarketStack_Tickers({'exchange':'XCBO'})
    rtn = loader.fetchAllPages()
    #print (rtn)
    loader.copyAllNewFilesToDB()

    
    #loader = Loader_MarketStack_Generic()
    #loader.copyS3FileToDB('tickers/tickers20221217161949033460.csv', 'marketstack_import_tickers')

# loader = Loader_MarketStack_Generic()
# rtn = loader.fetchAllPages()
# print (rtn)

#loader = Loader_MarketStack_Tickers({'exchange':'XNYS'})
# loader = Loader_MarketStack_Tickers({'exchange':'XNAS'})

# rtn = loader.fetchAllPages()
# print (rtn)

# symbolList1 = ['SPY']

# symbolList_error_test = ['ZTS']



# sp500_symbol_errors = ['ZTS','TT','WMB','XEL','OTIS','XOM','ZBH','WBD',
#                   'META','WMT','WY','WFC','VZ','WAT','WRB','XYL','ZBRA',
#                   'HWM','VTR','WAB','VTRS','BALL','WST','WDC','WRK',
#                   'BBWI', 'WYNN','WHR','ZION', 'XRAY', 'OGN', 'LUMN']
            

# sp500_full = ['NWL','RL','FOX','DVA','VNO','DISH','NWS',
#               'GNRC','LNC','ALK','MHK', 'FRT','PNR','NWSA',
#               'BEN','NCLH','AIZ','DXC', 'CTLT','RHI','HAS',
#               'AOS','SEE', 'HII','AAL','AAP','FFIV','ROL','UHS','PNW',
#               'IVZ','BIO','FBHS','SBNY','HSIC','NI','KMX',
#               'CPB','GL','CE','TFX','EMN','VFC','CZR','TAP','JNPR',
#               'PHM','STX','BWA','LYV','PARA','REG','BXP','NRG','ALLE',
#               'CDAY','FOXA','QRVO','MKTX','CCL','TPR','CMA',
#               'POOL','TECH','CPT','PKG','NDSN','LW','UDR','CHRW',
#               'CRL','SWK','MGM','L','MAS','SNA','SIVB',
#               'IPG','BRO','MTCH','EVRG','TYL','HST','IP',
#               'RE','RCL','GEN','CBOE','PTC','LKQ','DPZ','PEAK','LNT',
#               'JKHY','EXPE',
#               'APA','COO','JBHT','TXT','LDOS','LVS','INCY','SWKS',
#               'AKAM','FLT','NVR','TRMB','TER','ALGN','HRL','KIM','UAL',
#               'GRMN','ESS','EQT','IRM','AVY','PAYC','ETSY',
#               'SJM','OMC','FMC','SEDG','NTAP','TTWO','J','MPWR',
#               'KEY','BBY','ABMD','FDS','PKI','TRGP','ATO','BR',
#               'SYF','CLX','DRI','STE','CAG','MOS','IEX','DGX','CMS','CINF',
#               'EPAM','TSN','CHD','CNP','NTRS',
#               'TDY','MOH','AES','HOLX','EXPD','INVH','MAA','K','AMCR','VRSN',
#               'LYB','RF','EQR','ACGL','CAH','PPL','CF','IR',
#               'PFG','ANSS','MKC','MRO','CFG','PWR','EXR','HPE',
#               'DOV','AAPL','MSFT','AMZN','GOOGL','BRK.B','GOOG',
#               'UNH','TSLA','JNJ','XOM','JPM','NVDA','PG','V',
#               'CVX','HD','MA','LLY','ABBV','PFE','MRK','BAC','PEP',
#               'META','KO','COST','WMT','TMO','AVGO','CSCO','MCD',
#               'ABT','ACN','WFC','DIS','DHR','BMY','LIN','NEE','VZ',
#               'TXN','COP','CMCSA','ADBE','PM','UNH','TSLA','JNJ',
#               'JPM','NVDA','PG','V','CVX',
#               'HD','MA','LLY','ABBV','PFE','MRK','BAC','PEP',
#               'KO','COST','TMO','AVGO','CSCO','MCD','ABT','ACN',
#               'DIS','DHR','BMY','LIN','NEE',
#               'TXN','COP','CMCSA','ADBE','PM',
#               'AMGN,CRM,HON','RTX','T','UPS','NKE','QCOM','UNP','LOW',
#               'CVS','IBM','GS','NFLX','CAT','ELV','ORCL','SCHW','DE','MS',
#               'INTC','AMD','SPGI','LMT','SBUX','BLK','GILD','INTU',
#               'ADP','PLD','MDT','AMT','BA','CI','TJX','GE','AXP','ISRG','C',
#               'MDLZ','CB','AMAT','PYPL','TMUS','ADI','MMC','EOG',
#               'MO','VRTX','NOW','BKNG','REGN','TGT','NOC','SYK','PGR','DUK',
#               'SLB','SO','MMM','CSX','BDX','PNC','HUM','APD',
#               'FISV','ETN','AON','CL','BSX','ITW','CME','MPC','EQIX',
#               'MU','TFC','LRCX','USB','CCI','NSC','ICE','MRNA','GM','PXD',
#               'DG','SHW','GD','EMR','MCK','F','ORLY','ADM','FCX','VLO','KLAC',
#               'ATVI','PSX','OXY','MET','HCA','SRE','D','AZO','EL','SNPS','GIS','AEP',
#               'CNC','CTVA','AIG','EW','PSA','APH','MCO','JCI','A','KMB','ROP',
#               'CDNS','TRV','MAR','DVN','MSI','SYY','NXPI','DXCM','LHX','CMG',
#               'CHTR','ADSK','FDX','BIIB','AJG','FIS','ENPH','MCHP','ROST',
#               'AFL','STZ','EXC','TEL','IQV','PRU','MSCI','HES',
#               'COF','CTAS','NUE','O','MNST','SPG','PAYX','HLT','PH',
#               'KMI','CARR','DOW','NEM','ALL','PCAR','YUM','ECL',
#               'AMP','DD','CMI','IDXX','HSY','ED','FTNT','EA','HAL','BK',
#               'ANET','RMD','KDP','ILMN','VICI','KR',
#               'WELL','AME','MTD','SBAC',
#               'TDG','ALB','DLR','KEYS','KHC','PPG','CSGP','DLTR','CTSH','ON',
#               'CEG','WEC','MTB','ROK','DFS','WBA','PEG','BKR','OKE','FAST','RSG',
#               'ES','BAX','VRSK','GPN','APTV','CPRT','TROW','IT','STT','GWW','ODFL',
#               'DHI','AWK','HPQ','WTW','ABC','FANG','IFF','GPC','GLW','CDW',
#               'CBRE','HIG','FITB','TSCO','PCG','EBAY','URI','EIX','AVB',
#               'VMC','ULTA','FTV','LUV','ETR',
#               'EFX','ARE','NDAQ','RJF','CTRA','AEE','FRC','MLM','LEN',
#               'HBAN','DAL','DTE','LH','FE']

# xrt_components = ['ANF','GPS','AEO','FIVE','ODP','BURL','BKE','URBN',
#                   'M','ETSY','ROST','CHWY','GES','TJX','ORLY',
#                   'AZO','DDS','BBY','PAG','TSCO','GPI',
#                   'SFM','SAH','EYE','ABG','ULTA','CASY',
#                   'OLLI','DLTR','KSS','CHS','AN','JWN','FL','DKS','EBAY',
#                   'MUSA','SIG','RVLV','HIBB','MNRO','DG','TGT','BOOT',
#                   'COST','KR','GME','LAD','OSTK','HZO','CWH','BJ',
#                   'IMKTA','RCII','GCO','CAL','AAP','PLCE','GO',
#                   'BIG','QRTEA','SBH','PSMT','KMX','SCVL','PETS',
#                   'AMZN','ACI','SFIX','RAD','DBI','CRMT',
#                   'ZUMZ','SPWH','PRTS','TA','LQDT','CVNA',
#                   'ONEW','VSCO','POSH','WBA','WMT','BBWI','WRBY','ASO','LESL',
#                      'DASH','W','XMTR','WOOF','FRG','EVGO','WISH',
#                      'WMK','WINA','ARKO']

# xph_components = ['MRK','LLY','AXSM','BMY','JNJ','SAVA',
#                   'PFE','ITCI','AMLX','JAZZ','RETA','RPRX','PBH',
#                   'CORT','PCRX','ELAN','PRGO','AMPH','SIGA',
#                   'INVA','SUPN','CTLT','RVNC','NKTR','COLL','TBPH','ACRS',
#                   'ESPR','CARA','EOLS','ANIP','AVIR',
#                   'PAHC','RLMD','NGM','CINC','PLRX','HRMY','ZTS',
#                      'VTRS','OGN','ARVN','VTYX','NUVB']

# xme_components = ['BTU','HL','FCX','STLD','RGLD','CMC','NEM',
#                   'CEIX','ARCH','RS','NUE','ATI','AA','ARNC',
#                   'PLL','CENX','CLF','CDE','UEC','EVA','CMP','KALU',
#                   'CRS','TMST','MTRN','RYI','SCHN','SXC','HAYN',
#                     'AMR','X','MP','WOR','FEAM']

# kie_components = ['RNR','ACGL','KNSL','RE','SIGI','GL','AFL','TRV',
#                   'PFG','AIG','HIG','MET','CB','RGA','MKL','CINF',
#                   'BHF','PRU','ORI','AFG','UNM','THG','ALL','AJG','AON',
#                   'MMC','PGR','L','FAF','AGO','FNF','AXS','BRO','PRI',
#                   'AEL','CNO','AIZ','RLI','LNC','TRUP',
#                   'ERIE','GNW','KMPR','GSHD','ESGR','PLMR','RYAN','WTW','WRB','WTM']

# sector_etfs = ['XRT','XPH','XME','KIE']

# #exchange1 = 'XNYS'
# interval = '30min'
# dateFrom = '2009-01-25'
# dateTo = '2022-11-01'

# # for ticker in symbolList_error_test:
# #     intradayParams = {'symbols':ticker,
# #                       'interval':interval,
# #                       'date_from':dateFrom,
# #                       'date_to':dateTo
# #         }
# #     loader = Loader_MarketStack_Intraday(intradayParams)
    
# #     #rtn = loader.fetchAllPages()
# #     rtn = loader.fetchNextPage()
# #     print (rtn)

# # for ticker in symbolList_error_test:
# #     eodParams =     {'symbols':ticker,
# #                       'date_from':dateFrom,
# #                       'date_to':dateTo
# #         }
# #     loader = Loader_MarketStack_EOD(eodParams)
    
# #     rtn = loader.fetchAllPages()
# #     #rtn = loader.fetchNextPage()
# #     print (rtn)


# # api_result = requests.get('http://api.marketstack.com/v1/exchanges/XNYS', params)

# # api_response = api_result.json()


# # print (api_result)

# # print (api_response)

# # for stock_data in api_response['data']:
# #     print(u'Ticker %s has a day high of  %s on %s' % (
# #       stock_data['symbol'],
# #       stock_data['high'],
# #       stock_data['date']
# #    ))
