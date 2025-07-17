from gpiozero import LED
from signal import pause
import time

# leds = LEDBoard(2, 3, 4,1,pwm=True)
# 
# leds.value= (0.1, 0.4, 0.8, 1.0)
led=(1,2,3,4)
for i in led:
    A=LED(i)
    if i < 5:
        A.on()
        time.sleep(2)
        A.off()
        time.sleep(2)
    else:
        i=1