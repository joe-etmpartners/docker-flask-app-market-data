# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:39:50 2022

@author: josep
"""
from rds_skywalker import RDSCalendar
import sys

from ETM_AWS_Logger import ETM_AWS_Logger


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
            str(record['symbol']),
            str(record['date'][:10]),
            str(record['exchange']),
            str(record['open']),
            str(record['high']),
            str(record['low']),
            str(record['close']),
            str(record['volume']),
            str(record['adj_open']),
            str(record['adj_high']),
            str(record['adj_low']),
            str(record['adj_close']),
            str(record['adj_volume']),
            str(record['split_factor']),
            str(record['dividend'])
             ]
         
         mylist = [x.replace('None', '') for x in mylist]
         
         return mylist
     
     def urlExtenion(self):
         return('eod')
     
     def outFileExtension(self):
         return(self.urlExtenion())
     
     def importTableName(self):
         return('marketstack_import_eod')


    
    
    
    
def loader_marketstack_eod_test():
    # print("Starting...")
    # updateMarketStackEOD()

    rdsCalendar = RDSCalendar()
    rtn = rdsCalendar.getLastDate()
    print (rtn)
    print (type(rtn))
    dateFrom = str(rtn)
    print (dateFrom)
    print (type(dateFrom))
    
    from datetime import date
    today = date.today()
    dateTo = str(today)
    print (dateTo)
    print (type(dateTo))
        

    eodParams =     {'symbols':'AMZN',
                        'date_from':dateFrom,
                        'date_to':dateTo
        }
    loader = Loader_MarketStack_EOD(additionalParams=eodParams)
    
    loader.fetchAllPages()
    
  
    
    
    
    