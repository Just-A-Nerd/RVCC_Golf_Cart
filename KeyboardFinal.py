from gpiozero import LED
from gpiozero import Motor
import RPi.GPIO as GPIO
from time import sleep
import getch
import time

forwardled = LED(3)
leftled = LED(4)
reverseled = LED(14)
rightled = LED(15)
headlights = LED(17)
taillights = LED(18)
motor1 = Motor(22,5)

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(14, 50) # GPIO 14 for PWM with 50HZ
p.start(7.5) # Initialization

print('Please press a key to see its value')
while 1:
    
        headlights.on()
        taillights.on()
        key = getch.getch()
        if key == 'w':
            forwardled.on()
            sleep(1)
            forwardled.off()
            motor1.forward(1)
            print('Forward')
        if key == 'a':
            leftled.on()
            sleep(1)
            leftled.off()
            p.ChangeDutyCycle(12.5)
            print('Left')
        if key == 's':
            reverseled.on()
            sleep(1)
            reverseled.off()
            motor1.stop()
            print('Reverse')
        if key == 'd':
            rightled.on()
            sleep(1)
            rightled.off()
            p.ChangeDutyCycle(2.5)
            print('Right')
        if key == 'h':
            headlights.on()
            sleep(1)
            headlights.off()
        if key == 't':
            taillights.on()
            sleep(1)
            taillights.off()
            
GPIO.cleanup()