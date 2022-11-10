#!/usr/bin/python
import botrightbut

try:
    botrightbut.bot_right()
    while True:
        if botrightbut.bot_right == True:
            print("bottom right button pushed")
            botrightbut.bot_right = None

except KeyboardInterrupt:
    exit()