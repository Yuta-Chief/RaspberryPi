#Import Files
import RPi.GPIO as GPIO
import picamera
import time

#GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Camera Settings
CAM_DIR  = "/home/pi/python/_video/"

camera = picamera.PiCamera()

#Main
try:
    while True:
        if GPIO.input(4) == 1:
            filename = time.strftime("%Y%m%d%H%M%S") + ".h264"
            save_dir_filename = CAM_DIR + filename
            camera.start_recording(save_dir_filename)
            camera.wait_recording(300)
            camera.stop_recording()
        else:
            pass

except KeyboardInterrupt:
    GPIO.cleanup()

