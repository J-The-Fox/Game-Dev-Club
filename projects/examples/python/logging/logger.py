"""
Helps with logging by providing functions to easily write out to a file, terminal or both

- logger.Logger: is for logging with the custom logger.
- logger.Logger_module:  is for logging with the logger module.

Note: This module will use the colorama if it is installed
"""

# This Is A Logging Module And Class That I Created That I Use In Multiple Other Projects
# Logging Is A Good Thing To Get The Hang Of As It Allows You To Have A Good Idea Of What's
# Gonig On While Your Code Is Running

import datetime
import os
import inspect

_IMPORTERROR = []

try:
    import colorama
except ImportError:
    _IMPORTERROR.append("colorama")

# Logger Class
class Logger():
    """
    Logging Class

    Log Modes:

    There are 3 different log modes
    - LOGTOFILE
    - LOGTOTERM
    - LOGTOTERMANDFILE

    These are set when you first call it.
    EX: Logger = logger.Logger(logger.Logger.LOGTOTERM)

    Note: The default path for the logfile is in the same directory as logger.py and called 'main.log'.
    To change the log file name, pass in log_file = 'log_file_name.extension' to change the name / extension
    To change the log file location, pass in log_file_path = 'location/of/logfile' to change the location

    Write Mode:

    2 Write Modes are able to be used when logging to a file. 
    Use 'a' for appending the new log to the existing file.
    Use 'w' for erasing and starting a new log on the existing file

    Format:

    The format is in a list with 3 possible values being: dt, msg, and lvl. 
    'dt' is datetime and pulls the date and time using datetime.datetime.now().
    'lvl' is the level that gets passed in when using the .write() call.
    'msg' is the message that gets passed in when using the .write() call.

    A format like ['dt', 'lvl', 'msg'] would be displayed as: '+ 2023-01-20 10:49:26.358819 - [INFO] - Message Passed Through'

    Log Levels:

    There are 6 possible log levels
    - BUG
    - DEBUG
    - INFO
    - WARN / WARNING
    - ERROR
    - CRITICAL

    When using WARN, WARNING, ERROR, or CRITICAL, the extra_msg argument can be passed in to provide more information.
    If used when on INFO or DEBUG, the extra_msg argument will be ignored.

    EX: + 2023-01-20 10:54:02.692807 - [ERROR] - Could Not Find File.
        ╰─> Could Not Find File 'main.py'.
    """

    # Log Level
    BUG = "BUG"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARN = "WARN"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

    # Log Mode
    LOGTOFILE = 1
    LOGTOTERM = 2
    LOGTOTERMANDFILE = 3

    # Write Mode
    APPEND = "a"
    OVERWRITE = "w"

    # Version
    VERSION = "0.1.4"

    def __init__(self, mode: int, format: list, log_file: str = "main.log", log_file_path: str = None, write_mode: str = "w", levelsShown = [DEBUG, INFO, WARN, ERROR, CRITICAL]) -> None:
        if log_file_path is None:
            self.log_file_path = os.path.join(os.path.dirname(__file__), log_file)
        else:
            self.log_file_path = os.path.join(log_file_path, log_file)
        
        self.mode = mode
        self.write_mode = write_mode
        self.format = format

        self.levelsShown = levelsShown

        try:
            import colorama
            self.use_color = True
        except ImportError:
            self.use_color = False
            print(colorama.Fore.WHITE)

    def init(self) -> None:
        """
        Initilize The Logger
        """
        # If the user is only writting to the terminal, no need to create a new log file, just skip creating / clearing on the init
        if self.mode == 2:
            return
        # If the user has selected one of two log to file modes, either clear the file or append to the existing file
        if self.write_mode == "w":
            with open(self.log_file_path, self.write_mode) as logfile:
                logfile.write("")
                logfile.close()
        elif self.write_mode == "a":
            with open(self.log_file_path, self.write_mode) as logfile:
                logfile.write("\n")
                logfile.close()
        return # Return when done

    def write(self, msg: str, lvl: str, extra_msg: str = None) -> None:
        """
        Writes a log to the terminal, a file or both using the format provided

        Uses color if the colorama module is installed
        """

        output_string = ""
        format_list = ["+ "]

        # Use The Formatting Provided In The init Function and Create The Log
        index = 0
        for format_data in self.format:
            if str(format_data).capitalize() == "Dt":
                format_list.append(str(datetime.datetime.now()))
            if str(format_data).capitalize() == "Msg":
                format_list.append(msg)
            if str(format_data).capitalize() == "Lvl" and self.use_color is True:
                if lvl == "BUG":
                    format_list.append(f"[{colorama.Fore.LIGHTGREEN_EX}{lvl}{colorama.Fore.RESET}]")
                elif lvl == "DEBUG":
                    format_list.append(f"[{colorama.Fore.BLUE}{lvl}{colorama.Fore.RESET}]")
                elif lvl == "INFO":
                    format_list.append(f"[{colorama.Fore.CYAN}{lvl}{colorama.Fore.RESET}]")
                elif "WARN" in lvl:
                    format_list.append(f"[{colorama.Fore.LIGHTYELLOW_EX}{lvl}{colorama.Fore.RESET}]")
                elif lvl == "ERROR" or lvl == "CRITICAL":
                    format_list.append(f"[{colorama.Fore.LIGHTRED_EX}{lvl}{colorama.Fore.RESET}]")
            elif str(format_data).capitalize() == "Lvl":
                format_list.append(f"[{lvl}]")
            index += 1
            if index < 2:
                format_list.append(" - ")
            if index == 2:
                format_list.append(": ")

        if "DEBUG" in str(format_list) and "DEBUG" not in self.levelsShown:
            return
        if "INFO" in str(format_list) and "INFO" not in self.levelsShown:
            return
        if "WARN" in str(format_list) and "WARN" not in self.levelsShown or "WARNING" in format_list and "WARNING" not in self.levelsShown:
            return
        if "ERROR" in str(format_list) and "ERROR" not in self.levelsShown:
            return
        if "CRITICAL" in str(format_list) and "CRITICAL" not in self.levelsShown:
            return

        if self.mode == 1:
            with open(self.log_file_path, "a") as logfile:
                if self.use_color is True:
                    logfile.write(output_string.join(format_list).replace(colorama.Fore.WHITE, "").replace(colorama.Fore.BLUE, "").replace(colorama.Fore.CYAN, "").replace(colorama.Fore.LIGHTYELLOW_EX, "").replace(colorama.Fore.LIGHTRED_EX, "").replace("[39m", "") + "\n")
                else:
                    logfile.write(output_string.join(format_list) + "\n")
                if extra_msg is not None and lvl == "BUG" or extra_msg is not None and lvl == "WARN" or extra_msg is not None and lvl == "WARNING" or extra_msg is not None and lvl == "ERROR" or extra_msg is not None and lvl == "CRITICAL":
                    logfile.write(f"╰─> {extra_msg}\n")

        if self.mode == 2:
            print(output_string.join(format_list))
            if extra_msg is not None and lvl == "BUG" or extra_msg is not None and lvl == "WARN" or extra_msg is not None and lvl == "WARNING" or extra_msg is not None and lvl == "ERROR" or extra_msg is not None and lvl == "CRITICAL":
                print(f"╰─> {extra_msg}")

        if self.mode == 3:
            with open(self.log_file_path, "a") as logfile:
                if self.use_color is True:
                    logfile.write(output_string.join(format_list).replace(colorama.Fore.WHITE, "").replace(colorama.Fore.BLUE, "").replace(colorama.Fore.CYAN, "").replace(colorama.Fore.LIGHTYELLOW_EX, "").replace(colorama.Fore.LIGHTRED_EX, "").replace("[39m", "") + "\n")
                else:
                    logfile.write(output_string.join(format_list) + "\n")
                print(output_string.join(format_list))
                if extra_msg is not None and lvl == "BUG" or extra_msg is not None and lvl == "WARN" or extra_msg is not None and lvl == "WARNING" or extra_msg is not None and lvl == "ERROR" or extra_msg is not None and lvl == "CRITICAL":
                    logfile.write(f"╰─> {extra_msg}\n")
                    print(f"╰─> {extra_msg}")
        return

    def close(self, exit_code: int | str, exit_process: str = None, exit_reason: str = None) -> None:
        # if "0" in str(exit_code).lower and "x" in str(exit_code).lower():
        # else:
        #     self.write(msg=f"[logger-close]: Exit Code Error Given, '{exit_code}', But No Reason Given", lvl=Logger.ERROR)

        if exit_reason is None and exit_process is None:
            self.write(msg=f"[logger-close]: {inspect.stack()[1][1]} Exited With Code {exit_code}.", lvl=Logger.INFO)
        elif exit_reason is None:
            self.write(msg=f"[logger-close]: {exit_process} Exited With Code {exit_code}.", lvl=Logger.INFO)
        elif exit_process is None:
            self.write(msg=f"[logger-close]: {inspect.stack()[1][1]} Exited With Code {exit_code}. Reason: {exit_reason}", lvl=Logger.INFO)
        else:
            self.write(msg=f"[logger-close]: {exit_process} Exited With Code {exit_code}. Reason: {exit_reason}", lvl=Logger.INFO)
        return
    
    def get_format(self, index: int = None) -> list|str:
        """
        Returns the format that was used in this instance

        Use no parameters to give a list of the format.

        Use an index, starting at 0, to get a specific item in the format list; returns a string. Index can be up to 2
        """
        if index is None:
            return self.format
        else:
            return str(self.format[index])

    def get_write_mode(self) -> str:
        """
        Return the current write mode
        """
        return self.write_mode

    def clear_log_file(self) -> None:
        """
        Clear the log file

        Takes no parameters
        """
        with open(self.log_file_path, "w") as logfile:
            logfile.write("")
            logfile.close()
        return
