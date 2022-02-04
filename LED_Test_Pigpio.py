import pigpio
from time import sleep

pi = pigpio.pi()

G1 = 20
G2 = 25

pi.set_mode(G1, pigpio.OUTPUT)
pi.set_mode(G2, pigpio.OUTPUT)

# while True:
#     pi.set_PWM_dutycycle(13, 0)
#     sleep(1)
#     
#     pi.set_PWM_dutycycle(13, 64)
#     sleep(1)
#     
#     pi.set_PWM_dutycycle(13, 255)
#     sleep(1)
#     
#works!

# while True:
#     pi.set_PWM_frequency(13, 0)
#     print(pi.get_PWM_frequency(13))
#     sleep(5)
#     
#     pi.set_PWM_frequency(13, 320)
#     print(pi.get_PWM_frequency(13))
#     sleep(5)
#     `
#     pi.set_PWM_frequency(13, 19)
#     print(pi.get_PWM_frequency(13))
#     sleep(5)

#works! rounds to nearest frequency that it can work with. Chart on pigpio docs.

flashing1 = []
flashing2 = []
stop = []
stop.append(pigpio.pulse(1<<G1, 1>>G2, 1000000))
flashing1.append(pigpio.pulse(1<<G1, 1<<G2, 100000))
# flashing1.append(pigpio.pulse(1<<G1, 1>>G2, 100000))
flashing2.append(pigpio.pulse(1<<G2, 1<<G1, 1000000))

pi.wave_clear() # clear any existing waveforms

pi.wave_add_generic(flashing1) # 1 s flashes
f1 = pi.wave_create() # create and save id

pi.wave_add_generic(flashing2) # 1 s flashes
f2 = pi.wave_create() # create and save id

pi.wave_add_generic(stop)
stp = pi.wave_create()

pi.wave_send_repeat(f1)

sleep(4)

pi.wave_send_repeat(f2)

sleep(4)

pi.wave_send_repeat(stp)

sleep(1)
# 
# def droplet(volume, number):
#     for i in range(number):        
#         pi.wave_send_repeat(f1)
#         sleep(volume)
#         pi.wave_send_repeat(stp)
#         sleep(2)

# droplet(0.6, 5)
# 
# volume = 0.6
# number = 5
# pi.wave_clear()
# pi.wave_add_generic(flashing1) # 1 s flashes
# f1 = pi.wave_create() # create and save id
# 
# pi.wave_send_repeat(f1)
# sleep(1)
# pi.wave_send_repeat(stp)
# for i in range(5):
#     pi.wave_send_repeat(f1)
#     sleep(volume)
#     
#     pi.wave_send_repeat(stp)
#     sleep(1)
pi.wave_tx_stop() # stop waveform

pi.wave_clear() # clear all waveforms
    
