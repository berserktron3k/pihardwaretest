#!/usr/bin/python
import RPi.GPIO as GPIO

# fuction for bottom right button
def bot_right():
    
    def bot_right_cb(bot_right_pin):
        global bot_right
        bot_right = True
        return bot_right
    
    GPIO.setmode(GPIO.BCM)
    bot_right_pin = 25
    GPIO.setup(bot_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(bot_right_pin, GPIO.RISING, bot_right_cb, bouncetime=1000)