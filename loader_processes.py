

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

from dbtables import DBTables
import pandas as pd
from datetime import date
import boto3

import timeit
import time

from loader_marketstack_eod import Loader_MarketStack_EOD


# 1. Get list of Marketwatch tickers to download
# 2. Get last date in database
# 3. Download from Marketstack to staging table
#    a. Download to S3 bucket

def sendSQSMsg(queueName = 'MarketStack_EOD_NewS3File',msg='No message'):
    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName=queueName)

    # You can now access identifiers and attributes
    print(queue.url)
    print(queue.attributes.get('DelaySeconds'))
    # Create a new message
    response = queue.send_message(MessageBody=msg)

def getSQSMsg(queueName = 'MarketStack_EOD_NewS3File'):
    # Get the service resource
    sqs = boto3.resource('sqs')

    # Get the queue. This returns an SQS.Queue instance
    queue = sqs.get_queue_by_name(QueueName=queueName)

    # Process messages by printing out body and optional author name
    messages = queue.receive_messages(MaxNumberOfMessages=1,VisibilityTimeout=600,WaitTimeSeconds=5)

    if len(messages) == 0:
        print("No messages on queue")
        return None
    
    message = messages[0]

    print(message.body)

    return (message)

        # # Let the queue know that the message is processed
        # message.delete()


def fetchLatestMarketWatchEOD():
    print("Entering updateMarketWatchEOD()", flush=True)
    db = DBTables()
    symbols = db.getTickersForGroup('MARKETWATCH_DAILY_DOWNLOAD_LIST')

    lastDate = db.getLastDate()
    dateFrom = str(lastDate)
    today = date.today()
    dateTo = str(today)

    tic = time.perf_counter()

    counter = 0

    tickers = []
    for ticker in symbols:
        counter = counter + 1
        print(ticker, flush=True)
        tickers.append(ticker)
        # print("tickers = ", tickers)
        # print("counter = ", counter)
        if counter % 50 == 0:
            print("Modula 50 == 0", flush=True)
            csv_tickers = ','.join(tickers)
            eodParams = {'symbols':csv_tickers,
                        'date_from':dateFrom,
                        'date_to':dateTo
                    }
            loader = Loader_MarketStack_EOD(additionalParams=eodParams)
            loader.fetchAllPages()
            tickers = []
            keyNames = loader.getS3Keynames()
            print("keyNames = ", keyNames, flush=True)  
            for keyName in keyNames:
                sendSQSMsg(queueName = 'MarketStack_EOD_NewS3File',msg=keyName)
            loader.clearS3Keynames()

    toc = time.perf_counter()
    print("Time difference:",(toc - tic)," seconds", flush=True)


    return symbols

def toStagingMarketWatchEOD():
    print("Entering toStagingMarketWatchEOD()", flush=True)

    loader = Loader_MarketStack_EOD()
    tableName = loader.importTableName()
    
    while True:
        message = getSQSMsg(queueName = 'MarketStack_EOD_NewS3File')
        if message is None:
            print("toStagingMarketWatchEOD: No messages on queue")
            return
        keyName = message.body
        print("keyName = ", keyName, flush=True)
        success = loader.copyS3FileToDB(fileKey=keyName, tableName=tableName)

        if success:
            print("Successfully copied file to staging table")
            print("Deleting message from queue", flush=True)
            message.delete()
        else:
            print("Failed to copy file to staging table")
            print("Leaving message on queue", flush=True)


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
