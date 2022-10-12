import logging

'''
NOTSET = 0
DEBUG = 10
INFO = 20
WARN = 30
ERROR = 40
CRITICAL = 50
'''


def Logger(level=10, file=None):
    logger = logging.getLogger()
    logger.setLevel(level)
    fmt = "[%(asctime)s] %(levelname)s {%(filename)s %(funcName)s : %(lineno)d} - %(message)s]"
    handler = logging.FileHandler(file) if file else logging.StreamHandler()
    handler.setFormatter(logging.Formatter(fmt))
    logger.addHandler(handler)
    return logger
