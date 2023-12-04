# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 15:39:50 2022

@author: josep
"""
from loader_marketstack import Loader_MarketStack_Generic


class Loader_MarketStack_Exchanges(Loader_MarketStack_Generic):
    
    
    def flatten_record(self, record):
        
         try:
             f1 = record['name'].encode(encoding = 'ascii')[:1023]
         except:
             f1 = ''
            
         mylist = [
                record['mic'],
                f1
                 ]

         return(mylist)
     
    def urlExtenion(self):
        return('exchanges')

    def importTableName(self):
        return('marketstack_import_exchanges')

    def outFileExtension(self):
        return(self.urlExtenion())


if __name__ == '__main__':
    
    
    

    loader = Loader_MarketStack_Exchanges()
    
    rtn = loader.fetchAllPages()
    loader.copyAllNewFilesToDB()

    
    
    
    
    