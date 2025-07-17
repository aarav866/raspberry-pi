from gpiozero import InputDevice, LED
from time import sleep
from signal import pause
# Initialize the sensor as a digital input device on GPIO 12
sensor = InputDevice(17)
l_1=LED(1)
l_2=LED(2)
l_3=LED(3)
l_4=LED(4)
a=0
while True:
    if a<5:
        if sensor.is_active:
            print("no obstacle")
        else:
            print("obstacle detected")
            a+=1
            sleep(2)
    else:
        a=0
    if a==1:
        l_1.on()
    elif a==2:
        l_2.on()
    elif a==3:
        l_3.on()

    elif a==4:
        l_4.on()
    else:
        l_1.off()
        l_2.off()
        l_3.off()
        l_4.off()
