#!/usr/bin/python3

# import external modules
import RPi.GPIO as GPIO # for the Pi's GPIO
from time import sleep # to permit us to SLEEEEEP!!!

# This is helpful so that I know that my script has started running :)
print("This is my \'Digital Outputs\' script")
print("Press <ctrl>+C to exit")

# set the pin-numbering mode; GPIO.BOARD for the way the ribbon numbers it; GPIO.BCM for the way the processor does
# (the breakout cable uses GPIO.BCM)
GPIO.setmode(GPIO.BCM)

# define pins
greenLED = 23 # (GPIO 23 is pin 16)
yellowLED = 18 # (GPIO 18 is pin 12)
redLED = 17 # (GPIO 17 is pin 11)

# define the length of time to stay blunk, in ms
blinkPeriod = 500

# pin setup; this script only uses digital outputs
GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)

# Initially, set the LEDs to 'off' (LOW)
GPIO.output(greenLED, GPIO.LOW)
GPIO.output(yellowLED, GPIO.LOW)
GPIO.output(redLED, GPIO.LOW)

# main loop
try:
    while True:
        # get the states of the three LEDs
        greenLEDstate = GPIO.input(greenLED)
        yellowLEDstate = GPIO.input(yellowLED)
        redLEDstate = GPIO.input(redLED)
        # if green is on, turn it off and turn yellow on
        if (greenLEDstate is GPIO.HIGH):
            GPIO.output(greenLED, GPIO.LOW)
            GPIO.output(yellowLED, GPIO.HIGH)
            GPIO.output(redLED, GPIO.LOW)
        # if yellow is on, turn it off and turn red on
        elif (yellowLEDstate is GPIO.HIGH):
            GPIO.output(greenLED, GPIO.LOW)
            GPIO.output(yellowLED, GPIO.LOW)
            GPIO.output(redLED, GPIO.HIGH)
        # if red is on, end of the line: turn them all off
        elif (redLEDstate is GPIO.HIGH):
            GPIO.output(greenLED, GPIO.LOW)
            GPIO.output(yellowLED, GPIO.LOW)
            GPIO.output(redLED, GPIO.LOW)
        # otherwise they are all off; start over at green
        else:
            GPIO.output(greenLED, GPIO.HIGH)
            GPIO.output(yellowLED, GPIO.LOW)
            GPIO.output(redLED, GPIO.LOW)
        # and now . . . SLEEEEEP!!!
        sleep((blinkPeriod / 1000.0)) # divide by 1000.0 rather than 1000 so it's a floating-point number
except KeyboardInterrupt: # handle it if the user presses <ctrl>+C
    # GPIO.output(greenLED, GPIO.LOW) # set the LED to 'LOW'
    GPIO.cleanup() # cleanup all GPIO

exit(0)
