# Built-In Modules
import os
# Custom Modules
import logger

# -----=====[Logging Paramaters]=====----- #
_logging_mode         = logger.Logger.LOGTOTERM # This Is Where The Goes, It Can Go To The Terminal, A File Or Both. It Is Set To Terminal For Right Now
_logging_write_mode   = None # This Is The Write Mode If You Were Writing A Log File. 'w'  Clears It Nn Start While 'a' Appends To The End Of The Existing File
_logging_format       = ['dt', 'lvl', 'msg'] # This Is The Format Of Log File
_log_file             = "test.log" # This Is The File Name For The Log File If It Were Set
_logging_file_path    = os.path.dirname(__file__) # This Is Where The Log File Would Go If It Were Set. It Is Set To Be In The Same Directory Of This File
_logging_levels_shown = [logger.Logger.BUG, logger.Logger.DEBUG, logger.Logger.INFO, logger.Logger.NOTICE, logger.Logger.WARN, logger.Logger.ERROR, logger.Logger.CRITICAL] # This Shows What Levels Are Shown When Logging Happens

logging = logger.Logger(mode=_logging_mode, format=_logging_format, log_file=_log_file, log_file_path=_logging_file_path, write_mode=_logging_write_mode, levelsShown=_logging_levels_shown)
# This Sets The logging Variable To Be The 'Logger' Class From The Module 'logger'

# This Is All The Methods The Current Logger Has
logging.init # -> Initlize The Logger
logging.write # -> Writes Out A Message From The 
logging.close # -> Adds A Closing Statment And Exit Code To The Log

logging.clear_log_file # -> Erases The Current Logging File

logging.get_format # -> Returns The Format List
logging.get_write_mode # Returns The Write Mode

# The () Are Removed To Make Them Not Callable

# Here Are Some Constants
# -----=====[Levels]=====----- #
logging.BUG
logging.DEBUG
logging.INFO
logging.NOTICE
logging.WARN
logging.WARNING
logging.ERROR
logging.CRITICAL
# -----=====[Write Modes]=====----- #
logging.APPEND
logging.OVERWRITE
# -----=====[Logging Modes]=====----- #
logging.LOGTOFILE
logging.LOGTOTERM
logging.LOGTOTERMANDFILE
# -----=====[Version]=====----- #
logging.VERSION

print("This Is Text In A Print Statment!")
logging.write("This Is Text But In The logging.write Method With A lvl Of INFO!", lvl=logging.INFO)

print("------------------------------------------")

# Here Are All The Levels The Logger Can Have And What They Look Like
logging.write("BUG!", lvl=logging.BUG)
logging.write("DEBUG!", lvl=logging.DEBUG)
logging.write("INFO!", lvl=logging.INFO)
logging.write("NOTICE!", lvl=logging.NOTICE)
logging.write("WARN!", lvl=logging.WARN)
logging.write("WARNING!", lvl=logging.WARNING)
logging.write("ERROR!", lvl=logging.ERROR)
logging.write("CRITICAL!", lvl=logging.CRITICAL)

print("----------------------------------------------------")

# With NOTICE, WARN, WARNING, ERROR And CRITICAL, You Can Also Have An Extra Message Below Using The Keyword Argument extra_msg
logging.write("This Is Normal Text!", lvl=logging.NOTICE, extra_msg="This Is Extra Text!")

logging.write(f"This Is The Version Of The Logger: {logging.VERSION}!", lvl=logging.INFO)
logging.write("It Got Upadated From 0.1.6 To 0.1.7 :)", lvl=logging.INFO)

# Logging Makes Debuging So Much Easier And Also It Is Neat To See What The Program Is Doing 
