#!/usr/bin/python
import topirsensory
import botirsensor
import topleftbut
import toprightbut
import botleftbut
import botrightbut

try:
    topirsensory.top()
    botirsensor.bottom()
    topleftbut.top_left()
    toprightbut.top_right()
    botleftbut.bot_left()
    botrightbut.bot_right()
    while True:
        if topirsensory.top == True:
            print("top sensor tripped")
            topirsensory.top = None # this resets it back to null preventing infinite loop
        
        if botirsensor.bottom == True:
            print("bottom sensor tripped")
            botirsensor.bottom = None # this resets it back to null preventing infinite loop
        
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