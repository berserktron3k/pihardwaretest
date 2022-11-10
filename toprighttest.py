#!/usr/bin/python
import toprightbut

try:
    toprightbut.top_right()
    while True:
        if toprightbut.top_right == True:
            print("top right button pushed")
            toprightbut.top_right = None

except KeyboardInterrupt:
    exit()