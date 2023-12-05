

# Steps in the EOD pipeline
# 
# 1. Get list of Marketwatch and Yahoo tickers to download
# 2. Get last date in database
# 3. Download from Marketstack to staging table
#    a. Download to S3 bucket
#    b. Copy from S3 to staging table
# 4. Download from Yahoo to staging table
#    a. Download to S3 bucket
#    b. Copy from S3 to staging table
# 5. Update SYMBOLS
# 6. Update CALENDAR table
# 7. Update EOD_QUOTES table from Marketstack staging table
# 8. Update EOD_QUOTES table from Yahoo staging table
# 9. Update EOD_MOVING_AVERAGE_INDICATORS table
# 10. Update EOD_MOVING_AVERAGE_SLOPES table
# 11. Update INDICATOR_STATS table
# 12. Update GAUGES table

# Steps in EOD quality control pipeline
#
# 1. Get list of Marketwatch and Yahoo tickers to check
# 2. Quality checks EOD_QUOTES table
#    a. Check for missing dates
#    b. Check for missing or out of whack data
# 3. Quality checks EOD_MOVING_AVERAGE_INDICATORS table
#    a. Check for missing dates
#    b. Check for missing or out of whack data
# 4. Quality checks EOD_MOVING_AVERAGE_SLOPES table
#    a. Check for missing dates
#    b. Check for missing or out of whack data
# 5. Quality checks INDICATOR_STATS table
#    a. Check for missing dates
#    b. Check for missing or out of whack data
# 6. Quality checks GAUGES table
#    a. Check for missing dates
#    b. Check for missing or out of whack data




# 1. Get list of Marketwatch and Yahoo tickers to download

from rds_skywalker import RDSSkywalker
import pandas as pd

def getTickersForGroup(group_name):
    myRDS = RDSSkywalker()
    sql = 'select ticker from symbols where eod = 1'
    df = myRDS.getDataFrame(sql)
    return df



# print ('Fetching latest Marketstack quotes...')
#     updateMarketStackEOD(dateFrom, dateTo)
    
#     print ('Fetching latest Marketstack quotes...')
#     updateYahooEOD(dateFrom, dateTo)
    
#     print('Updating symbol table...')
#     myRDS.connectAndRunStoredProcedure('CALL update_symbols()')
    
#     print('Updating calendar table...')
#     myRDS.connectAndRunStoredProcedure('CALL update_calendar()')
    
#     print('Updating EOD quotes from MarketWatch...')
#     execString = "call update_eod_quotes_marketstack_from_date('{}')".format(dateFrom)
#     myRDS.connectAndRunStoredProcedure(execString)
    
    
#     print('Updating EOD quotes from Yahoo...')
#     execString = "call update_eod_quotes_yahoo_from_date('{}')".format(dateFrom)
#     myRDS.connectAndRunStoredProcedure(execString)
    
#     print('Updating EOD moving average indicators...')
#     execString = "call update_eod_moving_average_indicators_from_date('{}')".format(dateFrom)
#     myRDS.connectAndRunStoredProcedure(execString)
    
#     print('Updating EOD moving average slopes...')
#     execString = "call update_eod_moving_average_slopes_from_date('{}')".format(dateFrom)
#     myRDS.connectAndRunStoredProcedure(execString)
    
#     print('Updating indicator stats...')
#     myRDS.connectAndRunStoredProcedure('call update_indicator_stats()')
    
#     print('Updating gauges...')
#     execString = "call update_gauges_from_indicators_eod_by_date('{}','{}')".format(dateFrom,dateTo)
#     myRDS.connectAndRunStoredProcedure(execString)    
