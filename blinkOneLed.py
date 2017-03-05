#!/usr/bin/python3

# import external modules
import RPi.GPIO as GPIO # for the Pi's GPIO
from time import sleep # to permit us to SLEEEEEP!!!

# This is helpful so that I know that my script has started running :)
print("This is my \'Blink One LED\' script")
print("Press <ctrl>+C to exit")

# fix this comment, jackass
GPIO.setmode(GPIO.BCM)

# define pins
greenLED = 23 # (pin 16 on 'old' Pi)

# define the length of time to stay blunk, in ms
blinkPeriod = 500

# pin setup
GPIO.setup(greenLED, GPIO.OUT) # the LED should be an output

# Initially, set the LED to 'off' (LOW)
GPIO.output(greenLED, GPIO.LOW)

# main loop
try:
    while True:
        greenLEDstate = GPIO.input(greenLED) # get the state of the LED
        if (greenLEDstate is GPIO.HIGH): # if it's on, turn it off
            GPIO.output(greenLED, GPIO.LOW)
        else:                       # otherwise, turn it on
            GPIO.output(greenLED, GPIO.HIGH)
        sleep((blinkPeriod / 1000.0)) # and now . . . SLEEEEEP!!!
except KeyboardInterrupt: # handle it if the user presses <ctrl>+C
    GPIO.cleanup() # cleanup all GPIO

exit(0)
