#Import Files
import RPi.GPIO as GPIO
import picamera
import time

#GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Camera Settings
CAM_DIR  = "/home/pi/python/_photo/"

camera = picamera.PiCamera()

#Camera Function
def camera_func(x):
    if GPIO.input(26) == 0:
        filename = time.strftime("%Y%m%d%H%M%S") + ".jpeg"
        save_dir_filename = CAM_DIR + filename
        camera.capture(save_dir_filename)

#Interrupt
GPIO.add_event_detect(26, GPIO.FALLING, callback=camera_func)

#Main
try:
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()
