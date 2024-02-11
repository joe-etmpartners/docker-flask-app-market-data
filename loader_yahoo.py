# -*- coding: utf-8 -*-
"""
Created on Thu Dec 29 13:57:53 2022

@author: josep
"""
import datetime
#import csv
from s3skywalker import S3Skywalker 
from rds_skywalker import RDSSkywalker
from rds_skywalker import RDSImportLog
from rds_skywalker import RDSCalendar

from yahoo_fin.stock_info import get_data
from ticker_lists import yahoo_symbol_lists


class Loader_Yahoo_Generic:
    
    def importTableName(self):
        return('yahoo_import_quotes')
    
    def outFileExtension(self):
        return('yahooQuotes')
    
    def __init__(self):
        pass
        
    def save_csv(self):
        now = datetime.datetime.today().strftime('%Y%m%d%H%M%S%f')
        basename = self.outFileExtension()
        fname = 'C:\\projects\\data\\'+basename+'\\'+basename+now+'.csv'
        keyname = basename+'/'+basename+now+'.csv'

        self.yahoo_data.to_csv(fname, header=False)

        s3 = S3Skywalker()
        s3.upload_file(fname, keyname, basename)
        
    def copyS3FileToDB(self, fileKey, tableName):
        sqlString = "SELECT aws_s3.table_import_from_s3(" + \
                    "'public." + tableName + "', " + \
                    "'', " + \
                    "'(format csv)'," + \
                    "'s3-skywalker', " + \
                    "'" + fileKey + "', " + \
                    "'us-east-2'" + \
                    ");"
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
            
    def getYahooQuotes(self,ticker,start_date,end_date):
        
        print("Getting Yahoo quote data for "+ticker)
        
        self.yahoo_data = get_data(ticker, start_date = start_date, end_date = end_date, index_as_date = True, interval = '1d')
        # Drop rows with missing data
        self.yahoo_data = self.yahoo_data.dropna(subset=['open', 'close'])
        # Get the list of all column names from headers
        #column_headers = list(self.yahoo_data.columns.values)
        #print("The Column Header :", column_headers)

class Loader_Yahoo_EOD(Loader_Yahoo_Generic):
    pass

    
def updateYahooEOD(dateFrom = None, dateTo = None):

    print('Starting Yahoo Loader')
    
    yahooLoader = Loader_Yahoo_Generic()
    
    if dateFrom == None:
        rdsCalendar = RDSCalendar()
        rtn = rdsCalendar.getLastDate()
        print (rtn)
        print (type(rtn))
        dateFrom = str(rtn)
        print (dateFrom)
        print (type(dateFrom))
        
    if dateTo == None:
        from datetime import date
        today = date.today()
        dateTo = str(today)
        print (dateTo)
        print (type(dateTo))
    
    for dkey in yahoo_symbol_lists:
        for ticker in yahoo_symbol_lists[dkey]:
            yahooLoader.getYahooQuotes(ticker,dateFrom,dateTo)
            yahooLoader.save_csv()
            yahooLoader.copyAllNewFilesToDB()

if __name__ == '__main__':
    updateYahooEOD()
   