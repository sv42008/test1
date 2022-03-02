from time import sleep
import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM) # using BCM numbering system

# setting up pins (states and allocations to driver)
# DIR =  20
M1A =20
M1B = 16

M2A = 23
M2B = 24
#STEP = 
# MODE0 = 17
# MODE1 = 4
# MODE2 = 3
# EN = 20

# input_list = [MODE0, MODE1, MODE2]
#output_list = [STEP, DIR, 7]
output_list2 = [M1A, M1B, M2A, M2B]

# GPIO.setup(input_list, GPIO.IN)
GPIO.setup(output_list2, GPIO.OUT, initial=GPIO.LOW)
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
    #q.stop()

    
def old_motor_driver_flashing(freq):
    dutycycle = 8
    
    p = GPIO.PWM(M1B, freq)
    q = GPIO.PWM(M2B, freq)
    p.start(dutycycle)
    q.start(dutycycle)
    input('press return to reset')
    GPIO.setup(output_list2, GPIO.OUT, initial=GPIO.LOW)
    p.stop()
    q.stop()

def flashing2(frequency):
    for dc in range(0, 100, 10):     
        p = GPIO.PWM(STEP, frequency)
        p.start(dc)
        #input('Press return to stop ')
        sleep(1)
        p.stop()
    input('Press return to stop')
    
def ramp(gauge, frequency):
    #gauge will be a value between 0 and 1, with 1 being the slowest acceleration and deceleration)
    if 10*gauge in range(0, 10):

        for freq in range(1, frequency, 10):
            p = GPIO.PWM(STEP, freq)
            p.start(5)
            sleep(1/freq)
            p.stop()
            sleep(1/freq)
        
        sleep(2)

        for freq in range(1, frequency):
            p = GPIO.PWM(STEP, frequency - freq)
            p.start(1)
            sleep(gauge)
            p.stop()

        p.stop()

    else:
        print("Gauge is outside of range")
        
def flashing3(gauge, frequency):
    dutycycle = 50

    p = GPIO.PWM(STEP, frequency)
    p.start(dutycycle)
    sleep(gauge/100)
    p.stop()
        
def ramp2(gauge, frequency):
    dutycycle = 50
    for i in range(0, 100):
        
        p = GPIO.PWM(STEP, 1+ (i/100)*(frequency-1))
        p.start(dutycycle)
        sleep(1)
        p.stop()

old_motor_driver_flashing(100)


GPIO.cleanup()

