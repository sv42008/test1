from time import sleep
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM) # using BCM numbering system

# setting up pins (states and allocations to driver)
DIR =  16
STEP = 20
# MODE0 = 17
# MODE1 = 4
# MODE2 = 3
# EN = 20

# input_list = [MODE0, MODE1, MODE2]
output_list = [STEP, DIR]
#output_list2 = [M1A, M1B, M2A, M2B]

# GPIO.setup(input_list, GPIO.IN)
GPIO.setup(output_list, GPIO.OUT, initial=GPIO.LOW)
#GPIO.setup(DIR, GPIO.OUT, initial=GPIO.LOW)
#GPIO.output(DIR, 1)

# Simple PWM generation
def flashing(frequency):
    dutycycle = 20

    p = GPIO.PWM(STEP, frequency)
    p.start(dutycycle)
    #sleep(1/(2*frequency))
    #q = GPIO.PWM(7, frequency)
    #q.start(dutycycle)
    input('Press return to stop ')
    p.stop()
    GPIO.setup(output_list, GPIO.OUT, initial=GPIO.OUT)
    #q.stop()

flashing(10)