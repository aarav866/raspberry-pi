from picamera2 import Picamera2, Preview
from time import sleep  
import signal   

picamera = Picamera2()
picamera.start_preview(Preview.QTGL)  # Use DRM preview instead of QTGL
sleep(5)  # Allow time for the preview to start
picamera.start()  # Start the camera
signal.pause()
