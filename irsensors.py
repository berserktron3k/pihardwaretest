#!/usr/bin/python
import RPi.GPIO as GPIO

def top():
    def topcb(channel):
        global top
        top = True
        return top

    GPIO.setmode(GPIO.BCM)
    top_pin = 17
    GPIO.setup(top_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(top_pin, GPIO.FALLING, topcb, bouncetime=1000)

def bottom():
    def botcb(channel):
        global bottom
        bottom = True
        return bottom

    GPIO.setmode(GPIO.BCM)
    bot_pin = 27
    GPIO.setup(bot_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(bot_pin, GPIO.FALLING, botcb, bouncetime=1000)