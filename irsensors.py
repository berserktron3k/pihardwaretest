#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Define top and bottom sensors and get result
def top_sensor():
    global top
    GPIO.setmode(GPIO.BCM)
    top_pin = 17
    GPIO.setup(top_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    top = GPIO.input(top_pin)
    return top

def bottom_sensor():
    global bottom
    GPIO.setmode(GPIO.BCM)
    bot_pin = 27
    GPIO.setup(bot_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    bottom = GPIO.input(bot_pin)
    return bottom