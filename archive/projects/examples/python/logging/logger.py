"""
Helps With Logging By Writing To A File And / Or The Terminal

Note: This Module Will Use Colorama To Color The Text In The Terminal.  
If It Is Not Installed, Color Will Not Be Used.

Version: 0.1.8-dev4
"""

# Built-In Modules
import datetime
import os
import inspect

_IMPORTERROR = []

# External Modules
try:
    import colorama
except ImportError:
    _IMPORTERROR.append("colorama")

# Logger Class
class Logger():
    """
    Logging Class

    Log Modes:

    There are 4 different log modes
    - 0 or LOGDISABLED (No Logging)
    - 1 or LOGTOTERM (Log To Terminal Only)
    - 2 or LOGTOFILE (Log To File Only)
    - 3 or LOGTOTERMANDFILE (Log To Terminal And File)

    These are set when you first call it.
    EX: Logger = logger.Logger(logger.Logger.LOGTOTERM)

    Note: The default path for the logfile is in the same directory as logger.py and called 'main.log'.
    To change the log file name, pass in log_file = 'log_file_name.extension' to change the name / extension
    To change the log file location, pass in log_file_path = 'location/of/logfile' to change the location

    Write Mode:

    2 Write Modes are able to be used when logging to a file.
    - a or append (Append)
    - w or overwrite (Overwrite)

    Format:

    The format is in a list with 3 possible values being: dt, msg, and lvl. 
    - dt (Date + Time)
    - lvl (Log Level)
    - msg (Message)

    A format like ['dt', 'lvl', 'msg'] would be displayed as: '+ 2023-01-20 10:49:26.358819 - [INFO] - Message Passed Through'  
    Note: A Time and Date Format Is In The Works, But Is Not Ready Yet.

    Log Levels:

    There are 8 possible log levels
    - ART (Used Mainly For ASCII Art)
    - BUG (Rarely Used, Only Used For Bugs That Are Known But Not Fixed)
    - DEBUG (Used For Debugging Information)
    - INFO (Basic Information)
    - NOTICE (Something Important Happened But It Is Not An Error)
    - WARN / WARNING (Something Went Wrong And Might Need To Be Looked At, Usually Used For A Minor Error)
    - ERROR (Something Went Wrong, But The Program Can Recover)
    - CRITICAL (Something Went Wrong, And The Program Can Not Recover)

    When using NOTICE, WARN, WARNING, ERROR, or CRITICAL, the extra_msg argument can be passed in to provide more information.
    If used when on ART, BUG, INFO or DEBUG, the extra_msg argument will be ignored.

    EX: + 2023-01-20 10:54:02.692807 - [ERROR] - Could Not Find File.
        ╰─> Could Not Find File 'main.py'.
    """

    # Log Level
    ART = "ART" # Used Mainly For ASCII Art
    BUG = "BUG" # Rarely Used, Only Used For Bugs That Are Known But Not Fixed
    DEBUG = "DEBUG" # Used For Debugging Information
    INFO = "INFO" # Basic Information
    NOTICE = "NOTICE" # Something Important Happened But It Is Not An Error
    WARN = "WARN" # Alias For WARNING, Mean The Same Thing
    WARNING = "WARNING" # Alias For WARN, Mean The Same Thing
    ERROR = "ERROR" # Something Went Wrong, But The Program Can Recover
    CRITICAL = "CRITICAL" # Something Went Wrong, And The Program Can Not Recover

    # Log Mode
    LOGDISABLED = 0
    LOGTOTERM = 1
    LOGTOFILE = 2
    LOGTOTERMANDFILE = 3

    # Write Mode
    APPEND = "a" 
    OVERWRITE = "w" # Default

    # Version
    VERSION = "0.1.8-dev4"

    def __init__(self, mode: int, write_mode: str = "w", format: list = ["dt", "lvl", "msg"], log_file: str = "main.log", log_file_path: str = None, maxSize: int = 100000, levelsShown = [BUG, DEBUG, INFO, NOTICE, WARN, ERROR, CRITICAL], use_color: bool = True) -> None:
        # Check If The log_file_path Is None, If It Is, Set It To The Current Directory
        if log_file_path is None:
            self.log_file_path = os.path.join(os.path.dirname(__file__), log_file)
        else:
            self.log_file_path = os.path.join(log_file_path, log_file)
        self.log_file = log_file
        self.maxSize = maxSize

        self.mode = mode
        self.write_mode = write_mode
        self.format = format

        self.levelsShown = levelsShown

        # Check If The colorama Module Is Installed
        if 'colorama' not in _IMPORTERROR:
            self.use_color = use_color
        else:
            self.use_color = False

    def init(self, log_text=False) -> None:
        """
        Initilize The Logger

        Arguments:
            log_text (bool): If True, Will Log The Initilization Text. Defaults To False.
        """

        # If the user has selected one of two log to file modes, either clear the file or append to the existing file
        if self.write_mode == "w":
            with open(self.log_file_path, self.write_mode) as logfile:
                logfile.write("")
                logfile.close()
        elif self.write_mode == "a":
            with open(self.log_file_path, self.write_mode) as logfile:
                logfile.write("\n")
                logfile.close()

        # If The User Has Selected To Log To The Terminal, Log The Initilization Text And Configuration Information
        if log_text:
            if os.path.getsize(self.log_file_path) > self.maxSize:
                with open(self.log_file_path, "w") as f:
                    f.write("")
                    f.close()
                self.write("The Log File Is Greater Than The Maximum Size Allowed, Overwriting The Log File", self.WARN)
            self.write("Logger Version: " + self.VERSION, self.INFO)

            self.write("====================================[ Logging Config ]====================================", self.INFO)
            self.write(f"Log Mode: {self.mode}", self.INFO)
            self.write(f"Write Mode: {self.write_mode}", self.INFO)
            self.write(f"Format: {self.format}", self.INFO)
            self.write(f"Log File: {self.log_file}", self.INFO)
            self.write(f"Log File Path: {self.log_file_path}", self.INFO)
            self.write(f"Levels Shown: {self.levelsShown}", self.INFO)
            self.write(f"Use Color: {self.use_color}", self.INFO)
            self.write("==========================================================================================", self.INFO)

        # If the user is only writting to the terminal, no need to create a new log file, just skip creating / clearing on the init
        # if self.mode == 2:
        return

    def write(self, msg: str, lvl: str, extra_msg: str = None) -> None:
        """
        Writes a log to the terminal, a file or both using the format provided

        Uses color if the colorama module is installed

        Arguments:
            msg (str): The Message To Be Logged  
            lvl (str): The level of the log  
        Optional Arguments:
            extra_msg (str): Extra Information To Be Logged. Defaults To None.
        """

        output_string = ""
        # Use The Formatting Provided In The init Function and Create The Log String
        format_list = self.__parse_format__(msg, lvl)

        # If The Level Provided Is Not In The Levels Shown List, Return
        if "ART" in str(format_list) and "ART" not in self.levelsShown:
            return
        if "BUG" in str(format_list) and "BUG" not in self.levelsShown:
            return
        if "DEBUG" in str(format_list) and "DEBUG" not in self.levelsShown:
            return
        if "INFO" in str(format_list) and "INFO" not in self.levelsShown:
            return
        if "NOTICE" in str(format_list) and "NOTICE" not in self.levelsShown:
            return
        if "WARN" in str(format_list) and "WARN" not in self.levelsShown or "WARNING" in format_list and "WARNING" not in self.levelsShown:
            return
        if "ERROR" in str(format_list) and "ERROR" not in self.levelsShown:
            return
        if "CRITICAL" in str(format_list) and "CRITICAL" not in self.levelsShown:
            return

        # If The Mode Is 1, Write To The Terminal
        if self.mode == 1:
            print(output_string.join(format_list))
            if extra_msg is not None and lvl == "NOTICE" or extra_msg is not None and lvl == "WARN" or extra_msg is not None and lvl == "WARNING" or extra_msg is not None and lvl == "ERROR" or extra_msg is not None and lvl == "CRITICAL":
                print(f"╰─> {extra_msg}")

        # If The Mode Is 2, Write To The Log File
        if self.mode == 2:
            with open(self.log_file_path, "a") as logfile:
                if self.use_color is True:
                    logfile.write(output_string.join(format_list).replace(colorama.Fore.WHITE, "").replace(colorama.Fore.BLUE, "").replace(colorama.Fore.CYAN, "").replace(colorama.Fore.LIGHTYELLOW_EX, "").replace(colorama.Fore.LIGHTRED_EX, "").replace("[39m", "") + "\n")
                else:
                    logfile.write(output_string.join(format_list) + "\n")
                if extra_msg is not None and lvl == "NOTICE" or extra_msg is not None and lvl == "WARN" or extra_msg is not None and lvl == "WARNING" or extra_msg is not None and lvl == "ERROR" or extra_msg is not None and lvl == "CRITICAL":
                    logfile.write(f"╰─> {extra_msg}\n")

        # If The Mode Is 3, Write To The File And The Terminal
        if self.mode == 3:
            with open(self.log_file_path, "a") as logfile:
                if self.use_color is True:
                    logfile.write(output_string.join(format_list).replace(colorama.Fore.WHITE, "").replace(colorama.Fore.BLUE, "").replace(colorama.Fore.CYAN, "").replace(colorama.Fore.LIGHTYELLOW_EX, "").replace(colorama.Fore.LIGHTRED_EX, "").replace("[39m", "") + "\n")
                else:
                    logfile.write(output_string.join(format_list) + "\n")
                print(output_string.join(format_list))
                if extra_msg is not None and lvl == "NOTICE" or extra_msg is not None and lvl == "WARN" or extra_msg is not None and lvl == "WARNING" or extra_msg is not None and lvl == "ERROR" or extra_msg is not None and lvl == "CRITICAL":
                    logfile.write(f"╰─> {extra_msg}\n")
                    print(f"╰─> {extra_msg}")
        return

    def close(self, exit_code: int, exit_process: str = None, exit_reason: str = None) -> None:
        """
        Close The Logger And Write The Exit Message To The Log File.

        Arguments:
            exit_code (int | str): The Exit Code Of The Process.  
        Optional Arguments:
            exit_reason (str): The Reason For The Process To Exit. Defaults To None.
            exit_process (str): The Process That Exited. Defaults To The Current Process Using inspect.stack(). Defaults To None.
        """

        if exit_reason is None and exit_process is None:
            self.write(msg=f"[logger-close]: {inspect.stack()[1][1]} Exited With Code {exit_code}.", lvl=Logger.INFO)
        elif exit_reason is None:
            self.write(msg=f"[logger-close]: {exit_process} Exited With Code {exit_code}.", lvl=Logger.INFO)
        elif exit_process is None:
            self.write(msg=f"[logger-close]: {inspect.stack()[1][1]} Exited With Code {exit_code}. Reason: {exit_reason}", lvl=Logger.INFO)
        else:
            self.write(msg=f"[logger-close]: {exit_process} Exited With Code {exit_code}. Reason: {exit_reason}", lvl=Logger.INFO)
        return
    
    def get_format(self) -> str:
        """
        Returns The Format List Used To Format The Log Message

        Takes No Arguments
        """

        return self.format

    def get_write_mode(self) -> str:
        """
        Return The Write Mode

        Takes No Arguments
        """

        return self.write_mode

    def clear_log_file(self) -> None:
        """
        Clears The Log File

        Takes No Arguments
        """

        with open(self.log_file_path, "w") as logfile:
            logfile.write("")
            logfile.close()
        return

    def get_log_file_path(self) -> str:
        """
        Returns The Log File Path

        Takes No Arguments
        """

        return self.log_file_path
    
    def get_log_file_name(self) -> str:
        """
        Returns The Log File Name

        Takes No Arguments
        """

        return self.log_file
    
    # Private Functions
    def __parse_format__(self, msg, lvl) -> list:
        format_list = ["+ "]

        # Use The Formatting Provided In The init Function and Create The Log
        index = 0
        for format_data in self.format: # Loop Through The Format List
            if str(format_data).capitalize() == "Dt":
                format_list.append(str(datetime.datetime.now())) # Add The Current Date And Time
            if str(format_data).capitalize() == "Msg":
                format_list.append(msg) # Add The Message
            if str(format_data).capitalize() == "Lvl" and self.use_color is True:
                if lvl == "ART": # If The Level Is ART, Make It Grey:
                    format_list.append(f"[{colorama.Fore.LIGHTBLACK_EX}{lvl}{colorama.Fore.RESET}]")
                if lvl == "BUG": # If The Level Is BUG, Make It Green
                    format_list.append(f"[{colorama.Fore.LIGHTGREEN_EX}{lvl}{colorama.Fore.RESET}]")
                elif lvl == "DEBUG": # If The Level Is DEBUG, Make It Blue
                    format_list.append(f"[{colorama.Fore.BLUE}{lvl}{colorama.Fore.RESET}]")
                elif lvl == "INFO": # If The Level Is INFO, Make It Cyan
                    format_list.append(f"[{colorama.Fore.CYAN}{lvl}{colorama.Fore.RESET}]")
                elif lvl == "NOTICE": # If The Level Is NOTICE, Make It Magenta
                    format_list.append(f"[{colorama.Fore.LIGHTMAGENTA_EX}{lvl}{colorama.Fore.RESET}]")
                elif "WARN" in lvl: # If The Level Is WARN or WARNING, Make It Yellow
                    format_list.append(f"[{colorama.Fore.LIGHTYELLOW_EX}{lvl}{colorama.Fore.RESET}]")
                elif lvl == "ERROR" or lvl == "CRITICAL": # If The Level Is ERROR or CRITICAL, Make It Red
                    format_list.append(f"[{colorama.Fore.LIGHTRED_EX}{lvl}{colorama.Fore.RESET}]")
            elif str(format_data).capitalize() == "Lvl":
                format_list.append(f"[{lvl}]") # Add The Level
            index += 1
            if index < 2:
                format_list.append(" - ")
            if index == 2:
                format_list.append(": ")
        return format_list