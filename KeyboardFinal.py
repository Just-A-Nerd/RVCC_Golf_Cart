from gpiozero import PWMLED
import pygame
from pygame.locals import *

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

while not done:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        print("Ending program")
        done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            forwardLed.on()

            if forwardVoltage > 1:
                forwardVoltage = 1

            forwardLed.value = forwardVoltage
            print("w pressed")
        if event.key == pygame.K_a:
            leftLed.on()
            print("a pressed")
        if event.key == pygame.K_s:
            forwardLed.off()
            reverseLed.on()
            print("s pressed")
        if event.key == pygame.K_d:
            rightLed.on()
            print("d pressed")

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            forwardLed.off()
            print("w released")
        if event.key == pygame.K_a:
            leftLed.off()
            print("a released")
        if event.key == pygame.K_s:
            reverseLed.off()
            print("s released")
        if event.key == pygame.K_d:
            rightLed.off()
            print("d released")

    pygame.display.flip()
    pygame.event.pump()
