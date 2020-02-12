from gpiozero import PWMLED
import pygame
from pygame.locals import *
import time
from time import sleep

forwardLed = PWMLED(3)
forwardVoltage = 0

leftLed = PWMLED(4)
leftVoltage = 0

reverseLed = PWMLED(14)
reverseVoltage = 0

rightLed = PWMLED(15)
rightVoltage = 0

screen = pygame.display.set_mode((400, 300))

done = False
increment = 1/15
while not done:
    sleep(1/15)
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        print("Ending program")
        done = True
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            forwardLed.off()
    else:
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            forwardVoltage += increment
            if forwardVoltage > 1:
                forwardVoltage = 1
                print("Brightness limit reached")
            forwardLed.on()
            reverseLed.off()
            forwardLed.value = forwardVoltage
            print("w pressed")
            
        if keys[pygame.K_s]:
            reverseVoltage += increment
            if reverseVoltage > 1:
                reverseVoltage = 1
                print("Brightness limit reached")
            reverseLed.on()
            forwardLed.off()
            reverseLed.value = reverseVoltage
            print("s pressed")
            
        if keys[pygame.K_a]:
            leftVoltage += increment
            if leftVoltage > 1:
                leftVoltage = 1
                print("Brightness limit reached")
            leftLed.on()
            rightLed.off()
            leftLed.value = leftVoltage
            print("a pressed")
            
        if keys[pygame.K_d]:
            rightVoltage += increment
            if rightVoltage > 1:
                rightVoltage = 1
                print("Brightness limit reached")
            rightLed.on()
            leftLed.off()
            rightLed.value = rightVoltage
            print("d pressed")

    # if event.type == pygame.KEYUP:
    #     if event.key == pygame.K_w:
    #         forwardLed.off()
    #         print("w released")
    #     if event.key == pygame.K_a:
    #         leftLed.off()
    #         print("a released")
    #     if event.key == pygame.K_s:
    #         reverseLed.off()
    #         print("s released")
    #     if event.key == pygame.K_d:
    #         rightLed.off()
    #         print("d released")

    pygame.display.flip()
    pygame.event.pump()
