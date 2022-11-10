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
    if inputs_new.top_sensor == 1:
        print("top sensor status:")
        print(inputs_new.top_sensor)
    if inputs_new.bot_sensor == 1:
        print("bot sensor status:")
        print(inputs_new.bot_sensor)
    if inputs_new.top_left_button == 1:
        print("top left button status:")
        print(inputs_new.top_left_button)
    if inputs_new.top_right_button == 1:
        print("top right button status:")
        print(inputs_new.top_right_button)
    if inputs_new.bot_left_button == 1:
        print("bot left button status:")
        print(inputs_new.bot_left_button)
    if inputs_new.bot_right_button == 1:
        print("bot right button status:")
        print(inputs_new.bot_right_button)