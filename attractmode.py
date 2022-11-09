#!/usr/bin/python
# import modules

import inputs
import pygame
import sys
import os
import glob
import random
import time

# variables

attract = True
fps = 60 # Framerate
ani = 4 # Animaction Cycles
clock = pygame.time.Clock()
attract_song = random.choice(glob.glob("./assets/attractmode/audio/*"))
black = (0, 0, 0)
loop = 1

# setup

pygame.init()
pygame.mixer.init()

# run attract mode

try:
    # check status of buttons and ir sensors
    inputs.top()
    inputs.bottom()
    inputs.top_left()
    inputs.top_right()
    inputs.bot_left()
    inputs.bot_right()
    # begin main attract mode loop
    while attract:
        if (inputs.top == True or inputs.bottom == True or inputs.top_left == True or inputs.bot_left == True or inputs.bot_right == True):
            try:
                sys.exit()
            finally:
                attract = False
        # create the graphic display
        world = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        world.fill(black)
        pygame.mouse.set_visible(False) # hides the mouse cursor
        pygame.display.flip() # update the full display surface to the screen
        clock.tick(fps) # advance animation
        # this bit loads the background track in the pygame mixer
        # we play the song at full volume once, wait 120 seconds, 
        # then play it in a loop at half the volume
        pygame.mixer.music.load(attract_song)
        if loop < 2:
            pygame.music.set_volume(0.8)
            pygame.mixer.music.play()
            # this bit makes sure the background music plays
            while pygame.mixer.music.get_busy():
                pass
            loop +=1
        else:
            time.sleep(120)
            pygame.music.set_volume(0.4)
            pygame.mixer.music.play()
            # this bit makes sure the background music plays
            while pygame.mixer.music.get_busy():
                pass
            loop +=1
except KeyboardInterrupt:
    exit()