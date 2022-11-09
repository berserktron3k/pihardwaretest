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
        if inputs.top == 0:
            print("top sensor tripped")
            inputs.top = None # this resets it back to null preventing infinite loop
        
        if inputs.bottom == 0:
            print("bottom sensor tripped")
            inputs.bottom = None # this resets it back to null preventing infinite loop
        
        if inputs.top_left == 1:
            print("top left button pushed")
            inputs.top_left = None
        
        if inputs.top_right == 1:
            print("top right button pushed")
            inputs.top_right = None
        
        if inputs.bot_left == 1:
            print("bottom left button pushed")
            inputs.bot_left = None
        
        if inputs.bot_right == 1:
            print("bottom right button pushed")
            inputs.bot_right = None

except KeyboardInterrupt:
    exit()