import pigpio

#make sure you connect the daemon before you run this program through terminal
#sudo pigpiod

pi = pigpio.pi()

pi.set_mode(26, pigpio.INPUT)
pi.set_mode(12, pigpio.OUTPUT)