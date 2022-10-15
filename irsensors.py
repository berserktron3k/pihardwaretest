#!/usr/bin/python
import RPi.GPIO as GPIO

# Set GPIO to BCM
GPIO.setmode(GPIO.BCM)

# Define top and bottom sensors and get result
def get_top():
    global top
    top_pin = 17
    GPIO.setup(top_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    top = GPIO.input(top_pin)
    return top
    GPIO.cleanup()

def get_bottom():
    global bottom
    bot_pin = 27
    GPIO.setup(bot_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    bottom = GPIO.input(bot_pin)
    return bottom
    GPIO.cleanup()