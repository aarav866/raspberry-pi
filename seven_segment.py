from gpiozero import LEDCharDisplay
from time import sleep

display = LEDCharDisplay(1, 2, 3, 4, 5, 6, 7, dp=25)

for char in '1':
    display.value = char
    sleep(1)

display.off()