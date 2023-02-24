"""
Button Module

This Module Is Used To Create Buttons And Switches

Swtiches Coming Soon
"""

# External Modules
import pygame

class toggleButton:

    def __init__(self, location: tuple, size: tuple, text: str = "Button", altText: str = None, textSize: int = 20, textFont:  str = None, textColor: str = "black", color: str = "white", toggleColor: str = "grey", hoverColor: str = "black", borderRadius: int | float = 5) -> None:
        """
        Creates A New toggleButton
        """

        self.surface = pygame.display.get_surface()
        self.location = location
        self.size = size
        self.color = color
        self.toggleColor = toggleColor
        self.hoverColor = hoverColor
        self.currentColor = color
        self.text = text
        self.toggleMode = False
        self.currentText = text

        if altText is None:
            self.toggleText = text
        else:
            self.toggleText = altText

        self.textObject = pygame.font.Font(textFont, textSize)
        self.textColor = textColor

        self.borderRadius = borderRadius

    def displayButton(self) -> None:
        """
        Displays The Button On The Current Surface
        """

        
        button = pygame.Rect((self.location[0], self.location[1], self.size[0], self.size[1]))
        pygame.draw.rect(self.surface, self.currentColor, button, 0, self.borderRadius)
        self.surface.blit(self.textObject.render(self.text, True, self.textColor), (self.location[0] + self.size[0] / 2 - self.textObject.size(self.text)[0] / 2, self.location[1] + self.size[1] / 2 - self.textObject.get_height() / 2))

        # When The Mouse Goes Over The Button, Make It Change Color
        if pygame.mouse.get_pos()[0] > self.location[0] and pygame.mouse.get_pos()[0] < self.location[0] + self.size[0] and pygame.mouse.get_pos()[1] > self.location[1] and pygame.mouse.get_pos()[1] < self.location[1] + self.size[1]:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.toggle()


    def toggle(self) -> None:
        """
        Toggles The Toggle Mode Of The Button
        """

        if self.toggleMode == False:
            self.toggleMode = True
            self.currentColor = self.toggleColor
            self.currentText = self.toggleText
        else:
            self.toggleMode = False
            self.currentColor = self.color
            self.currentText = self.text

    def getToggleMode(self) -> bool:
        """
        Returns The Current Toggle Mode Of The Button
        """

        return self.toggleMode

    def setPos(self, newLocation: tuple) -> None:
        self.location = newLocation
        return

class button:

    def __init__(self, command: str, location: tuple, size: tuple, text: str = "Button", textSize: int = 20, textFont:  str = None, textColor: str = "black", color: str = "white", hoverColor: str = "grey", pressColor = "black", borderRadius: int = 5) -> None:
        """
        Creates A New Button
        """

        self.surface = pygame.display.get_surface()
        self.location = location
        self.size = size

        self.color = color
        self.hoverColor = hoverColor
        self.currentColor = color
        self.pressColor = pressColor

        self.text = text
        self.command = command

        self.textObject = pygame.font.Font(textFont, textSize)
        self.textColor = textColor
        self.pressMode = False

        self.borderRadius = borderRadius

    def displayButton(self) -> None:
        """
        Displays The Button On The Current Surface
        """

        button = pygame.Rect((self.location[0], self.location[1], self.size[0], self.size[1]))
        pygame.draw.rect(self.surface, self.currentColor, button, 0, self.borderRadius)
        self.surface.blit(self.textObject.render(self.text, True, self.textColor), (self.location[0] + self.size[0] / 2 - self.textObject.size(self.text)[0] / 2, self.location[1] + self.size[1] / 2 - self.textObject.get_height() / 2))

        # When The Mouse Goes Over The Button, Make It Change Color
        if pygame.mouse.get_pos()[0] > self.location[0] and pygame.mouse.get_pos()[0] < self.location[0] + self.size[0] and pygame.mouse.get_pos()[1] > self.location[1] and pygame.mouse.get_pos()[1] < self.location[1] + self.size[1]:
            self.currentColor = self.hoverColor
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pressed = True
                    self.currentColor = self.pressColor
                    if self.command is not None:
                        eval(self.command + "()")
                    self.pressMode = True
                else:
                    self.pressMode = False
        else:
            self.currentColor = self.color
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def getPressMode(self) -> bool:
        """
        Returns The Current Press Mode Of The Button
        """

        return self.pressMode
                    

class toggleSwitch:
    """
    Creates A New Toggle Switch
    """

    def __init__(self):
        print(self)