#from gpiozero import LED
import pygame
import * from pygame.locals

import time
from time import sleep

forwardled = LED(3)
leftled = LED(4)
reverseled = LED(14)
rightled = LED(15)

screen = pygame.display.set_mode((400, 300))

done = false
    
while not done: 
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		print("keydown")
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_w:
            forwardled.on()
			print("w pressed")
		if event.key == pygame.K_a:
            leftled.on()
			print("a pressed")
		if event.key == pygame.K_s:
            reverseled.on()
			print("s pressed")
		if event.key == pygame.K_d:
            rightled.on()
			print("d pressed")

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            forwardled.off()
            print("w  released")
        if event.key == pygame.K_a:
            leftled.off()
            print("a released")
        if event.key == pygame.K_s:
            reverseled.off()
            print("s released")
        if event.key == pygame.K_d:
            rightled.off()
            print("d released")
	

	pygame.display.flip()
	pygame.event.pump()
