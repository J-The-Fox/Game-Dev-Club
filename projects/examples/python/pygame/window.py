"""
How To Create A Window In Python Using pygame
"""

# Built-In Modules
import sys
# Downloaded Modules
import pygame

pygame.init() 
# You Must Run The init Function Before You Start Using Pygame.
# You Can Use The Specific init Functions For pygame Too.
# Examples Are pygame.mixer.init(), pygame.font.init() and pygame.display.init() 
# For pygames's audio, font And display Modules Respectivly .
# The pygame.mixer module has .pre_init() As Well. It Holds Audio Info You
# Can Use To Tune And Tweak How The Module Runs

def new_window(window_size: tuple, window_caption: str = "New Window!", tick_speed: int = 60, text: str = "This Is A Window With Text!"):
    window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
    # variable_name = pygame.display.set_mode((size), flags) Is How You Start Your Screen.
    # This Creates A Surface You Can Use To Display Things On Later, More On That Later.
    # But You Need To Run This First.
    #
    # As A Side Note For How The Location Works On pygame.
    # The Top Left Corner Is (0, 0) And Increases From There

    clock = pygame.time.Clock()
    # Create A New Clock
    # The Clock Is Useful For Setting Framerates On Your Window
    # The clock.tick(framerate) Can Be Used To Set It
    # Make Sure To Put It In The While Loop!

    pygame.display.set_caption(window_caption)
    # This Sets The Title / Caption Of Your Display
    # If You Want It To Update, You Can Place It In The Loop.
    # However, If You Don't Need That, You Can Put It Outside Of The Loop

    new_font = pygame.font.Font(None, 25)
    # This Creates A New Font Object With The Default System Font(Because Of The 'None') With A Size Of 25

    while True: # To Make Your Screen Work, You Need To Put It In A While Loop Of Some Kind

        window.fill((252, 145, 0)) # This Fills The Screen With A Certian Color Using RGB Values

        window.blit(new_font.render(text, True, (255, 255, 255), (0, 0, 0)), (10, 10))
        # This Uses The .blit Method To Render The Font On To The Screen.
        # Inside The .blit, There Is The new_font.render From The Font Created Earlier.
        # This Allow You To Set Text, Antialiasing, Font Color And Background Color Respectivly
        # Inside The .blit At The End Is The Location Of The Font.

        for event in pygame.event.get(): # This Runs Through All The Events pygame Has

            if event.type == pygame.QUIT: # The Type Is QUIT (Which Is When The X-Button On The Window Is Hit), Quit pygame And Exit The Program
                pygame.quit() # Quit pygame
                sys.exit() # Exit The Program
        
        clock.tick(tick_speed) # Sets The Framerate Of The Game, Whihc In This Case, Defaults To 60.
        pygame.display.update() # This Update The Entire Display, If You Don't Have This, You Won't Be Able To Update The Display And Nothing Will Happen


if __name__ == "__main__":
    new_window((400, 200))