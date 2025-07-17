from picamera2 import Picamera2
import time

# Initialize camera
picam2 = Picamera2()

# Configure camera for preview (RGB format, 640x480 resolution)
picam2.configure(picam2.create_preview_configuration(main={"format": "RGB888", "size": (640, 480)}))

# Start camera preview
picam2.start()

# Let the preview run for 10 seconds
time.sleep(10)

# Stop camera
picam2.stop()