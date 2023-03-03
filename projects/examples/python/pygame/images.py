"""
How To Display Images In Pygame.
"""

# Built-In Modules
import os
import sys
# External Modules
import pygame

# -----=====[Pygame Init]=====----- #
pygame.display.init()
pygame.font.init()

# -----=====[Pygame Setup]=====----- #
screen = pygame.display.set_mode((600, 200), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Images")

# -----=====[Pygame Images]=====----- #
doc_folder = os.path.dirname(__file__).replace("pygame", "").replace("python/", "").replace("examples/", "").replace("projects", "docs")
# The Path To The Docs Folder
# This Is Used To Get The Path To The Docs Folder So We Can Load The Images From There

image_object1 = pygame.image.load(os.path.join(doc_folder, "images", "Phox.jpg"))

# -----=====[Pygame Fonts]=====----- #
font = pygame.font.Font(None, 25)

def main():
    while True:
        # Side Note: Have To Use image_object2 Because If They Are The Same Object It Complains That It Can't Change As It Doesn't Have A Value. Which Is Weird Because It Does Have A Value.
        image_object2 = pygame.transform.scale(image_object1, (screen.get_width(), screen.get_height())) # Scale The Image To The Size Of The Screen
        screen.blit(image_object2, (screen.get_width() / 2 - image_object2.get_width() / 2, screen.get_height() / 2 - image_object2.get_height() / 2)) # Center The Image On The Screen

        # -----=====[Pygame Text]=====----- #
        screen.blit(font.render("There's An Image!", True, (255, 255, 255), (0, 0, 0)), (10, 10))

        # -----=====[Pygame Events]=====----- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    main()