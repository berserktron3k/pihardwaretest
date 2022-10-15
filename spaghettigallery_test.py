#!/usr/bin/python
import irsensors

try:
    while True:
        if not irsensors.get_top():
            print("top sensor tripped")
        if not irsensors.get_bottom():
            print("bottom sensor tripped")

except KeyboardInterrupt:
    exit()