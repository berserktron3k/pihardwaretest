#!/usr/bin/python
import botirsensor

try:
    botirsensor.bottom()
    while True:
        if botirsensor.bottom == True:
            print("bottom ir sensor tripped")
            botirsensor.bottom = None

except KeyboardInterrupt:
    exit()