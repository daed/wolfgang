import RPi.GPIO as GPIO
import time

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def button_state():
    input_state = GPIO.input(pin)
    if not input_state:
        return True
    return False
