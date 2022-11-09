import sys, os, platform, datetime, colorama, configparser, time, psutil, pygame

from modules.python.lib import *
from modules.python.decorators import *

class Main():
    """The Main Game Function"""

    FULLSCREENSIZE = pygame.display.get_window_size()


    def __init__(self):

        self.platform = platform.platform()

        
        self.full
        self.screen = pygame.display.set_mode("")