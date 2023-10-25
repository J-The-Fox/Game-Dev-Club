# Built-In Modules
import os
# External Modules
import requests
# Custom Modules
import logger

# -----=====[Logging Paramaters]=====----- #
_logging_mode         = logger.Logger.LOGTOTERMANDFILE
_logging_write_mode   = 'w'
_logging_format       = ['dt', 'lvl', 'msg']
_log_file             = "Narro.log"
_logging_file_path    = os.path.join(os.path.dirname(__file__).replace("modules", "docs/logs"))
_logging_levels_shown = [logger.Logger.BUG, logger.Logger.DEBUG, logger.Logger.INFO, logger.Logger.WARN, logger.Logger.ERROR, logger.Logger.CRITICAL]

logging = logger.Logger(mode=_logging_mode, format=_logging_format, log_file=_log_file, log_file_path=_logging_file_path, write_mode=_logging_write_mode, levelsShown=_logging_levels_shown)


# Adding A Running Time Decarator Breakes This Function, Returns None Always
def check_connection():
    """
    Check If The Computer Is Connected To The Internet
    """    

    # Try To Connect To The Internet, If It Fails, Return False, Else, Return True
    try:
        requests.get("https://stackoverflow.com") # Why Not Use stackoverflow.com?
        logging.write(f"[network]: Succesfully Reached Out To URL 'https://stackoverflow.com'", lvl=logger.Logger.INFO)
        return True # Return True If There Is No Error
    except requests.exceptions.ConnectionError:
        logging.write(f"[network]: Netork Error.", lvl=logger.Logger.ERROR, extra_msg="Could Not Reach URL: https://stackoverflow.com") # Log The Error If There Is One
        return False # Return False If There Is An Error
