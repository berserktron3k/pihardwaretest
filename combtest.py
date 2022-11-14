#!/usr/bin/python
import combinputs

try:
    combinputs.top_ir()
    combinputs.bot_ir()
    combinputs.top_left()
    combinputs.top_right()
    combinputs.bot_left()
    combinputs.bot_right()
    while True:
        print(combinputs.top_ir)
        print(combinputs.bot_ir)
        print(combinputs.top_left)
        print(combinputs.top_right)
        print(combinputs.bot_left)
        print(combinputs.bot_right)

except KeyboardInterrupt:
    exit()