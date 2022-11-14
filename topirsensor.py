#!/usr/bin/python
import RPi.GPIO as GPIO

# function for top sensor
def top():
    
    def top_cb(top_pin):
        #global top
        #top = True
        top = GPIO.event_detected(top_pin)
        return top

    GPIO.setmode(GPIO.BCM)
    top_pin = 17
    GPIO.setup(top_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(top_pin, GPIO.FALLING, top_cb, bouncetime=3000)