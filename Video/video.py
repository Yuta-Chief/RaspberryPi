#Import Files
import RPi.GPIO as GPIO
import picamera
import time

#GPIO Settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Camera Settings
CAM_DIR  = "/home/pi/python/_video/"

camera = picamera.PiCamera()

#Camera Function
def camera_func(x):
    if GPIO.input(26) == 0:
        filename = time.strftime("%Y%m%d%H%M%S") + ".mjpeg"
        save_dir_filename = CAM_DIR + filename
        GPIO.output(19, GPIO.HIGH)
        camera.start_recording(save_dir_filename)
        camera.wait_recording(30)
        camera.stop_recording()
        GPIO.output(19, GPIO.LOW)
    else:
        GPIO.output(13, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(13, GPIO.LOW)

#Interrupt
GPIO.add_event_detect(26, GPIO.FALLING, callback=camera_func, bouncetime=200)

#Main
try:
    while True:
        pass

except KeyboardInterrupt:
    GPIO.cleanup()

