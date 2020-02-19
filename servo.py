from gpiozero import servo
import pygame
from pygame.locals import *


screen = pygame.display.set_mode((400, 300))

servo = Servo(17)


done = false
while not done:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        done = true
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            servo.value = 0
        if event.key == pygame.K_s:
            servo.value = 0
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            servo.max()
        elif keys[pygame.K_s]:
            servo.min()
