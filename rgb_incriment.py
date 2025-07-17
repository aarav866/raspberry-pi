from gpiozero import PWMLED, Button
import random
import time
import signal

button=Button(17)
red=PWMLED(2)
green=PWMLED(3)
blue=PWMLED(4)

green.value=1
blue.value=1
red.value=1

def incriment ():
    red.value-=0.1
    
button.when_pressed=incriment
signal.pause()