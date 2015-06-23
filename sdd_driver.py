import RPi.GPIO as GPIO
from time import sleep
from sdd import disp_num

GPIO.setmode(GPIO.BCM)

a = 13
b = 5
c = 12
d = 16
e = 21
f = 19
g = 26

pin = [a,b,c,d,e,f,g]

for p in pin:
    GPIO.setup(p,GPIO.OUT)

try:
    for x in range(0,10):
        print x
        sdd.disp_num(x,pin)
        sleep(2)
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()
