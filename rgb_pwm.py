from gpiozero import PWMLED, Button
import random
import time
import signal
red=PWMLED(2)
green=PWMLED(3)
blue=PWMLED(4)
button=Button(17)
values=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
def change_color ():
    red_pwm=random.choice(values)
    blue_pwm=random.choice(values)
    green_pwm=random.choice(values)
    red.value=red_pwm
    blue.value=blue_pwm
    green.value=green_pwm

button.when_pressed=change_color
signal.pause()