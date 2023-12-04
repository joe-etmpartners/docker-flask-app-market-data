# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:39:50 2022

@author: josep
"""
from loader_marketstack import Loader_MarketStack_Generic
from ticker_lists import symbol_lists



class Loader_MarketStack_Intraday_5min(Loader_MarketStack_Generic):
    
    
     def flatten_record(self, record):
                  
         mylist = [
            record['symbol'],
            record['date'][:10],
            record['date'][11:],
            record['exchange'],
            record['open'],
            record['high'],
            record['low'],
            record['close'],
            record['last'],
            record['volume']
             ]
         
         return(mylist)
     
     def urlExtenion(self):
         return('intraday')
     
     def outFileExtension(self):
         return(self.urlExtenion()+'_5min')
     
     def importTableName(self):
         return('marketstack_import_intraday_5min')


if __name__ == '__main__':
    
    symbolList1 = ['SPY']
    
    dateFrom = '2022-11-01'
    dateTo = '2022-12-29'
 
    
    
    for dkey in symbol_lists:
        pickupFlag = False
        for ticker in symbol_lists[dkey]:
            # if ticker == 'INFA':
            #     pickupFlag = True
            pickupFlag = True
            if pickupFlag:
                print("\nAttempting to fetch intraday data for "+ticker)
                intradayParams =     {'symbols':ticker,
                                  'date_from':dateFrom,
                                  'date_to':dateTo,
                                  'interval':'5min'
                    }
                loader = Loader_MarketStack_Intraday_5min(intradayParams)
                
                rtn = loader.fetchAllPages()
                loader.copyAllNewFilesToDB()
                
                # try:
                #     rtn = loader.fetchAllPages()
                #     loader.copyAllNewFilesToDB()
                # except:
                #     print("ERROR trying to fetch intraday data for "+ticker)
    
        
        
        
    
    