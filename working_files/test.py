""" to test the motor action """
from time import sleep
import RPi.GPIO as GPIO

def setup_pins(pins, output_or_input = "output"):
    """'pins' is a list of integer values relating to the pin number, choose pins as output or input,
     defaults to output set to low."""
    GPIO.setwarnings(False)                                                        
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        if output_or_input == "input":
            print("{} set to input.".format(pin))
            GPIO.setup(pin, GPIO.IN)
        else:
            print("{} set to output.".format(pin))
            GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

def epoch(del_t):
  # move and track progressing a unit of time
  sleep(del_t)
  #global timer
  #timer = timer + del_t
  #print(timer)
  
STEP = 5
del_t = 0.001
DIR = 6
STEP2 = 12
DIR2 = 13

setup_pins([STEP, STEP2, DIR, DIR2])
for i in range(100000):
     GPIO.output(STEP, 1)
     GPIO.output(STEP2, 1)
     print("pulse on")
     epoch(del_t)
     GPIO.output(STEP, 0)
     GPIO.output(STEP2, 0)
     print("pulse off")
     epoch(del_t)
