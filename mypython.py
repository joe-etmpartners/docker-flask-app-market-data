import sys
import datetime
import logging
import watchtower

from app import app

#
def init_logging(logfile, loglevel):
    """
    Defines the logging destination, level and format.
    """
    
    logging_levels = [logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]

    try:
        logging_level = logging_levels[loglevel]
    except TypeError:
        logging_level = logging.NOTSET

    logging_format = '%(asctime)20s : %(filename)11s : %(funcName)16s : Line %(lineno)5d : Process %(processName)15s %(process)6d : Thread %(threadName)10s %(thread)6d : %(levelname)10s %(message)s'

    logger = logging.getLogger('awslogger')
    
    logger.setLevel(logging.DEBUG) 
    console_handler = logging.StreamHandler()
    stream_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    cw_handler = watchtower.CloudWatchLogHandler(log_group="market-data-app", stream_name=stream_name)
    #logger.addHandler(console_handler)
    logger.addHandler(cw_handler)
    formatter = logging.Formatter(logging_format)
    cw_handler.setFormatter(formatter)
    logger.error('ERROR MESSAGE #1')
    logger.error('This is a new message sent after 9pm')
    return cw_handler
    
    # Force push the logs to CloudWatch
    cw_handler.flush()
    try:
        x = 1 / 0
    except ZeroDivisionError:
        logger.exception('EXCEPTION log msg')  # logs at same level as logging.error() but includes traceback
    
import os

secret_fpath = f'/app/aws_public_key'
existence = os.path.exists(secret_fpath)
if existence:
    v2 = open(secret_fpath).read().rstrip('\n')
    print("AWS public key file exists and contains: " + v2)
    os.environ['AWS_ACCESS_KEY_ID'] = v2
else:
    print("AWS public key file does not exist")

secret_fpath = f'/app/aws_private_key'
existence = os.path.exists(secret_fpath)
if existence:
    v2 = open(secret_fpath).read().rstrip('\n')
    print("AWS private key file exists and contains: " + v2)
    os.environ['AWS_SECRET_ACCESS_KEY'] = v2
else:
    print("AWS private key file does not exist")
#

print("THIS SHOULD PRINT TO DOCKER LOG")
sys.stdout.flush()  
print (f"Name = {__name__}")
sys.stdout.flush() 

secret_fpath = f'/app/secrets.txt'
existence = os.path.exists(secret_fpath)
#FUDGE

    
if existence:
    v2 = open(secret_fpath).read().rstrip('\n')
    print("Secret file exists and contains: " + v2)
else:
    print("Secret file does not exist")



for name, value in os.environ.items():
    print("{0}: {1}".format(name, value))
sys.stdout.flush() 

print("Starting mypython.py")
sys.stdout.flush()
cw_handler=init_logging('', 0)
logger = logging.getLogger('awslogger')
logger.debug('DEBUG log msg #2')
logger.error('ERROR MESSAGE A1')
cw_handler.flush()
logger.error('ERROR MESSAGE A2')
logger.debug('DEBUG log msg B1')

if __name__ == "__main__":
    #pass
    # Documentation for argparse:   https://docs.python.org/3/library/argparse.html#action 
    # Documentation for logging:    https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
    #                               https://docs.python.org/3/library/logging.html
    #                               https://docs.python.org/3/library/logging.html#logging-levels

    print("Starting mypython.py")
    sys.stdout.flush()
    init_logging('', 0)

    logger = logging.getLogger('awslogger')
    logger.debug('DEBUG log msg #2')
    # logging.info('INFO log msg')
    # logging.warning('WARNING log msg')
    # logging.error('ERROR log msg')
    # logging.critical('CRITICAL log msg')
