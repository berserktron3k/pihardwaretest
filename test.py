#!/usr/bin/python
import inputs

try:
    inputs.top()
    inputs.bottom()
    while True:
        if inputs.top == True:
            print("top sensor tripped")
            inputs.top = None # this resets it back to null preventing infinite loop
        if inputs.bottom == True:
            print("bottom sensor tripped")
            inputs.bottom = None # this resets it back to null preventing infinite loop

except KeyboardInterrupt:
    exit()