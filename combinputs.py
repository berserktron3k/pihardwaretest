#!/usr/bin/python
import RPi.GPIO as GPIO

# set pins
top_ir_sensor = 17
bot_ir_sensor = 27
top_left_button = 21
top_right_button = 16
bot_left_button = 19
bot_right_button = 24

# set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(top_ir_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bot_ir_sensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(top_left_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(top_right_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bot_left_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bot_right_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# define callbacks

def top_ir_cb(top_ir_sensor):
    top_ir = True
    return top_ir

def bot_ir_cb(bot_ir_sensor):
    bottom_ir = True
    return bottom_ir

def top_left_cb(top_left_button):
    top_left = True
    return top_left

def top_right_cb(top_right_button):
    top_right = True
    return top_right

def bot_left_cb(bot_left_button):
    bot_left = True
    return bot_left

def bot_right_cb(bot_right_button):
    bot_right = True
    return bot_right

# create GPIO event detects
GPIO.add_event_detect(top_ir_sensor, GPIO.FALLING, top_ir_cb, bouncetime=3000)
GPIO.add_event_detect(bot_ir_sensor, GPIO.FALLING, bot_ir_cb, bouncetime=3000)
GPIO.add_event_detect(top_left_button, GPIO.RISING, top_left_cb, bouncetime=1000)
GPIO.add_event_detect(top_right_button, GPIO.RISING, top_right_cb, bouncetime=1000)
GPIO.add_event_detect(bot_left_button, GPIO.RISING, bot_left_cb, bouncetime=1000)
GPIO.add_event_detect(bot_right_button, GPIO.RISING, bot_right_cb, bouncetime=1000)