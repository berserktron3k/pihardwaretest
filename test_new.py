#!/usr/bin/python
import inputs_new

print("first we check the current status")
print(inputs_new.top_sensor)
print(inputs_new.bot_sensor)
print(inputs_new.top_left_button)
print(inputs_new.top_right_button)
print(inputs_new.bot_left_button)
print(inputs_new.bot_right_button)

print("now we test dynamically")
while True:
    if inputs_new.top_sensor == True:
        print("top sensor status " + inputs_new.top_sensor)
    if inputs_new.bot_sensor == True:
        print("bot sensor status " + inputs_new.bot_sensor)
    if inputs_new.top_left_button == True:
        print("top left button status " + inputs_new.top_left_button)
    if inputs_new.top_right_button == True:
        print("top right button status " + inputs_new.top_right_button)
    if inputs_new.bot_left_button == True:
        print("bot left button status " + inputs_new.bot_left_button)
    if inputs_new.bot_right_button == True:
        print("bot right button status " + inputs_new.bot_right_button)