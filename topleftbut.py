#!/usr/bin/python
import RPi.GPIO as GPIO

# function for top left button
def top_left():
    
    def top_left_cb(top_left_pin):
        global top_left
        top_left = True
        return top_left
    
    GPIO.setmode(GPIO.BCM)
    top_left_pin = 22
    GPIO.setup(top_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(top_left_pin, GPIO.RISING, top_left_cb, bouncetime=1000)