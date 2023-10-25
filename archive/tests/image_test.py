# Built-In Modules
import os
# External Modules
import pygame

pygame.init()

image1path = os.path.join(os.path.dirname(__file__).replace("tests", "docs"), "images", "made_using_pygame.png")
image2path = os.path.join(os.path.dirname(__file__).replace("tests", "docs"), "images", "pygame_powered.png")


image = pygame.image.load(image1path)
image2 = pygame.image.load(image2path)

screen = pygame.display.set_mode((800, 600))

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    screen.blit(image, (0, 0))
    screen.blit(image2, (100, 100))
    pygame.display.update()