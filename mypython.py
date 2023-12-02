from app import app

from ETM_AWS_Logger import ETM_AWS_Logger

import rds_skywalker

rds_skywalker.printVersion()


etmLogger = ETM_AWS_Logger(1, 'MarketDataService')

etmLogger.log('Starting mypython.py')


# etmLogger.log('Not doing much today, so flushing and exiting')
# etmLogger.flush()
# exit()


