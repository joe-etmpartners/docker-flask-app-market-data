from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, select
from sqlalchemy.orm import Session

from sqlalchemy.ext.automap import automap_base

from sqlalchemy.exc import IntegrityError

from psycopg2 import OperationalError, errorcodes, errors
from psycopg2.errors import UniqueViolation

from pprint import pprint

import rds_skywalker
from rds_skywalker import RDSSkywalker

import ticker_lists


class DBTables(object):

    def __init__(self):
        rdsobj = RDSSkywalker()
        self.engine = create_engine(rdsobj.connectionString)

        # produce our own MetaData object
        self.metadata = MetaData()

        # we can reflect it ourselves from a database, using options
        # such as 'only' to limit what tables we look at...
        self.metadata.reflect(self.engine, only=['symbols','calendar','symbol_groups','symbol_group_membership'])
        #self.metadata.reflect(self.engine)


        # we can then produce a set of mappings from this MetaData.
        self.Base = automap_base(metadata=self.metadata)

        # # calling prepare() just sets up mapped classes and relationships.
        self.Base.prepare()

        print (dir(self.Base.classes))

        self.symbolTable = self.Base.classes.symbols
        self.calendarTable = self.Base.classes.calendar
        self.symbolGroupsTable = self.Base.classes.symbol_groups


        # return self.Base.classes.symbols



    def get_all_symbols(self):
        rtndata = []
        symbolTable = self.symbolTable
        with Session(self.engine) as session:
            u1 = session.query(symbolTable).all()   
            for u in u1:
                rtndata.append([u.symbol_id,u.symbol])
        rtn = {'columns':['symbol_id','symbol'],'data':rtndata}
        return rtn
    
    def insert_symbol_group(self, group_name):
        symbolGroupsTable = self.symbolGroupsTable
        with Session(self.engine) as session:
            session.add(symbolGroupsTable(group_name=group_name))
            session.commit()
        return True
    
    def add_symbol_to_group(self, group_name, symbol_name):
        symbolGroupsTable = self.symbolGroupsTable
        symbolTable = self.symbolTable
        symbolGroupMembershipTable = self.Base.classes.symbol_group_membership
        with Session(self.engine) as session:

            try:
                group_id = session.query(symbolGroupsTable).where(symbolGroupsTable.group_name == group_name).first().group_id
            except AttributeError:
                print("group name "+group_name+" not found")
                return False
            print ('group_id',group_id)

            try:
                symbol_id = session.query(symbolTable).where(symbolTable.symbol == symbol_name).first().symbol_id
            except:
                print("symbol name "+symbol_name+" not found")
                return False
            print ('symbol_id',symbol_id)

            try:
                session.add(symbolGroupMembershipTable(group_id=group_id,symbol_id=symbol_id))
                session.commit()
            except IntegrityError:
                print ("Record already exists")
                session.rollback()
                return False
        return True
    
    def get_symbol_group(self, group_name):
        symbolGroupsTable = self.symbolGroupsTable
        symbolGroupMembershipTable = self.Base.classes.symbol_group_membership
        symbolTable = self.symbolTable
        with Session(self.engine) as session:
            group_id = session.query(symbolGroupsTable).where(symbolGroupsTable.group_name == group_name).first().group_id
            print ('group_id',group_id)
            u1 = session.query(symbolGroupMembershipTable)\
                .where(symbolGroupMembershipTable.group_id == group_id)\
                .join(symbolTable, symbolGroupMembershipTable.symbol_id == symbolTable.symbol_id).all()   
            rtndata = []
            for u in u1:
                # print('u is '+str(u))
                # print('dir(u) is '+str(dir(u)))
                rtndata.append([u.symbol_id,u.symbols.symbol])
        rtn = {'columns':['symbol_id','symbol'],'data':rtndata}
        return rtn
    
if __name__ == '__main__':
    dbTables = DBTables()
    #allSymbols = dbTables.get_all_symbols()
    #print(allSymbols['columns'])

    #dbTables.add_symbol_to_group('MARKETWATCH_DAILY_DOWNLOAD_LIST','AAPL')

    test_symbols = dbTables.get_symbol_group('yahoo_currency_pairs')
    pprint(test_symbols)

    # my_list = []
    # for x in ticker_lists.yahoo_symbol_lists:
    #     my_list.extend(ticker_lists.yahoo_symbol_lists[x])
    # #remove duplicates
    # yahoo_daily_download_list = list(set(my_list))
    # for symbol in yahoo_daily_download_list:
    #     dbTables.add_symbol_to_group('yahoo_symbol_lists',symbol)

 

    # my_list = []
    # for x in ticker_lists.symbol_lists:
    #     my_list.extend(ticker_lists.symbol_lists[x])
    # #remove duplicates
    # marketwatch_daily_download_list = list(set(my_list))
    # for symbol in marketwatch_daily_download_list:
    #     dbTables.add_symbol_to_group('MARKETWATCH_DAILY_DOWNLOAD_LIST',symbol)

    # yahoo_index_symbols = ticker_lists.yahoo_index_symbols
    # for symbol in yahoo_index_symbols:
    #     dbTables.add_symbol_to_group('yahoo_index_symbols',symbol)

    # yahoo_commodities_symbols = ticker_lists.yahoo_commodities_symbols
    # for symbol in yahoo_commodities_symbols:
    #     dbTables.add_symbol_to_group('yahoo_commodities_symbols',symbol)

    # yahoo_interest_rate_symbols = ticker_lists.yahoo_interest_rate_symbols
    # for symbol in yahoo_interest_rate_symbols:
    #     dbTables.add_symbol_to_group('yahoo_interest_rate_symbols',symbol)

    # yahoo_currency_pairs = ticker_lists.yahoo_currency_pairs
    # for symbol in yahoo_currency_pairs:
    #     dbTables.add_symbol_to_group('yahoo_currency_pairs',symbol)

    # # yahoo_symbol_lists = ticker_lists.yahoo_symbol_lists
    # # for symbol in yahoo_symbol_lists:
    # #     dbTables.add_symbol_to_group('yahoo_symbol_lists',symbol)

    # sector_etfs = ticker_lists.sector_etfs
    # for symbol in sector_etfs:
    #     dbTables.add_symbol_to_group('sector_etfs',symbol)

    # xle_components = ticker_lists.xle_components
    # for symbol in xle_components:
    #     dbTables.add_symbol_to_group('xle_components',symbol)

    # xlu_components = ticker_lists.xlu_components
    # for symbol in xlu_components:
    #     dbTables.add_symbol_to_group('xlu_components',symbol)

    # xlk_components = ticker_lists.xlk_components
    # for symbol in xlk_components:
    #     dbTables.add_symbol_to_group('xlk_components',symbol)

    # xlre_components = ticker_lists.xlre_components
    # for symbol in xlre_components:
    #     dbTables.add_symbol_to_group('xlre_components',symbol)  

    # xlb_components = ticker_lists.xlb_components
    # for symbol in xlb_components:
    #     dbTables.add_symbol_to_group('xlb_components',symbol)

    # xli_components = ticker_lists.xli_components
    # for symbol in xli_components:
    #     dbTables.add_symbol_to_group('xli_components',symbol)

    # xlv_components = ticker_lists.xlv_components
    # for symbol in xlv_components:
    #     dbTables.add_symbol_to_group('xlv_components',symbol)

    # xlf_components = ticker_lists.xlf_components
    # for symbol in xlf_components:
    #     dbTables.add_symbol_to_group('xlf_components',symbol)

    # xlc_components = ticker_lists.xlc_components
    # for symbol in xlc_components:
    #     dbTables.add_symbol_to_group('xlc_components',symbol)

    # xly_components = ticker_lists.xly_components
    # for symbol in xly_components:
    #     dbTables.add_symbol_to_group('xly_components',symbol)

    # xlp_components = ticker_lists.xlp_components
    # for symbol in xlp_components:
    #     dbTables.add_symbol_to_group('xlp_components',symbol)

    # xtn_components = ticker_lists.xtn_components
    # for symbol in xtn_components:
    #     dbTables.add_symbol_to_group('xtn_components',symbol)

    # xsw_components = ticker_lists.xsw_components
    # for symbol in xsw_components:
    #     dbTables.add_symbol_to_group('xsw_components',symbol)

    # xsd_components = ticker_lists.xsd_components
    # for symbol in xsd_components:
    #     dbTables.add_symbol_to_group('xsd_components',symbol)
    
    # xbi_components = ticker_lists.xbi_components
    # for symbol in xbi_components:
    #     dbTables.add_symbol_to_group('xbi_components',symbol)

    # kce_components = ticker_lists.kce_components
    # for symbol in kce_components:
    #     dbTables.add_symbol_to_group('kce_components',symbol)

    # xhe_components = ticker_lists.xhe_components
    # for symbol in xhe_components:
    #     dbTables.add_symbol_to_group('xhe_components',symbol)

    # xhs_components = ticker_lists.xhs_components
    # for symbol in xhs_components:
    #     dbTables.add_symbol_to_group('xhs_components',symbol)

    # xhb_components = ticker_lists.xhb_components
    # for symbol in xhb_components:
    #     dbTables.add_symbol_to_group('xhb_components',symbol)

    # kie_components = ticker_lists.kie_components
    # for symbol in kie_components:
    #     dbTables.add_symbol_to_group('kie_components',symbol)

    # xme_components = ticker_lists.xme_components
    # for symbol in xme_components:
    #     dbTables.add_symbol_to_group('xme_components',symbol)

    # xph_components = ticker_lists.xph_components
    # for symbol in xph_components:
    #     dbTables.add_symbol_to_group('xph_components',symbol)

    # xrt_components = ticker_lists.xrt_components
    # for symbol in xrt_components:
    #     dbTables.add_symbol_to_group('xrt_components',symbol)

    # sp500_full = ticker_lists.sp500_full
    # for symbol in sp500_full:
    #     dbTables.add_symbol_to_group('sp500_full',symbol)

    # nasdaq100_components = ticker_lists.nasdaq100_components
    # for symbol in nasdaq100_components:
    #     dbTables.add_symbol_to_group('nasdaq100_components',symbol)



    """ insertSymbolGroup = dbTables.insert_symbol_group('yahoo_index_symbols')
    insertSymbolGroup = dbTables.insert_symbol_group('yahoo_commodities_symbols')
    insertSymbolGroup = dbTables.insert_symbol_group('yahoo_interest_rate_symbols')
    insertSymbolGroup = dbTables.insert_symbol_group('yahoo_currency_pairs')
    insertSymbolGroup = dbTables.insert_symbol_group('yahoo_symbol_lists')
    insertSymbolGroup = dbTables.insert_symbol_group('sector_etfs')
    insertSymbolGroup = dbTables.insert_symbol_group('xle_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xlu_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xlk_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xlre_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xlb_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xli_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xlv_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xlf_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xlc_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xly_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xlp_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xtn_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xsw_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xsd_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xbi_components')
    insertSymbolGroup = dbTables.insert_symbol_group('kce_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xhe_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xhs_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xhb_components')
    insertSymbolGroup = dbTables.insert_symbol_group('kie_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xme_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xph_components')
    insertSymbolGroup = dbTables.insert_symbol_group('xrt_components')
    insertSymbolGroup = dbTables.insert_symbol_group('sp500_full')
    insertSymbolGroup = dbTables.insert_symbol_group('nasdaq100_components')
    insertSymbolGroup = dbTables.insert_symbol_group('MARKETWATCH_DAILY_DOWNLOAD_LIST')




 """