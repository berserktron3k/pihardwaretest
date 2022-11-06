#!/usr/bin/python
# Import modules

import inputs
import pygame
import sys
import os
import glob
import random

# Variables

audio_absolute_path = os.path.dirname(__file__)
audio_relative_path = "assets/attractmode/audio"
audio_full_path = os.path.join(audio_absolute_path, audio_relative_path, '*.ogg')
attract = True
fps = 60 # Framerate
ani = 4 # Animaction Cycles
clock = pygame.time.Clock()
audio = glob.glob(audio_full_path)
black = (0, 0, 0)

# Setup

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume((0.7))
pygame.mixer.music.load(random.choice(audio))

# Attract mode
try:
    inputs.top()
    inputs.bottom()
    inputs.top_left()
    inputs.top_right()
    inputs.bot_left()
    inputs.bot_right()
    while attract:
        if (inputs.top == True or inputs.bottom == True or inputs.top_left == True or inputs.bot_left == True or inputs.bot_right == True):
            try:
                sys.exit()
            finally:
                attract = False
        world = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        world.fill(black)
        pygame.mouse.set_visible(False)
        pygame.display.flip()
        clock.tick(fps)
        pygame.mixer.music.play()

except KeyboardInterrupt:
    exit()