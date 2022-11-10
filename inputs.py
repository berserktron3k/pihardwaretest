#!/usr/bin/python
import RPi.GPIO as GPIO

# Function for top sensor
def top():
    
    def top_cb(top_pin):
        global top
        top = True
        return top

    GPIO.setmode(GPIO.BCM)
    top_pin = 17
    GPIO.setup(top_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(top_pin, GPIO.FALLING, top_cb, bouncetime=1000)

# Function for bottom sensor
def bottom():
    
    def bot_cb(bot_pin):
        global bottom
        bottom = True
        return bottom

    GPIO.setmode(GPIO.BCM)
    bot_pin = 27
    GPIO.setup(bot_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(bot_pin, GPIO.FALLING, bot_cb, bouncetime=1000)

# Function for top left button
def top_left():
    
    def top_left_cb(top_left_pin):
        global top_left
        top_left = True
        return top_left
    
    GPIO.setmode(GPIO.BCM)
    top_left_pin = 22
    GPIO.setup(top_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(top_left_pin, GPIO.RISING, top_left_cb, bouncetime=1000)

# Function for bottom left button
def bot_left():
    
    def bot_left_cb(bot_left_pin):
        global bot_left
        bot_left = True
        return bot_left
    
    GPIO.setmode(GPIO.BCM)
    bot_left_pin = 23
    GPIO.setup(bot_left_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(bot_left_pin, GPIO.RISING, bot_left_cb, bouncetime=1000)

# Function for top right button
def top_right():
    
    def top_right_cb(top_right_pin):
        global top_right
        top_right = True
        return top_right
    
    GPIO.setmode(GPIO.BCM)
    top_right_pin = 24
    GPIO.setup(top_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(top_right_pin, GPIO.RISING, top_right_cb, bouncetime=1000)

# Fuction for bottom right button
def bot_right():
    
    def bot_right_cb(bot_right_pin):
        global bot_right
        bot_right = True
        return bot_right
    
    GPIO.setmode(GPIO.BCM)
    bot_right_pin = 25
    GPIO.setup(bot_right_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(bot_right_pin, GPIO.RISING, bot_right_cb, bouncetime=1000)