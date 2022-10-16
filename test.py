#!/usr/bin/python
import irsensors

try:
    irsensors.top()
    irsensors.bottom()
    while True:
        if irsensors.top == True:
            print("top sensor tripped")
            irsensors.top = None # this resets it back to null preventing infinite loop
        if irsensors.bottom == True:
            print("bottom sensor tripped")
            irsensors.bottom = None # this resets it back to null preventing infinite loop

except KeyboardInterrupt:
    exit()