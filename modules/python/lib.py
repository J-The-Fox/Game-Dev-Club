import pygame, os, time, socket, subprocess, datetime, colorama
from cryptography.fernet import Fernet
from decorators import memorize

pygame.init()

#[--------------[Create Debug Text Parser]--------------]#

class Debug():

    def __init__(self, font: pygame.font.Font):

        self.font = font

    def createDebugText(self, msg: str or list, textColor: str, backgroundColor: str, posX: int = 10, posY: int = 10, textSpacingDistanceY: int = 20) -> None:
        """Create Debug Text For Displaying Values On The Screen"""

        if isinstance(msg, str):
            displaySurfuce = pygame.display.get_surface()
            debugSurf = self.font.render(str(msg), True, textColor)
            debugRect = debugSurf.get_rect(topleft = (posX, posY))
            pygame.draw.rect(displaySurfuce, backgroundColor, debugRect)
            displaySurfuce.blit(debugSurf, debugRect)

        elif isinstance(msg, list):
            count = posY - posY
            for text in msg:
                displaySurfuce = pygame.display.get_surface()
                debugSurf = self.font.render(str(text), True, textColor)
                debugRect = debugSurf.get_rect(topleft = (posX, posY + count))
                pygame.draw.rect(displaySurfuce, backgroundColor, debugRect)
                displaySurfuce.blit(debugSurf, debugRect)

                count += textSpacingDistanceY

    def displayLog(self, surface: pygame.Surface, enabled: bool, pos: tuple or str, logFile: str, textBoxSizeX: int, textBoxSizeY: int):
        _textLogList = []
        
        try:
            with open(logFile, 'r') as logFileHandler:
                for _line in logFileHandler:
                    _textLogList.append(_line)
                logFileHandler.close()
    
        except FileNotFoundError:
            print(f"x {str(datetime.datetime.now())} - [{colorama.Fore.RED}ERROR{colorama.Fore.RESET}] - The Log File Doesn't Exist")
            print(f"╰─> The File {logFile} Does Not Exist.")
            return


        _logSurface = pygame.Surface((textBoxSizeX, textBoxSizeY)).convert_alpha()
        _logSurface.fill((10, 10, 10, 100))

        if enabled != True:
            return
        
        if str(pos).capitalize() not in ["Topleft", "Topright", "Bottomleft", "Bottomright"] and isinstance(pos, tuple) == False:
            return
        
        lineNum = 0
        if isinstance(pos, tuple) == True:
            surface.blit(_logSurface, (pos[0] - textBoxSizeX / 2, pos[1] - textBoxSizeY / 2))
        elif str(pos).capitalize() == "Topright":
            surface.blit(_logSurface, (pygame.display.get_window_size()[0] - textBoxSizeX, 0))
            for _text in reversed(_textLogList[:]):
                surface.blit(self.font.render(str(_text).replace("\n", ""), True, "Orange"), (pygame.display.get_window_size()[0] - _logSurface.get_width() + 10, _logSurface.get_height() - 20 - lineNum))
                lineNum += self.font.get_height()
        elif str(pos).capitalize() == "Bottomright":
            surface.blit(_logSurface, (pygame.display.get_window_size()[0] - textBoxSizeX, pygame.display.get_window_size()[1] - textBoxSizeY))
        elif str(pos).capitalize() == "Topleft":
            surface.blit(_logSurface, (0, 0))
        elif str(pos).capitalize() == "Bottomleft":
            surface.blit(_logSurface, (0, pygame.display.get_window_size()[1] - textBoxSizeY))
        else:
            return
        


        # Output The Text To The Terminal


        return

def parseKeysPressed(keysPressed: pygame.key.ScancodeWrapper) -> list:
    """Parse The ScancodeWrapper And Output A List That Contains All The Current Keys Being Pressed"""

    allKeysPressed = []

    # Shift Keys
    if keysPressed[pygame.K_LSHIFT]:
        allKeysPressed.append("LShift")
    if keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("RShift")

    # Numbers + Shift Varaients
    if keysPressed[pygame.K_0] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_0] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append(")")
    elif keysPressed[pygame.K_0]:
        allKeysPressed.append("0")
    if keysPressed[pygame.K_1] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_1] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("!")
    elif keysPressed[pygame.K_1]:
        allKeysPressed.append("1")
    if keysPressed[pygame.K_2] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_2] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("@")
    elif keysPressed[pygame.K_2]:
        allKeysPressed.append("2")
    if keysPressed[pygame.K_3] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_3] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("#")
    elif keysPressed[pygame.K_3]:
        allKeysPressed.append("3")
    if keysPressed[pygame.K_4] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_4] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("$")
    elif keysPressed[pygame.K_4]:
        allKeysPressed.append("4")
    if keysPressed[pygame.K_5] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_5] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("%")
    elif keysPressed[pygame.K_5]:
        allKeysPressed.append("5")
    if keysPressed[pygame.K_6] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_6] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("^")
    elif keysPressed[pygame.K_6]:
        allKeysPressed.append("6")
    if keysPressed[pygame.K_7] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_7] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("&")
    elif keysPressed[pygame.K_7]:
        allKeysPressed.append("7")
    if keysPressed[pygame.K_8] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_8] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("*")
    elif keysPressed[pygame.K_8]:
        allKeysPressed.append("8")
    if keysPressed[pygame.K_9] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_9] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("(")
    elif keysPressed[pygame.K_9]:
        allKeysPressed.append("9")
    
    # Letters <- Not Adding Capital Letters. Too Much Work For That ATM - J-The-Fox
    if keysPressed[pygame.K_a]:
        allKeysPressed.append("a")
    if keysPressed[pygame.K_b]:
        allKeysPressed.append("b")
    if keysPressed[pygame.K_c]:
        allKeysPressed.append("c")
    if keysPressed[pygame.K_d]:
        allKeysPressed.append("d")
    if keysPressed[pygame.K_e]:
        allKeysPressed.append("e")
    if keysPressed[pygame.K_f]:
        allKeysPressed.append("f")
    if keysPressed[pygame.K_g]:
        allKeysPressed.append("g")
    if keysPressed[pygame.K_h]:
        allKeysPressed.append("h")
    if keysPressed[pygame.K_i]:
        allKeysPressed.append("i")
    if keysPressed[pygame.K_j]:
        allKeysPressed.append("j")
    if keysPressed[pygame.K_k]:
        allKeysPressed.append("k")
    if keysPressed[pygame.K_l]:
        allKeysPressed.append("l")
    if keysPressed[pygame.K_m]:
        allKeysPressed.append("m")
    if keysPressed[pygame.K_n]:
        allKeysPressed.append("n")
    if keysPressed[pygame.K_o]:
        allKeysPressed.append("o")
    if keysPressed[pygame.K_p]:
        allKeysPressed.append("p")
    if keysPressed[pygame.K_q]:
        allKeysPressed.append("q")
    if keysPressed[pygame.K_r]:
        allKeysPressed.append("r")
    if keysPressed[pygame.K_s]:
        allKeysPressed.append("s")
    if keysPressed[pygame.K_t]:
        allKeysPressed.append("t")
    if keysPressed[pygame.K_u]:
        allKeysPressed.append("u")
    if keysPressed[pygame.K_v]:
        allKeysPressed.append("v")
    if keysPressed[pygame.K_w]:
        allKeysPressed.append("w")
    if keysPressed[pygame.K_x]:
        allKeysPressed.append("x")
    if keysPressed[pygame.K_y]:
        allKeysPressed.append("y")
    if keysPressed[pygame.K_z]:
        allKeysPressed.append("z")

    # Action Keys
    if keysPressed[pygame.K_SPACE]:
        allKeysPressed.append("Space")
    if keysPressed[pygame.K_LEFT]:
        allKeysPressed.append("Left")
    if keysPressed[pygame.K_UP]:
        allKeysPressed.append("Up")
    if keysPressed[pygame.K_DOWN]:
        allKeysPressed.append("Down")
    if keysPressed[pygame.K_RIGHT]:
        allKeysPressed.append("Right")
    if keysPressed[pygame.K_BACKSPACE]:
        allKeysPressed.append("Backspace")
    if keysPressed[pygame.K_RETURN]:
        allKeysPressed.append("Return")
    if keysPressed[pygame.K_TAB]:
        allKeysPressed.append("Tab")
    if keysPressed[pygame.K_ESCAPE]:
        allKeysPressed.append("Escape")
    if keysPressed[pygame.K_LCTRL]:
        allKeysPressed.append("LCtrl")
    if keysPressed[pygame.K_RCTRL]:
        allKeysPressed.append("RCtrl")

    # Function Keys
    if keysPressed[pygame.K_F1]:
        allKeysPressed.append("Func1")
    if keysPressed[pygame.K_F2]:
        allKeysPressed.append("Func2")
    if keysPressed[pygame.K_F3]:
        allKeysPressed.append("Func3")
    if keysPressed[pygame.K_F4]:
        allKeysPressed.append("Func4")
    if keysPressed[pygame.K_F5]:
        allKeysPressed.append("Func5")
    if keysPressed[pygame.K_F6]:
        allKeysPressed.append("Func6")
    if keysPressed[pygame.K_F7]:
        allKeysPressed.append("Func7")
    if keysPressed[pygame.K_F8]:
        allKeysPressed.append("Func8")
    if keysPressed[pygame.K_F9]:
        allKeysPressed.append("Func9")
    if keysPressed[pygame.K_F10]:
        allKeysPressed.append("Func10")
    if keysPressed[pygame.K_F11]:
        allKeysPressed.append("Func11")
    if keysPressed[pygame.K_F12]:
        allKeysPressed.append("Func12")
        
    # Symbols + Shift Varaients
    if keysPressed[pygame.K_BACKSLASH] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_BACKSLASH] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("|")
    elif keysPressed[pygame.K_BACKSLASH]:
        allKeysPressed.append("\\")
    if keysPressed[pygame.K_SLASH] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_SLASH] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("?")
    elif keysPressed[pygame.K_SLASH]:
        allKeysPressed.append("/")
    if keysPressed[pygame.K_MINUS] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_MINUS] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("_")
    elif keysPressed[pygame.K_MINUS]:
        allKeysPressed.append("-")
    if keysPressed[pygame.K_EQUALS] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_EQUALS] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("+")
    elif keysPressed[pygame.K_EQUALS]:
        allKeysPressed.append("=")
    if keysPressed[pygame.K_SEMICOLON] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_SEMICOLON] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append(":")
    elif keysPressed[pygame.K_SEMICOLON]:
        allKeysPressed.append(":")
    if keysPressed[pygame.K_COMMA] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_COMMA] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("<")
    elif keysPressed[pygame.K_COMMA]:
        allKeysPressed.append(",")
    if keysPressed[pygame.K_PERIOD] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_PERIOD] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append(">")
    elif keysPressed[pygame.K_PERIOD]:
        allKeysPressed.append(".")
    if keysPressed[pygame.K_BACKQUOTE] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_BACKQUOTE] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("~")
    elif keysPressed[pygame.K_BACKQUOTE]:
        allKeysPressed.append(" ` ")
    if keysPressed[pygame.K_QUOTE] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_QUOTE] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append(' " ')
    elif keysPressed[pygame.K_QUOTE]:
        allKeysPressed.append(" ' ")
    if keysPressed[pygame.K_RIGHTBRACKET] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_RIGHTBRACKET] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("}")
    elif keysPressed[pygame.K_RIGHTBRACKET]:
        allKeysPressed.append("]")
    if keysPressed[pygame.K_LEFTBRACKET] and keysPressed[pygame.K_LSHIFT] or keysPressed[pygame.K_LEFTBRACKET] and keysPressed[pygame.K_RSHIFT]:
        allKeysPressed.append("{")
    elif keysPressed[pygame.K_LEFTBRACKET]:
        allKeysPressed.append("[")
    
    return allKeysPressed

#[--------------[Create Connection Class]--------------]#
class Connection():
    """Anything That Deals With The Internets"""

    def __init__(self, timeout: int):
        self.timeout = timeout

    def getOnlineStatus(self, host = "8.8.8.8", port = 53) -> bool:
        """Returns True If A Connection Is Active Or Returns False If The Connection Is Inactive"""

        try:
            socket.setdefaulttimeout(self.timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error:
            return False
        
    def checkGithubConnection(self) -> bool:

        if self.getOnlineStatus() == False:
            return False
        
        subprocess.run(["ping", "-c", "5", "github.com"])
        socket.setdefaulttimeout(self.timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("github.com", 53))


#]-----------------[Set Up The Level Class]-----------------[#
class Level():
    def __init__(self):

        self.displaySurface = pygame.display.get_surface()

        # Set Up Sprite Groups
        self.visbaleSprites = pygame.sprite.Group() # Creates A Sprite Group For visableSrpites. Sprites That Will Be Drawn On Screen
        self.coliderSprites = pygame.sprite.Group() # Creates A Sprite Group For coliderSprites. Sprites That Act As Borders / Collision

    def update(self):
        pass

#]-----------------[Set Up The Sprite Class]-----------------[#
class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos :tuple, imagePath :str, spriteGroup :str):
        super().__init__(spriteGroup)
        self.image = pygame.image.load(os.path.join(os.getcwd(), imagePath)).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

class Button():
    """Create A Button"""

    def __init__(self, buttonMessege: str,  pos: tuple, elevation: int, buttonColor, buttonShadowColor, buttonHoverColor, textColor: str = "#FFFFFF", textSize: int = 15, textFont: str = "rockwell", width: int = 100, height: int = 50, offsetX: int = 20, offsetY: int = 20):
        #self.image = pygame.transform.scale(image, (int(width), int(height)))
        #self.rect = self.image.get_rect()
        self.elevation = elevation
        self.original_y_pos = pos[1]
        self.color = buttonColor
        self.color_shadow = buttonShadowColor
        self.hover = buttonHoverColor
        self.clicked = False
        self.top_rect = pygame.Rect(pos,(width,height))
        self.top_color = buttonColor
        self.bottom_rect = pygame.Rect(pos,(width,height))
        self.bottom_color = buttonShadowColor
        font = pygame.font.SysFont(textFont, textSize)
        self.text_surf = font.render(buttonMessege, True, textColor)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        self.offsetX = offsetX
        self.offsetY = offsetY

    def draw_button(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        top_rect = self.top_rect.copy()
        bottom_rect = self.bottom_rect.copy()
        bottom_rect.x += self.offsetX
        bottom_rect.y += self.offsetY
        if top_rect.collidepoint(pos):
            self.top_color = self.color

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = True

            if pygame.mouse.get_pressed()[0]:
                bottom_rect.inflate_ip(self.elevation, self.elevation)
                top_rect.inflate_ip(self.elevation, self.elevation)

            if pygame.mouse.get_pressed()[0] and self.clicked == True:
                self.clicked = False
                action = True

            self.top_color = self.hover
        else:
            self.top_color = self.color

        bottom_surf = pygame.Surface(bottom_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(bottom_surf, self.bottom_color, (0, 0, * bottom_rect.size), border_radius = 12)
        screen.blit(bottom_surf, bottom_rect.topleft)

        top_surf = pygame.Surface(top_rect.size, pygame.SRCALPHA)
        pygame.draw.rect(top_surf, self.top_color, (0, 0, *top_rect.size), border_radius = 12)
        screen.blit(top_surf, top_rect.topleft)

        screen.blit(self.text_surf, self.text_rect)
        return action  

#]-----------------[Set Up The Logs Class]-----------------[#
class Popup():
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.transparancy = pygame.Surface((pygame.display.get_window_size())).convert_alpha()
    
    def drawMessageBox(self, color: str, pos: tuple, sizeX: int, sizeY: int, backgroundOpacity: int = 100, boxOpacity: int = 255):
        self.transparancy.fill((50, 50, 50, backgroundOpacity))
        _messageBoxRect = (pos[0], pos[1], sizeX, sizeY)
        pygame.display.get_window_size()
        self.surface.blit(self.transparancy, (0, 0))
        pygame.draw.rect(surface=self.surface, color=color, rect=_messageBoxRect, border_radius=10)
        return


#]-----------------[Set Up The Logs Class]-----------------[#
class Logs():
    def __init__(self, lookMode: str = "isContainedIn"):
        self.lookMode = lookMode


    def encyrptFile(self, declarers: list = ["None", "##@", "is"]):
        declarersNum = len(declarers)

        for root, dirs, files in os.walk(os.getcwd()):
            # Get The File Name
            for file in files:
                # Check If The File Ends In .conf, .py or .txt
                if file.endswith('.conf') or file.endswith('.py') or file.endswith('.txt') or file.endswith('.md') or file.endswith('.json'):
                    lineNum = 0
                    with open(os.path.join(root, file), 'r') as handler:
                        lines = handler.readlines()
                        for line in lines:
                            lineNum += 1
                            if self.lookMode == "isContainedIn":
                                for num in range(declarersNum):
                                    if declarers[num] in line:
                                        line = line.strip()
                                        print(f"x Found {declarers[num]} In File: {os.path.join(root, file)} On Line: {lineNum}\n╰─> {line}\n")
                            if self.lookMode == "isEqualTo":
                                for num in range(declarersNum):
                                    if declarers[num] in line.strip() == declarers[num]:
                                        line = line.strip()
                                        print(f"x Found {declarers[num]} In File: {os.path.join(root, file)} On Line: {lineNum}\n╰─> {line}\n")

                        handler.close()

    def createKey(self):
        key = Fernet.generate_key()
        keyFile = str(key) + ".key"
        with open(os.path.join(os.path.join(os.getcwd(), os.path.join("docs", os.path.join("entries", keyFile)))), 'wb') as keyHandler:
            keyHandler.write(key)
            keyHandler.close()

    def createPassword():
        print("")

    def encrypt(self):
        with open(os.path.join(os.path.join(os.getcwd(), os.path.join("docs", os.path.join("entries", "b'YYLBzKhiudnPQDBDjQ9LX3O0_xmj2FwMkfHWo_W2HUE='.key")))), 'rb') as filekey:
            key = filekey.read()
            filekey.close()

        fernet = Fernet(key)

        with open(os.path.join(os.path.join(os.getcwd(), os.path.join("docs", os.path.join("entries", "test.txt")))), 'rb') as file:
            original = file.read()
            file.close()

        encrypted = fernet.encrypt(original)

        with open(os.path.join(os.path.join(os.getcwd(), os.path.join("docs", os.path.join("entries", "test.txt")))), 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            encrypted_file.close()

    def decrypt(self, key):
        fernet = Fernet(key)

        with open(os.path.join(os.path.join(os.getcwd(), os.path.join("docs", os.path.join("entries", "test.txt")))), 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
            encrypted_file.close()

        decrypted = fernet.decrypt(encrypted)

        with open(os.path.join(os.path.join(os.getcwd(), os.path.join("docs", os.path.join("entries", "test.txt")))), 'wb') as dec_file:
            dec_file.write(decrypted)
            dec_file.close()

if __name__ == "__main__":
    Logs(lookMode="isContainedIn").encyrptFile(declarers=["ht"])
    #Logs().encrypt()
    #Logs().decrypt(key = "YYLBzKhiudnPQDBDjQ9LX3O0_xmj2FwMkfHWo_W2HUE=")
