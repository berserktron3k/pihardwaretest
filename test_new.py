#!/usr/bin/python
import topirsensor
import botirsensor
import topleftbut
import toprightbut
import botleftbut
import botrightbut

try:
    topirsensor.top()
    botirsensor.bottom()
    topleftbut.top_left()
    toprightbut.top_right()
    botleftbut.bot_left()
    botrightbut.bot_right()
    while True:
        if topirsensor.top == True:
            print("top ir sensor tripped")
            topirsensor.top = None

        if botirsensor.bottom == True:
            print("bottom ir sensor tripped")
            botirsensor.bottom() = None

        if topleftbut.top_left == True:
            print("top left button pushed")
            topleftbut.top_left = None

        if toprightbut.top_right == True:
            print("top right button pushed")
            toprightbut.top_right = None

        if botleftbut.bot_left == True:
            print("bottom left button pushed")
            botleftbut.bot_left = None

        if botrightbut.bot_right == True:
            print("bottom right button pushed")
            botrightbut.bot_right = None

except KeyboardInterrupt:
    exit()