#!/usr/bin/python
# Import modules

import inputs
import pygame
import sys
import os

# Variables

attract = True
world_x = 1280
world_y = 1024
fps = 60
ani = 4
black = (0, 0, 0)

# Setup

clock = pygame.time.Clock()
pygame.init()

# Attract mode
try:
    inputs.top()
    inputs.bottom()
    inputs.top_left()
    inputs.top_right()
    inputs.bot_left()
    inputs.bot_right()
    while attract:
        if (inputs.top == True OR inputs.bottom == True OR inputs.top_left == True OR inputs.bot_left == True OR inputs.bot_right == True)
            pygame.quit()
            try:
                sys.exit()
            finally:
                attract = False
        world = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        world.fill(black)
        pygame.display.flip()
        clock.tick(fps)
        
except KeyboardInterrupt:
    exit()