""" chrome://dino/ """

import pygame
import math
#import pyautogui
#import typing

pygame.init()
pygame.font.init()

def drawCenary():
	for yG in range(0,len(levelStyle["1"])):
		for xG in range(0,len(levelStyle["1"][yG])):
			pixel = levelStyle["1"][yG][xG]
			src = "Senario/Chao"
			if(pixel != 0):
				try:
					Window.blit(pygame.image.load(f"{src}{pixel}.png"),[xG*96,yG*96])
				except:
					Window.blit(pygame.image.load(f"{src}{pixel}.jpg"),[xG*96,yG*96])
				if(pixel == 7 or pixel == 11):
					coll[pixel-1].append(pygame.draw.line(Window,(255,0,0),[xG*96,(yG+1)*96],[(xG+1)*96,yG*96],5))
				elif(pixel == 8 or pixel == 12):
					coll[pixel-1].append(pygame.draw.line(Window,(255,0,0),[xG*96,yG*96],[(xG+1)*96,(yG+1)*96],5))
					#coll[pixel-1].append(pygame.draw.line(Window,(0,255,0),[xG*96,yG*96],[xG*96,(yG+1)*96],5))
				else:
					coll[pixel-1].append(pygame.draw.line(Window,(255,0,0),[xG*96,yG*96],[(xG+1)*96,yG*96],5))
					coll[pixel-1].append(pygame.draw.line(Window,(0,255,0),[xG*96,yG*96],[xG*96,(yG+1)*96],5))

Window = pygame.display.set_mode([1280,600],pygame.FULLSCREEN)
dinoDir = 1
#imageSize = [70,[616,360]]
#imageSize = [imageSize[0],int(imageSize[0]*(imageSize[1][0]/imageSize[1][1]))]
dinoSpriteR = [[],[pygame.image.load("Dinos/Animation/DinoS-0.png").convert_alpha()],[]]
for i in range(0,16):
	dinoSpriteR[0].append(pygame.image.load(f"Dinos/Animation/DinoD-{i}.png").convert_alpha())
	dinoSpriteR[2].append(pygame.image.load(f"Dinos/Animation/DinoC-{i}.png").convert_alpha())
spr = 0
coll = [[],[],[],[],[],[],[],[],[],[]]
perDown = True
	
levelStyle = {
	"1":[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		 [0, 0, 0, 0, 0, 9, 6, 6, 6, 8, 0, 0, 9, 6],
		 [0, 0, 0, 0, 10, 3, 3, 3, 3, 3, 8, 9, 3, 3],
		 [5, 5, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
		 [3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]
		 #ResMáxima = 14index / 7index#
}
dinoCor = [100,325]
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				exit()

	Window.fill([10,10,170])
	key = pygame.key.get_pressed()
	if(key[ord("w")]):
		dinoCor[1] = dinoCor[1] - 5
	if(perDown):
		dinoCor[1] = dinoCor[1] + 5
	if(key[ord("d")]):
		dinoCor[0] = dinoCor[0] + 5
	if(key[ord("a")]):
		dinoCor[0] = dinoCor[0] - 5

	
	Window.blit(dinoSpriteR[dinoDir][spr],dinoCor)
	drawCenary()
	collDino = pygame.Rect(
	dinoCor,(dinoSpriteR[dinoDir][spr].get_size()[0]-50,dinoSpriteR[dinoDir][spr].get_size()[1]-10))
	#pygame.draw.rect(Window,(255,0,255),collDino)
	perDown = True
	for c in range(0,len(coll)):
		dinoDir = 1
		spr = 0
		if(collDino.collidelist(coll[c]) != -1):
			if(c == 8 or c == 2):
				dinoDir = 2
				spr = 16
				dinoCor[1] = dinoCor[1] - 5
			fonte = pygame.font.get_default_font()
			fontesys = pygame.font.SysFont(fonte, 18)
			txttela = fontesys.render(f"Colidiu[{c+1}]: {dinoCor}", 1, (255,255,255))
			Window.blit(txttela,(20,20))
			perDown = False
			dinoCor[1] = dinoCor[1] - 5


	#dinoCor[0] = dinoCor[0] + 5


	coll = [[],[],[],[],[],[],[],[],[],[]]
	pygame.display.update()



#collidelist
#https://humberto.io/pt-br/blog/desbravando-o-pygame-5-movimento-e-colisao/