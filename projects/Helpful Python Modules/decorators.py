import time
import os
from functools import wraps

import logger

# -----=====[Logging Paramaters]=====----- #
_logging_mode         = logger.Logger.LOGTOTERMANDFILE
_logging_write_mode   = 'w'
_logging_format       = ['dt', 'lvl', 'msg']
_log_file             = "Narro.log"
_logging_file_path    = os.path.join(os.path.dirname(__file__).replace("modules", "docs/logs"))
_logging_levels_shown = [logger.Logger.DEBUG, logger.Logger.INFO, logger.Logger.WARN, logger.Logger.ERROR, logger.Logger.CRITICAL]

logging = logger.Logger(mode=_logging_mode, format=_logging_format, log_file=_log_file, log_file_path=_logging_file_path, write_mode=_logging_write_mode, levelsShown=_logging_levels_shown)

# This File Is For Creating Decorators To Use In Other Files

def memorize(func) -> None:
    """Take A Function And Store The Argumemnts And The Keyword Arguments In A Cache To Speed Up Repetitive Tasks Such As Calculating Digits"""

    # Create A Cache
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        # The Key Is The Arguments And Keyword Arguments Added Together In A String
        # If The Key Is Not Stored In The Cache, Store It In The Cache
        if key not in cache:
            cache[key] = func(*args, **kwargs)

        return cache[key]
    
    return wrapper # Return The Wrapper

def runningTime(func):
    """Times How Long a Function or Method Takes To Complete"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        startTime = time.perf_counter()

        func(*args, **kwargs)

        endTime = time.perf_counter()

        totalTime = endTime - startTime

        logging.write(f"[time]: {func.__name__} Completed In {totalTime} Seconds.", lvl=logger.Logger.DEBUG)
    
    return wrapper # Return The Wrapper