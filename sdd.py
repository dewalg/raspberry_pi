# python 2.7.9
import RPi.GPIO as GPIO

def reset(pin):
    GPIO.output(pin[0], GPIO.LOW)
    GPIO.output(pin[1], GPIO.LOW)
    GPIO.output(pin[2], GPIO.LOW)
    GPIO.output(pin[3], GPIO.LOW)
    GPIO.output(pin[4], GPIO.LOW)
    GPIO.output(pin[5], GPIO.LOW)
    GPIO.output(pin[6], GPIO.LOW)

def disp_num(num, pin):
    if num > 9 or num < 0:
        return 0
    elif len(pin) != 7:
        return 0

    if num == 0:
        reset(pin)
        GPIO.output(pin[0], GPIO.HIGH)
        GPIO.output(pin[1], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
        GPIO.output(pin[3], GPIO.HIGH)
        GPIO.output(pin[4], GPIO.HIGH)
        GPIO.output(pin[5], GPIO.HIGH)
    elif num == 1:
        reset(pin)
        GPIO.output(pin[1], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
    elif num == 2:
        reset(pin)
        GPIO.output(pin[0], GPIO.HIGH)
        GPIO.output(pin[1], GPIO.HIGH)
        GPIO.output(pin[6], GPIO.HIGH)
        GPIO.output(pin[4], GPIO.HIGH)
        GPIO.output(pin[3], GPIO.HIGH)
    elif num == 3:
        reset(pin)
        GPIO.output(pin[0], GPIO.HIGH)
        GPIO.output(pin[1], GPIO.HIGH)
        GPIO.output(pin[6], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
        GPIO.output(pin[3], GPIO.HIGH)
    elif num == 4:
        reset(pin)
        GPIO.output(pin[5], GPIO.HIGH)
        GPIO.output(pin[6], GPIO.HIGH)
        GPIO.output(pin[1], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
    elif num == 5:
        reset(pin)
        GPIO.output(pin[0], GPIO.HIGH)
        GPIO.output(pin[5], GPIO.HIGH)
        GPIO.output(pin[6], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
        GPIO.output(pin[3], GPIO.HIGH)
    elif num == 6:
        reset(pin)
        GPIO.output(pin[5], GPIO.HIGH)
        GPIO.output(pin[4], GPIO.HIGH)
        GPIO.output(pin[6], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
        GPIO.output(pin[3], GPIO.HIGH)
    elif num == 7:
        reset(pin)
        GPIO.output(pin[0], GPIO.HIGH)
        GPIO.output(pin[1], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
    elif num == 8:
        reset(pin)
        GPIO.output(pin[0], GPIO.HIGH)
        GPIO.output(pin[1], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
        GPIO.output(pin[3], GPIO.HIGH)
        GPIO.output(pin[4], GPIO.HIGH)
        GPIO.output(pin[5], GPIO.HIGH)
        GPIO.output(pin[6], GPIO.HIGH)
    elif num == 9:
        reset(pin)
        GPIO.output(pin[0], GPIO.HIGH)
        GPIO.output(pin[1], GPIO.HIGH)
        GPIO.output(pin[2], GPIO.HIGH)
        GPIO.output(pin[5], GPIO.HIGH)
        GPIO.output(pin[6], GPIO.HIGH)

    return 1
