#!/usr/bin/python
import inputs

try:
    inputs.top()
    inputs.bottom()
    inputs.top_left()
    inputs.top_right()
    inputs.bot_left()
    inputs.bot_right()
    while True:
        if inputs.top == True:
            print("top sensor tripped")
            inputs.top = None # this resets it back to null preventing infinite loop
        if inputs.bottom == True:
            print("bottom sensor tripped")
            inputs.bottom = None # this resets it back to null preventing infinite loop
        if inputs.top_left == True:
            print("top left button pushed")
            inputs.top_left = None
        if inputs.top_right == True:
            print("top right button pushed")
            inputs.top_right = None
        if inputs.bot_left == True:
            print("bottom left button pushed")
            inputs.bot_left = None
        if inputs.bot_right == True:
            print("bottom right button pushed")
            inputs.bot_right = None

except KeyboardInterrupt:
    exit()