from app import app
from time import sleep
import sys

from ETM_AWS_Logger import ETM_AWS_Logger

from ETMProcessManager import ETMProcessManager
from ETMProcessManager import ETMProcess

import rds_skywalker

from loader_marketstack import loader_marketstack_test
from loader_marketstack_eod import loader_marketstack_eod_test
from loader_processes import fetchLatestMarketWatchEOD
from loader_processes import toStagingMarketWatchEOD


rds_skywalker.printVersion()


print('Starting mypython.py', flush=True)

etmLogger = ETM_AWS_Logger(1, 'MarketDataService')

etmLogger.debug('Starting mypython.py')

fetchLatestMarketWatchEOD()
toStagingMarketWatchEOD()

etmLogger.flush()

#loader_marketstack_eod_test()

# rdsCalendar = rds_skywalker.RDSCalendar()
# rtn = rdsCalendar.getLastDate()
# print ('last date: ' + str(rtn))
# sys.stdout.flush() 

# pm = ETMProcessManager()
# process1 = ETMProcess('GetLastDate', 'Get last date from database', getLastDate)
# pm.register_process(process1)

# print('All process info: {}'.format(pm.get_all_process_info()))
# sys.stdout.flush() 

# sleep(1)

# print('Process 1 info: {}'.format(process1.info()))

# print('About to start process 1')
# sys.stdout.flush() 

# pm.run_process('GetLastDate')


# from pprint import pprint
# for i in range(20):
#     pprint(pm.get_all_process_info())
#     sys.stdout.flush() 
#     sleep(2)



# etmLogger.log('Not doing much today, so flushing and exiting')
# etmLogger.flush()
# exit()


