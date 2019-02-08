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

#Main
try:
    while True:
        time.sleep(0.1)
        if GPIO.input(26) == 0:
            filename = time.strftime("%Y%m%d%H%M%S") + ".jpeg"
            save_dir_filename = CAM_DIR + filename
            cam.capture(save_dir_filename)

except KeyboardInterrupt:
    GPIO.cleanup()
