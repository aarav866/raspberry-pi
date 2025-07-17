from gpiozero import PWMLED
import time
led=PWMLED(2)
a=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
while True:
    for i in a:
        led.value=i
        print(i)
        time.sleep(2)