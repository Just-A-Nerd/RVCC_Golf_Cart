from gpiozero import LED
from time import sleep
import getch
import time

forwardled = LED(3)
leftled = LED(4)
reverseled = LED(14)
rightled = LED(15)
headlights = LED(17)
taillights = LED(18)

print('Please press a key to see its value')
while 1:
    
        headlights.on()
        taillights.on()
        key = getch.getch()
        if key == 'w':
            forwardled.on()
            sleep(1)
            forwardled.off()
            print('Forward')
        if key == 'a':
            leftled.on()
            sleep(1)
            leftled.off()
            print('Left')
        if key == 's':
            reverseled.on()
            sleep(1)
            reverseled.off()
            print('Reverse')
        if key == 'd':
            rightled.on()
            sleep(1)
            rightled.off()
            print('Right')
        if key == 'h':
            headlights.on()
            sleep(1)
            headlights.off()
        if key == 't':
            taillights.on()
            sleep(1)
            taillights.off()
