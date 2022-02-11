from time import sleep
import RPi.GPIO as GPIO

DIR = 20
STEP = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)


for x in range(100):
    GPIO.output(STEP, GPIO.HIGH)
    #GPIO.output(DIR, GPIO.LOW)
    sleep(0.005)
    #GPIO.output(DIR, GPIO.HIGH)
    #sleep(0.05)
    
