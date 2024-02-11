

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
from loader_yahoo import Loader_Yahoo_EOD


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



def fetchLatestEOD(loader_class, group_name, queueName, dateFrom=None, dateTo=None):
    print(f"Entering fetchLatestEOD({loader_class.__name__}, {group_name})", flush=True)
    print("queueName = ", queueName, flush=True)
    print("dateFrom = ", dateFrom, flush=True)
    print("dateTo = ", dateTo, flush=True)
    print("group_name = ", group_name, flush=True)
    db = DBTables()
    symbols = db.getTickersForGroup(group_name)

    print ("symbols = ", symbols, flush=True)

    if dateFrom is None:
        lastDate = db.getLastDate()
        dateFrom = str(lastDate)

    print("dateFrom = ", dateFrom, flush=True)

    if dateTo is None:
        today = date.today()
        dateTo = str(today)

    print("dateTo = ", dateTo, flush=True)

    tic = time.perf_counter()
    counter = 0

    tickers = []
    for ticker in symbols:
        counter = counter + 1
        print(ticker, flush=True)
        tickers.append(ticker)
        if (counter % 50 == 0 or counter == len(symbols)):
            print("Modula 50 == 0", flush=True)
            csv_tickers = ','.join(tickers)
            eodParams = {'symbols':csv_tickers,
                        'date_from':dateFrom,
                        'date_to':dateTo
                    }
            loader = loader_class(additionalParams=eodParams)
            loader.fetchAllPages()
            tickers = []
            keyNames = loader.getS3Keynames()
            print("keyNames = ", keyNames, flush=True)  
            for keyName in keyNames:
                sendSQSMsg(queueName = queueName, msg=keyName)
            loader.clearS3Keynames()

    toc = time.perf_counter()
    print("Execution time:",(toc - tic)," seconds", flush=True)
    return symbols

def fetchLatestMarketStackEOD():
    print("Entering fetchLatestMarketStackEOD()", flush=True)
    fetchLatestEOD(Loader_MarketStack_EOD, 'MARKETWATCH_DAILY_DOWNLOAD_LIST', 'MarketStack_EOD_NewS3File')

def fetchLatestYahooEOD():
    fetchLatestEOD(Loader_Yahoo_EOD, 'yahoo_symbol_lists', 'Yahoo_EOD_NewS3File')


def toStagingEOD(loader_class, queue_name):
    print(f"Entering toStagingEOD({loader_class.__name__})", flush=True)

    loader = loader_class()
    tableName = loader.importTableName()
    
    tic = time.perf_counter()

    while True:
        message = getSQSMsg(queueName=queue_name)
        if message is None:
            print(f"toStagingEOD: No messages on {queue_name} queue")
            toc = time.perf_counter()
            print("Execution time:", (toc - tic), " seconds", flush=True)
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

def toStagingMarketStackEOD():
    toStagingEOD(Loader_MarketStack_EOD, 'MarketStack_EOD_NewS3File')

def toStagingYahooEOD():
    toStagingEOD(Loader_Yahoo_EOD, 'Yahoo_EOD_NewS3File')

    

# 5. Update SYMBOLS
# 6. Update CALENDAR table
# 7. Update EOD_QUOTES table from Marketstack staging table
# 8. Update EOD_QUOTES table from Yahoo staging table
# 9. Update EOD_MOVING_AVERAGE_INDICATORS table
# 10. Update EOD_MOVING_AVERAGE_SLOPES table
# 11. Update INDICATOR_STATS table
# 12. Update GAUGES table

def updateMainTables(fromDate='2000-01-01', toDate='2024-12-30'):
    print("", flush=True)
    db = DBTables()

    print("Updating SYMBOLS", flush=True)
    tic = time.perf_counter()
    db.updateSymbols()
    toc = time.perf_counter()
    print("Execution time:",(toc - tic)," seconds", flush=True)

    print("Updating CALENDAR", flush=True)
    tic = time.perf_counter()
    db.updateCalendar()
    toc = time.perf_counter()
    print("Execution time:",(toc - tic)," seconds", flush=True)

    print("Updating EOD_QUOTES", flush=True)
    tic = time.perf_counter()
    db.updateEODQuotes(fromDate=fromDate)
    toc = time.perf_counter()
    print("Execution time:",(toc - tic)," seconds", flush=True)

    print("Updating EOD_MOVING_AVERAGE_INDICATORS", flush=True)
    tic = time.perf_counter()
    db.updateEODMovingAverageIndicators(fromDate=fromDate)
    toc = time.perf_counter()
    print("Execution time:",(toc - tic)," seconds", flush=True)

    print("Updating EOD_MOVING_AVERAGE_SLOPES", flush=True)
    tic = time.perf_counter()
    db.updateEODMovingAverageSlopes(fromDate=fromDate)
    toc = time.perf_counter()
    print("Execution time:",(toc - tic)," seconds", flush=True)

    print("Updating INDICATOR_STATS", flush=True)
    tic = time.perf_counter()
    db.updateIndicatorStats()
    toc = time.perf_counter()
    print("Execution time:",(toc - tic)," seconds", flush=True)

    print("Updating GAUGES", flush=True)
    tic = time.perf_counter()
    db.updateGauges(fromDate=fromDate)
    toc = time.perf_counter()
    print("Execution time:",(toc - tic)," seconds", flush=True)




