#!/usr/bin/python
import RPi.GPIO as GPIO

# function for top right button
def top_right():
    
    def top_right_cb(top_right_pin):
        global top_right
        top_right = True
        return top_right
    
    GPIO.setmode(GPIO.BCM)
    top_right_pin = 16
    GPIO.setup(top_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(top_right_pin, GPIO.RISING, top_right_cb, bouncetime=1000)