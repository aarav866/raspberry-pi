# from time import sleep
# from picamera2 import Picamera2, Preview
# picamera = Picamera2()
# picamera.start_preview(Preview.QTGL)
# sleep(5)  # Allow time for the preview to start
# picamera.start()
from time import sleep
from picamera2 import Picamera2, Preview
import signal
picamera = Picamera2()
picamera.start_preview(Preview.DRM)  # Use DRM preview instead of QTGL
sleep(5)  # Allow time for the preview to start
picamera.start()# Keep the script running to maintain the preview
