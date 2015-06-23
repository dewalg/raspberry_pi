# python 2.7.9
import RPi.GPIO as GPIO

def disp_num(num, pin):
    if num > 9 or num < 0:
        return 0
    elif len(pin) != 7:
        return 0

    if num == 0:
        GPIO.output(pin[0])
        GPIO.output(pin[1])
        GPIO.output(pin[2])
        GPIO.output(pin[3])
        GPIO.output(pin[4])
        GPIO.output(pin[5])
    elif num == 1:
        GPIO.output(pin[1])
        GPIO.output(pin[2])
    elif num == 2:
        GPIO.output(pin[0])
        GPIO.output(pin[1])
        GPIO.output(pin[6])
        GPIO.output(pin[4])
        GPIO.output(pin[3])
    elif num == 3:
        GPIO.output(pin[0])
        GPIO.output(pin[1])
        GPIO.output(pin[6])
        GPIO.output(pin[2])
        GPIO.output(pin[3])
    elif num == 4:
        GPIO.output(pin[5])
        GPIO.output(pin[6])
        GPIO.output(pin[1])
        GPIO.output(pin[2])
    elif num == 5:
        GPIO.output(pin[0])
        GPIO.output(pin[5])
        GPIO.output(pin[6])
        GPIO.output(pin[2])
        GPIO.output(pin[3])
    elif num == 6:
        GPIO.output(pin[5])
        GPIO.output(pin[4])
        GPIO.output(pin[6])
        GPIO.output(pin[2])
        GPIO.output(pin[3])
    elif num == 7:
        GPIO.output(pin[0])
        GPIO.output(pin[1])
        GPIO.output(pin[2])
    elif num == 8:
        GPIO.output(pin[0])
        GPIO.output(pin[1])
        GPIO.output(pin[2])
        GPIO.output(pin[3])
        GPIO.output(pin[4])
        GPIO.output(pin[5])
        GPIO.output(pin[6])
    elif num == 9:
        GPIO.output(pin[0])
        GPIO.output(pin[1])
        GPIO.output(pin[2])
        GPIO.output(pin[5])
        GPIO.output(pin[6])
