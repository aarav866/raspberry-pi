from picamera2 import Picamera2,Preview
from time import sleep
from gpiozero import Button
from signal import pause
button=Button(3)
cam=Picamera2()
def start ():
    cam.start_preview(Preview.QTGL)
    cam.start()
    cam.capture_file("photo.jpg")
def stop ():
    cam.stop_preview()
button.when_pressed=start
button.when_released=stop
pause()
