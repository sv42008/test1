from time import sleep
from gpiozero import LED

red = LED(13)

while True:
    red.on()
    sleep(0.5)
    red.off()
    sleep(0.1) 