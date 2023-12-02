import sys
import os
import datetime
import logging
import watchtower


class ETM_AWS_Logger(object):
    """
    This class is used to log messages to AWS CloudWatch.
    """
    # Define class variables for SINGLETON style access to logger and log handler

    log_level = logging.NOTSET
    logger = None
    cw_handler = None
    console_handler = None
    logging_format = '%(asctime)20s : %(filename)11s : %(funcName)16s : Line %(lineno)5d : Process %(processName)15s %(process)6d : Thread %(threadName)10s %(thread)6d : %(levelname)10s %(message)s'
    logger_name = 'awslogger'
    app_name = 'Unnamed App'
    stream_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")


    # Set the AWS credentials
    secret_fpath = f'/app/aws_public_key'
    v2 = open(secret_fpath).read().rstrip('\n')
    os.environ['AWS_ACCESS_KEY_ID'] = v2

    secret_fpath = f'/app/aws_private_key'
    v2 = open(secret_fpath).read().rstrip('\n')
    os.environ['AWS_SECRET_ACCESS_KEY'] = v2

    
    def __init__(self, log_level, app_name):
        """
        Initialize the logger.
        """
        self.app_name = app_name    
        self.logger = logging.getLogger(self.logger_name)

        logging_levels = [logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
        try:
            self.log_level = logging_levels[log_level]
        except TypeError:
            self.log_level = logging.NOTSET
        self.logger.setLevel(self.log_level) 

        #self.console_handler = logging.StreamHandler()
        #self.logger.addHandler(console_handler)

        self.cw_handler = watchtower.CloudWatchLogHandler(log_group=self.app_name, stream_name=self.stream_name)
        self.logger.addHandler(self.cw_handler)

        formatter = logging.Formatter(self.logging_format)
        self.cw_handler.setFormatter(formatter)
        
    def log(self, msg):
        """
        Logs the message.
        """
        self.logger.error(msg)

    def log_exception(self, msg):
        """
        Logs the exception.
        """
        self.logger.exception(msg)

    def log_debug(self, msg):
        """
        Logs the debug message.
        """
        self.logger.debug(msg)

    def log_info(self, msg):
        """
        Logs the info message.
        """
        self.logger.info(msg)

    def log_warning(self, msg):
        """
        Logs the warning message.
        """
        self.logger.warning(msg)

    def log_error(self, msg):
        """
        Logs the error message.
        """
        self.logger.error(msg)

    def log_critical(self, msg):
        """
        Logs the critical message.
        """
        self.logger.critical(msg)

    def flush(self):
        """
        Force push the logs to CloudWatch.
        """
        for handler in self.logger.handlers:
            handler.flush()
