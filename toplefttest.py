#!/usr/bin/python
import topleftbut

try:
    topleftbut.top_left()
    while True:
        if topleftbut.top_left == True:
            print("top left button pushed")
            topleftbut.top_left = None

except KeyboardInterrupt:
    exit()