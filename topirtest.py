#!/usr/bin/python
import topirsensor

try:
    topirsensor.top()
    while True:
        if topirsensor.top == True:
            print("top ir sensor tripped")
            topirsensor.top = None

except KeyboardInterrupt:
    exit()