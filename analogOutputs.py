#!/usr/bin/python3

# import external modules
import RPi.GPIO as GPIO # for the Pi's GPIO
from time import sleep # to permit us to SLEEEEEP!!!

# This is helpful so that I know that my script has started running :)
print("This is my \'Analog Outputs\' script")
print("Press <ctrl>+C to exit")

# set the pin-numbering mode; GPIO.BOARD for the way the ribbon numbers it; GPIO.BCM for the way the processor does
# (the breakout cable uses GPIO.BCM)
GPIO.setmode(GPIO.BCM)

# define pins
greenLED = 23 # (GPIO 23 is pin 16)
yellowLED = 18 # (GPIO 18 is pin 12)
redLED = 17 # (GPIO 17 is pin 11)

# define the length of time to hold a single duty cycle, in ms
dutyCycleHoldPeriod = 1000

# define the frequency to use for PWM output
pwmFrequency = 1000

# define the (percentage) amount we will increment or decrement the duty cycle each time
dutyCycleJump = 20

# pin setup; still set PWM pins as output first
GPIO.setup(greenLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)
GPIO.setup(redLED, GPIO.OUT)
# pin setup; now initialize new pwm objects for each of the LED pins
greenPWM = GPIO.PWM(greenLED, pwmFrequency)
yellowPWM = GPIO.PWM(yellowLED, pwmFrequency)
redPWM = GPIO.PWM(redLED, pwmFrequency)

# Set all PWM outputs to a duty cycle of 0 to turn them off
greenPWM.start(0)
yellowPWM.start(0)
redPWM.start(0)

# initially we will turn up the PWMs.
# Later we will turn them down.
turnUp = True

# start with a duty cycle of 0
dutyCycle = 0

# main loop
try:
    while True:
        # If we've reached a duty cycle of 100, then we can stop "turning up" the PWMs
        if (dutyCycle >= 100):
            turnUp = False
        # But, if the duty cycle has fallen to 0, then it's time to "turn up" the PWMs again
        elif (dutyCycle <= 0):
            turnUp = True
        # now increment the duty cycle if we're turning the PWMs "up"
        if (turnUp):
            dutyCycle += dutyCycleJump
        elif (not turnUp):
            dutyCycle -= dutyCycleJump
        # Set those PWM duty cycles!
        greenPWM.ChangeDutyCycle(dutyCycle)
        yellowPWM.ChangeDutyCycle(dutyCycle)
        redPWM.ChangeDutyCycle(dutyCycle)
        # and now . . . SLEEEEEP!!!
        sleep((dutyCycleHoldPeriod / 1000.0)) # divide by 1000.0 rather than 1000 so it's a floating-point number
except KeyboardInterrupt: # handle it if the user presses <ctrl>+C
    # turn off all three PWMs
    greenPWM.stop()
    yellowPWM.stop()
    redPWM.stop()
    GPIO.cleanup() # cleanup all GPIO

exit(0)
