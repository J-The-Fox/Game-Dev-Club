"""
How To Play Sounds In Pygame.
"""

# Built-In Modules
import os
import sys
# External Modules
import pygame

# -----=====[Pygame Init]=====----- #

# Initilize The Display
pygame.display.init()

# Initilize Font
pygame.font.init()

# Initilize The Mixer
pygame.mixer.init()
# You Can Also Pre Initilize The Mixer By Using:
# pygame.mixer.pre_init(44100, -16, 2, 2048)
# The Arguments Are: Frequency, Size, Channels, Buffer, Device Name And Allowed Changes
# The Default Values Are: 44100, -16, 2, 512, None, 5

# -----=====[Pygame Setup]=====----- #
screen = pygame.display.set_mode((600, 200), pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Sounds")

# -----=====[Pygame Sounds]=====----- #
doc_folder = os.path.dirname(__file__).replace("pygame", "").replace("python", "").replace("examples", "").replace("projects", "docs")
# The Path To The Docs Folder
# This Is Used To Get The Path To The Docs Folder So We Can Load The Sounds And Music From There

pygame.mixer.music.load(os.path.join(doc_folder, "audio", "music", "The Walking Dog - Backyard.mp3"))
# Load The Music File With pygame.mixer.music.load()
# The Music Is Different From The Sound As The Music Has 1 Channel And The Sound Can Have More Than Just The 1 Channel.
# It Also Can Be Loaded Directly With pygame.mixer.music.load() While load() Is Not Used For The Sound
# It Is Mainly Used For Background Music
# The Music Can Be Paused, Unpaused, Stopped, Rewinded, And Set Volume

pygame.mixer.music.queue(os.path.join(doc_folder, "audio", "music", "The Walking Dog - Lost.mp3"))
# You Can Queue Up More Music Files To Play After The Current One Is Finished
pygame.mixer.music.queue(os.path.join(doc_folder, "audio", "music", "The Walking Dog - Umbrella Shakeup.mp3"))
pygame.mixer.music.queue(os.path.join(doc_folder, "audio", "music", "The Walking Dog - Afterglow.mp3"))

sound_object = pygame.mixer.Sound(os.path.join(doc_folder, "audio", "sounds", "Tap.mp3"))
# Load The Sound File With pygame.mixer.Sound() And Store It In A Variable So We Can Play It Later
# You Can Specify Which Channel You Want The Sound To Play On By Using pygame.mixer.Channel(channel_num).play(sound_object)

# -----=====[Pygame Fonts]=====----- #
font = pygame.font.Font(None, 25)

def main():
    pygame.mixer_music.play(0) # A Loop Of 0 Means It Won't Loop. A Loop Of -1 Means It Will Loop Forever
    while True:
        screen.fill((252, 145, 0)) # Background Color

        # -----=====[Pygame Text]=====----- #
        screen.blit(font.render("Click The Mouse To Play The Sound", True, (255, 255, 255), (0, 0, 0)), (10, 10))

        # -----=====[Pygame Events]=====----- #
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN: # When The Mouse Is Clicked, Play The Sound
                pygame.mixer.Channel(1).play(sound_object)
                # Play The Sound On Channel 1

        clock.tick(60) # 60 FPS
        pygame.display.update()

if __name__ == "__main__":
    main()