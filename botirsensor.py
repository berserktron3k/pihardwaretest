#!/usr/bin/python
import RPi.GPIO as GPIO

# function for bottom sensor
def bottom():
    
    def bot_cb(bot_pin):
        global bottom
        bottom = True
        return bottom

    GPIO.setmode(GPIO.BCM)
    bot_pin = 5
    GPIO.setup(bot_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(bot_pin, GPIO.FALLING, bot_cb, bouncetime=1000)