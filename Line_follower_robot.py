from gpiozero import Motor
from time import sleep

motor = Motor(forward=2, backward=3)
motor2 = Motor(forward=4, backward=17)

while True:
    motor.forward()
    sleep(5)
    motor2.forward()
    sleep(5)
