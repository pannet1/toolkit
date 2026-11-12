import logging
from logging.handlers import RotatingFileHandler

'''
NOTSET = 0
DEBUG = 10
INFO = 20
WARN = 30
ERROR = 40
CRITICAL = 50
'''

_FMT = "[%(asctime)s.%(msecs)03d] %(levelname)s %(module)s:%(lineno)d | %(message)s"
_DATEFMT = "%d-%m-%Y %H:%M:%S"


def Logger(level=10, file=None, name="app", show=False, max_mb=20, backups=2):
    """Idempotent logger factory.

    - Same instance is returned for the same `name`, so calling Logger()
      repeatedly (re-imports, tests) never duplicates handlers.
    - `file`     : write to this file (rotated at max_mb, keeps `backups`).
    - `show`     : ALSO print to stdout. file+console work together.
    - Format includes module:lineno and ms — the last line before a hang
      tells you exactly which module froze.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False
    formatter = logging.Formatter(_FMT, datefmt=_DATEFMT)

    if file and not any(getattr(h, "_tk_file", False) for h in logger.handlers):
        fh = RotatingFileHandler(
            file, maxBytes=max_mb * 1024 * 1024, backupCount=backups
        )
        fh.setFormatter(formatter)
        fh._tk_file = True
        logger.addHandler(fh)

    if (show or not file) and not any(
        getattr(h, "_tk_stream", False) for h in logger.handlers
    ):
        sh = logging.StreamHandler()
        sh.setFormatter(formatter)
        sh._tk_stream = True
        logger.addHandler(sh)

    return logger
