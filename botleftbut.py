#!/usr/bin/python
import RPi.GPIO as GPIO

# function for bottom left button
def bot_left():
    
    def bot_left_cb(bot_left_pin):
        global bot_left
        bot_left = True
        return bot_left
    
    GPIO.setmode(GPIO.BCM)
    bot_left_pin = 19
    GPIO.setup(bot_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(bot_left_pin, GPIO.RISING, bot_left_cb, bouncetime=1000)