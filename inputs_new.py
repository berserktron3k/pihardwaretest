#!/usr/bin/python
import RPi.GPIO as GPIO

# setup variables
top_sensor_pin = 17
bot_sensor_pin = 27
top_left_pin = 22
bot_left_pin = 23
top_right_pin = 24
bot_right_pin = 25
top_sensor = 0
bot_sensor = 0
top_left_button = 0
top_right_button = 0
bot_left_button = 0
bot_right_button = 0

# setup GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(top_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(bot_sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(top_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bot_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(top_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(bot_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# define callbacks
def top_sensor_cb(top_sensor_pin):
    global top_sensor
    top_sensor = GPIO.input(top_sensor_pin)
    return top_sensor
    
def bot_sensor_cb(bot_sensor_pin):
    global bot_sensor
    bot_sensor = GPIO.input(bot_sensor_pin)
    return bot_sensor

def top_left_button_cb(top_left_pin):
    global top_left_button
    top_left_button = GPIO.input(top_left_pin)
    return top_left_button

def bot_left_button_cb(bot_left_pin):
    global bot_left_button
    bot_left_button = GPIO.input(bot_left_pin)
    return bot_left_button

def top_right_button_cb(top_right_pin):
    global top_right_button
    top_right_button = GPIO.input(top_right_pin)
    return top_right_button

def bot_right_button_cb(bot_right_pin):
    global bot_right_button
    bot_right_button = GPIO.input(bot_right_pin)
    return bot_right_button

# add event detects
GPIO.add_event_detect(top_sensor_pin, GPIO.FALLING, top_sensor_cb, bouncetime=1000)
GPIO.add_event_detect(bot_sensor_pin, GPIO.FALLING, bot_sensor_cb, bouncetime=1000)
GPIO.add_event_detect(top_left_pin, GPIO.RISING, top_left_button_cb, bouncetime=1000)
GPIO.add_event_detect(bot_left_pin, GPIO.RISING, bot_left_button_cb, bouncetime=1000)
GPIO.add_event_detect(top_right_pin, GPIO.RISING, top_right_button_cb, bouncetime=1000)
GPIO.add_event_detect(bot_right_pin, GPIO.RISING, bot_right_button_cb, bouncetime=1000)