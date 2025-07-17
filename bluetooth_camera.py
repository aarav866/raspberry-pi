from bluedot import BlueDot
from gpiozero import LED
from picamera2 import Picamera2
picam2=Picamera2()

bd = BlueDot()
led = LED(2)

while True:
    bd.wait_for_press()
    print("capturing")
    picam2.capture_file('home/pi/photo.jpg')
    bd.wait_for_release()
    led.off()