#!/usr/bin/python
import botleftbut

try:
    botleftbut.bot_left()
    while True:
        if botleftbut.bot_left == True:
            print("bottom left button pushed")
            botleftbut.bot_left = None

except KeyboardInterrupt:
    exit()