#to stop the pump

import pigpio
from time import sleep

G1 = 20
G2 = 25

pi = pigpio.pi()
pi.set_mode(G1, pigpio.OUTPUT)
pi.set_mode(G2, pigpio.OUTPUT)
stop = []
stop.append(pigpio.pulse(1<<G1, 1>>G2, 1000000))

pi.wave_add_generic(stop)
stp = pi.wave_create()

pi.wave_send_repeat(stp)
sleep(1)