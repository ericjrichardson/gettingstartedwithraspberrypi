#!/usr/bin/python3

# import external modules
import RPi.GPIO as GPIO # for the Pi's GPIO
from time import sleep # to permit us to SLEEEEEP!!!

# define the LEDState class
class LEDState(object):

    # set the pin-numbering mode; GPIO.BOARD for the way the ribbon numbers it; GPIO.BCM for the way the processor does
    # (the breakout cable uses GPIO.BCM)
    GPIO.setmode(GPIO.BCM)

    # define pins
    greenLED = 23 # (GPIO 23 is pin 16)
    yellowLED = 18 # (GPIO 18 is pin 12)
    redLED = 17 # (GPIO 17 is pin 11)

    # pin setup; still set PWM pins as output first
    GPIO.setup(greenLED, GPIO.OUT)
    GPIO.setup(yellowLED, GPIO.OUT)
    GPIO.setup(redLED, GPIO.OUT)

    def __init__(self, greenLEDState, yellowLEDState, redLEDState):
        self.greenLEDState = greenLEDState
        self.yellowLEDState = yellowLEDState
        self.redLEDState = redLEDState

    def setState(self):
        GPIO.output(LEDState.greenLED, self.greenLEDState)
        GPIO.output(LEDState.yellowLED, self.yellowLEDState)
        GPIO.output(LEDState.redLED, self.redLEDState)

def advance(stateNum, states):
    stateNum += 1
    if (stateNum >= len(states)):
        stateNum = 0
    states[stateNum].setState()
    return stateNum

def reverse(stateNum, states):
    stateNum -= 1
    if (stateNum <= 0):
        stateNum = (len(states) - 1)
    states[stateNum].setState()
    return stateNum

# begin "main"
# This is helpful so that I know that my script has started running :)
print("This is my \'Digital Input\' script")
print("Press <ctrl>+C to exit")

# create the LED states
stateList = []
stateList.append(LEDState(GPIO.LOW, GPIO.LOW, GPIO.LOW))
stateList.append(LEDState(GPIO.HIGH, GPIO.LOW, GPIO.LOW))
stateList.append(LEDState(GPIO.LOW, GPIO.HIGH, GPIO.LOW))
stateList.append(LEDState(GPIO.LOW, GPIO.LOW, GPIO.HIGH))

# define the pin to use for the input
inputPin = 4 # (GPIO 4 is pin 7)

# set up the input Button with a pulldown
GPIO.setup(inputPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# define the advance blink period, in ms
advancePeriod = 500

# define the reverse blink period, in ms
reversePeriod = 125

# variable to store the current state information in
i = 0

# main loop
try:
    while True:
        # if the button is not pressed, then advance
        buttonState = GPIO.input(inputPin)
        if (buttonState is GPIO.HIGH):
            i = advance(i, stateList)
            sleep(advancePeriod / 1000.0)
        # if the button IS pressed, then reverse
        elif (buttonState is GPIO.LOW):
            i = reverse(i, stateList)
            sleep(reversePeriod / 1000.0)

except KeyboardInterrupt: # handle it if the user presses <ctrl>+C
    GPIO.cleanup() # cleanup all GPIO
    exit(0)

# clean up on normal exit also
GPIO.cleanup()
exit(0)

