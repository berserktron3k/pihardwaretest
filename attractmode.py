#!/usr/bin/python
# Import modules

import inputs
import pygame
import sys
import os
import glob
import random

# Variables

attract = True
fps = 60 # Framerate
ani = 4 # Animaction Cycles
clock = pygame.time.Clock()
audio = glob.glob("./assets/attractmode/audio/*")
black = (0, 0, 0)

# Setup

pygame.init()
pygame.mixer.init()

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
        pygame.mixer.music.load(random.choice(audio))
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play()

except KeyboardInterrupt:
    exit()