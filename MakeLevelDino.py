""" chrome://dino/ """

import pygame
import os
#import math
#import typing

pygame.init()
pygame.font.init()

Window = pygame.display.set_mode([1280,600],pygame.FULLSCREEN)
dinoSprite = pygame.image.load("Dinos/DinoESSE.png")#.convert_alpha()
#imageSize = [70,[616,360]]
#imageSize = [imageSize[0],int(imageSize[0]*(imageSize[1][0]/imageSize[1][1]))]
dinoSprite = pygame.transform.scale(dinoSprite,(103,60))#616,360(imageSize[1],imageSize[0])
		

mapVetor = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0,0,0,0,0],]
point = [0,0]
block = 1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				os.system("cls")
				print(mapVetor)
				pygame.quit()
				exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			if(event.button == 1):
				mapVetor[pY][pX] = block
			if(event.button == 2):
				mapVetor[pY][pX] = mapVetor[pY][pX] + 1
			if(event.button == 3):
				mapVetor[pY][pX] = 0
			if(event.button == 4):
				block = block - 1
			if(event.button == 5):
				block = block + 1
			if(block < 1):
				block = 16
			if(block > 16):
				block = 1


	Window.fill([80,10,170])
	for yG in range(0,len(mapVetor)):
		for xG in range(0,len(mapVetor[yG])):
			pixel = mapVetor[yG][xG]
			image = [f"Senario/Chao{pixel}.png",f"Senario/Chao{pixel}.jpg"]
			if(pixel != 0):
				try:
					Window.blit(pygame.image.load(image[0]).convert_alpha(),[xG*96,yG*96])
				except:
					Window.blit(pygame.image.load(image[1]).convert(),[xG*96,yG*96])

	point = pygame.mouse.get_pos()
	pX,pY = point
	pX,pY = pX//96,pY//96
	try:
		Window.blit(pygame.image.load(f"Senario/Chao{block}.png"),(pX*96,pY*96))
	except:
		Window.blit(pygame.image.load(f"Senario/Chao{block}.jpg"),(pX*96,pY*96))
	pygame.draw.rect(Window,(255,0,0),[pX*96,pY*96,96,5])
	pygame.draw.rect(Window,(255,0,0),[pX*96+91,pY*96,5,96])
	pygame.draw.rect(Window,(255,0,0),[pX*96,pY*96+91,96,5])
	pygame.draw.rect(Window,(255,0,0),[pX*96,pY*96,5,96])
	

	pygame.display.update()