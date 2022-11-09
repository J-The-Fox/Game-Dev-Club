import time, inspect, colorama, datetime
from functools import wraps

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
    """Times How Long A Function Takes To Complete"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        startTime = time.perf_counter()

        func(*args, **kwargs)

        endTime = time.perf_counter()

        totalTime = round(endTime - startTime, 5)

        print(f"{str(datetime.datetime.now())} - [{colorama.Fore.BLUE}DEBUG{colorama.Fore.RESET}] - The {colorama.Fore.WHITE}{str(func)}{colorama.Fore.RESET} Took {colorama.Fore.WHITE}{totalTime}{colorama.Fore.RESET} Seconds To Complete.".replace("<", "").replace(">", "").replace("function", "Function").replace("at", "At"))
    
    return wrapper # Return The Wrapper