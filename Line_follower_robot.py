from gpiozero import Motor
from time import sleep
from gpiozero import DigitalInputDevice
from signal import pause

# Connect OUT pin of IR sensor to GPIO17
ir = DigitalInputDevice(27)
ir2 = DigitalInputDevice(21)
motor = Motor(forward=2, backward=3)
motor2 = Motor(forward=4, backward=17)
def Forward ():
    motor.forward()
    motor2.forward()
def Backward ():
    motor.backward()
    motor2.backward()
def Left ():
    motor2.forward()
    motor.backward()
def Right ():
    motor2.backward()
    motor.forward()
    
while True:
    if ir2.value == 1 and ir.value==0:
        Left()
    elif ir2.value == 0 and ir.value==1:
        Right()
    elif ir2.value == 0 and ir.value==0:
        Forward()
    elif ir.value == 1 and ir.value == 1:
        motor.stop()
        motor2.stop()

