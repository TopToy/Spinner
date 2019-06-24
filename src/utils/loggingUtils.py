import logging
import os

from datetime import datetime

logger_dir = '/tmp/Spinner/logs/'

def get_logger(
        LOG_FORMAT     = '%(asctime)s %(name)s %(levelname)s %(message)s',
        LOG_NAME       = '',
        LOG_FILE_INFO  = os.path.join(logger_dir, datetime.now().strftime("%m-%d-%Y:%H:%M") +'.log'),
        LOG_FILE_ERROR = os.path.join(logger_dir, datetime.now().strftime("%m-%d-%Y:%H:%M") +'.err')):

    os.makedirs(logger_dir, exist_ok=True)
    log           = logging.getLogger(LOG_NAME)
    log_formatter = logging.Formatter(LOG_FORMAT)

    # comment this to suppress console output
    # stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(log_formatter)
    # log.addHandler(stream_handler)

    file_handler_info = logging.FileHandler(LOG_FILE_INFO, mode='w')
    file_handler_info.setFormatter(log_formatter)
    file_handler_info.setLevel(logging.INFO)
    log.addHandler(file_handler_info)

    file_handler_error = logging.FileHandler(LOG_FILE_ERROR, mode='w')
    file_handler_error.setFormatter(log_formatter)
    file_handler_error.setLevel(logging.ERROR)
    log.addHandler(file_handler_error)

    log.setLevel(logging.INFO)

    return log

