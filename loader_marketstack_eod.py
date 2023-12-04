# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:39:50 2022

@author: josep
"""
from rdsskywalkercore import RDSCalendar
import sys

from loader_marketstack import Loader_MarketStack_Generic
from ticker_lists import sp500_full
from ticker_lists import xrt_components
from ticker_lists import xph_components
from ticker_lists import xme_components
from ticker_lists import xhb_components
from ticker_lists import xhs_components
from ticker_lists import xhe_components
from ticker_lists import kce_components
from ticker_lists import xbi_components
from ticker_lists import xsd_components
from ticker_lists import xsw_components
from ticker_lists import xtn_components
from ticker_lists import xlp_components
from ticker_lists import xly_components
from ticker_lists import xlc_components
from ticker_lists import xlf_components
from ticker_lists import xlv_components
from ticker_lists import xli_components
from ticker_lists import xlb_components
from ticker_lists import xlre_components
from ticker_lists import xlk_components
from ticker_lists import xlu_components
from ticker_lists import nasdaq100_components


class Loader_MarketStack_EOD(Loader_MarketStack_Generic):
     def flatten_record(self, record):
         
         #Only accept short and simple symbols (no OTC, preferred, warrants or other variants)
         mylist = [
            record['symbol'],
            record['date'][:10],
            record['exchange'],
            record['open'],
            record['high'],
            record['low'],
            record['close'],
            record['volume'],
            record['adj_open'],
            record['adj_high'],
            record['adj_low'],
            record['adj_close'],
            record['adj_volume'],
            record['split_factor'],
            record['dividend']
             ]
         
         return(mylist)
     
     def urlExtenion(self):
         return('eod')
     
     def outFileExtension(self):
         return(self.urlExtenion())
     
     def importTableName(self):
         return('marketstack_import_eod')


def updateMarketStackEOD(dateFrom = None, dateTo = None):
    symbolList1 = list(sp500_full)
    symbolList1.extend(x for x in nasdaq100_components if x not in symbolList1)
    symbolList1.extend(x for x in xrt_components if x not in symbolList1)
    symbolList1.extend(x for x in xph_components if x not in symbolList1)
    symbolList1.extend(x for x in xme_components if x not in symbolList1)
    symbolList1.extend(x for x in xhb_components if x not in symbolList1)
    symbolList1.extend(x for x in xhs_components if x not in symbolList1)
    symbolList1.extend(x for x in xhe_components if x not in symbolList1)
    symbolList1.extend(x for x in kce_components if x not in symbolList1)
    symbolList1.extend(x for x in xbi_components if x not in symbolList1)
    symbolList1.extend(x for x in xsd_components if x not in symbolList1)
    symbolList1.extend(x for x in xsw_components if x not in symbolList1)
    symbolList1.extend(x for x in xtn_components if x not in symbolList1)
    symbolList1.extend(x for x in xly_components if x not in symbolList1)
    symbolList1.extend(x for x in xlc_components if x not in symbolList1)
    symbolList1.extend(x for x in xlf_components if x not in symbolList1)
    symbolList1.extend(x for x in xlv_components if x not in symbolList1)
    symbolList1.extend(x for x in xli_components if x not in symbolList1)
    symbolList1.extend(x for x in xlb_components if x not in symbolList1)
    symbolList1.extend(x for x in xlre_components if x not in symbolList1)
    symbolList1.extend(x for x in xlk_components if x not in symbolList1)
    symbolList1.extend(x for x in xlu_components if x not in symbolList1)
    symbolList1.extend(x for x in xlp_components if x not in symbolList1)

    
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
            
    pickupFlag = False
    for ticker in symbolList1:
        # if ticker == 'GOOGL':
        #     pickupFlag = True
        pickupFlag = True
        if pickupFlag:
            print(ticker,end="", flush=True)
            eodParams =     {'symbols':ticker,
                              'date_from':dateFrom,
                              'date_to':dateTo
                }
            loader = Loader_MarketStack_EOD(eodParams)
            
            loader.fetchAllPages()
            loader.copyAllNewFilesToDB()

if __name__ == '__main__':
    # print("Starting...")
    # updateMarketStackEOD()
    
    for ticker in nasdaq100_components:

        eodParams =     {'symbols':ticker,
                          'date_from':'2001-01-01',
                          'date_to':'2023-04-01'
            }
        loader = Loader_MarketStack_EOD(eodParams)
        
        loader.fetchAllPages()
        loader.copyAllNewFilesToDB()
    
    
    
    