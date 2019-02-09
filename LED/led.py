#Import Files
import RPi.GPIO as GPIO
import time

#GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

#Main
try:
    while True:
        GPIO.output(13, GPIO.LOW)
        GPIO.output(19, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()

