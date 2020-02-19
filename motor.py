from gpiozero import Motor
import pygame
from pygame.locals import *

motor = Motor(2, 3)
motor.enable()

done = false
while not done:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        done = true
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            motor.value = 0
        if event.key == pygame.K_s:
            motor.value = 0
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            motor.forward()
        elif keys[pygame.K_s]:
            motor.backwards()
        elif keys[pygame.K_SPACE]:
            motor.stop()
