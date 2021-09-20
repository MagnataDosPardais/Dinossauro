import pygame
import random
import math

pygame.init()
pygame.font.init()

Window = pygame.display.set_mode([1280,600],pygame.FULLSCREEN)
#Window = pygame.display.set_mode([800,600])

lv = [
	[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,16,16,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,6,6,6,6,6,6,6,6,6,6,6,14,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,3,3,3,3,3,3,14,13,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,10,13,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,3,3,3,3,14,0,0,13,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,10,13,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,5,5,5,12,0,0,0,0,0,0,0,0,0,0,11,5,5,5,5,0,5,5,0,5,5,0,5,5,0,5,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,5,5,5,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,5,12,0,13,3,3,14,0,11,12,0,13,3,3,14,0,0,0,0,0,0,0,3,3,3,3,10,13,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,3,10,0,9,3,5,5,5,5,0,0,0,0,0,11,10,0,0,9,10,0,9,10,0,9,10,0,9,10,0,9,10,0,0,11,5,5,5,5,5,5,5,12,0,0,0,0,0,0,0,11,10,0,0,0,9,12,0,0,0,0,0,0,0,0,0,0,0,11,5,12,0,11,3,3,3,12,0,13,14,0,11,3,3,12,0,13,14,0,0,0,0,0,0,0,9,3,3,3,3,10,13,0],
	[0,0,0,0,0,0,0,0,11,12,0,0,0,11,3,10,0,0,0,3,3,3,3,10,0,0,0,0,11,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,5,12,0,11,3,3,3,5,3,3,3,3,3,12,0,0,11,3,3,3,3,12,0,0,11,5,5,5,5,5,3,3,3,3,3,3,10,13,0],
	[5,5,5,5,5,5,5,5,10,9,12,0,11,3,10,0,0,0,0,3,3,3,10,0,0,0,0,11,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,5,5,5,12,0,11,5,5,5,12,0,0,0,11,3,3,3,5,3,3,3,3,3,3,3,3,3,3,3,12,11,3,3,3,3,3,3,12,11,3,6,6,6,6,6,6,6,6,6,3,3,10,13,0],
	[0,0,0,0,0,0,0,0,0,0,9,5,3,10,0,0,0,0,0,3,3,10,0,5,5,5,5,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,3,10,0,0,9,15,10,0,0,9,3,5,5,15,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0]],

	[['R',[(6,5,1),(7,5,1)]],
	['R',[(13,4,2),(14,3,2)]],
	['Y',[(22,3,1)]],['Y',[(23,3,1)]],
	['R',[(27,5,2),(28,4,2),(29,3,2),(30,2,2)]],
	['R',[(31,2,1),(32,2,1),(33,2,1)]],
	['Y',[(50,3,1),(51,3,1)]],['R',[(53,3,1),(54,3,1)]],['B',[(56,3,1),(56,3,1)]],['Y',[(57,3,0),(58,4,0)]],
	['R',[(50,6,1),(51,6,1),(52,6,1)]],['B',[(54,6,1),(55,6,1),(56,6,1)]],
	['R',[(60,6,1),(61,6,1),(62,6,1)]],
	['B',[(65,3,2),(66,2,2)]],
	['Y',[(78,4,2)]],['Y',[(80,4,0),(81,5,1),(82,4,2)]],['Y',[(83,3,2),(84,3,1),(85,3,0)]],]]

lv1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,13,3,3,12,0,0,0,0,0],
	   [5,5,5,5,5,5,5,5,12,0,13,3,3,5,5,5,5,5],
	   [13,14,13,14,13,14,13,14,13,12,0,13,6,6,6,6,6,6],
	   [11,12,11,12,11,12,11,12,11,3,12,0,0,0,0,0,0,0],
	   [3,3,3,3,3,3,3,3,3,3,3,5,5,5,5,5,5,5]]

indInfoSettings = [0,0,0,0,0,0,0]
infoSettinsg = [
	["Preto","Cinza-Escuro","Cinza-Claro","Branco","Roxo","Azul","Ciano"],
	[True,False],
	["WASD","↑←↓→"],
	["auto","permission","exit"],
	[True,False],
	[False,True],]

def menu():	
	maxButtonsSettings = 5
	acInd = 0
	select = []
	for button in range(maxButtonsSettings):
		select.append([255,255,255])
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
				if event.key == pygame.K_UP:
					acInd -= 1
					if(acInd < 0): acInd = maxButtonsSettings-1
				if event.key == pygame.K_DOWN:
					acInd += 1
					if(acInd > maxButtonsSettings-1): acInd = 0
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 0:
					game(infoSettinsg,indInfoSettings)
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 1:
					settings()
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 2:
					tutorial()
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 3:
					credits()
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 4:
					pygame.quit()
					exit()
		
		Window.fill([80,10,170])
		select = []
		for button in range(maxButtonsSettings):
			select.append([255,255,255])
		select.insert(acInd,[45,0,54])
		
		tit = pygame.font.SysFont("VCR OSD Mono",56,)
		tit = tit.render(f"Dino Runner",True,(255,255,255))
		Window.blit(tit,(1280/2-tit.get_width()/2,50))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Play>",True,select[0])
		Window.blit(b,(1280/2-b.get_width()/2,250))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Settings>",True,select[1])
		Window.blit(b,(1280/2-b.get_width()/2,300))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Tutorial>",True,select[2])
		Window.blit(b,(1280/2-b.get_width()/2,350))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Credits>",True,select[3])
		Window.blit(b,(1280/2-b.get_width()/2,400))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Exit>",True,select[4])
		Window.blit(b,(1280/2-b.get_width()/2,550))

		pygame.display.update()

def game(data,stg):
	class Dino:
		"""docstring for Dino"""
		def __init__(self):
			self.sensorColl = []
			self.sensorObj = []
			self.jump = 0
			self.death = False
			self.allSpr = []
			self.atualSpr = 0
			for s in range(0,1):
				self.allSpr.append((pygame.image.load(f"Dinos/Dino-{s}.png").convert_alpha()))
			self.spr = self.allSpr[self.atualSpr]
			self.pos = [640-pygame.Surface.get_width(self.spr),360]
			self.per = False
			self.exe = True
			self.reseted = False
			self.deltaA = 1
			self.deltaT = 0
			self.deltaG = 46
			self.blindConf = [0,0]
			self.blindDur = 0
			self.light = pygame.image.load("Dinos/lght.png")
			self.light = pygame.transform.scale2x(self.light)
			self.dark = pygame.Surface([1280,600],pygame.SRCALPHA)
			self.dark.fill((0,0,0,255))
			self.lastPos = []
			self.indLP = 0

		def passSprite(self,limit,sen=1):
			self.atualSpr += sen
			if(self.atualSpr > limit): self.atualSpr = 0
			if(self.atualSpr < 0): self.atualSpr = limit
			try:
				self.spr = self.allSpr[self.atualSpr]
			except: pass

		def posSensor(self):
			self.sensorColl = []
			self.sensorObj = []
			self.sensorObj.append(pygame.Surface([55,25],pygame.SRCALPHA)) #Base
			self.sensorObj.append(pygame.Surface([60,20],pygame.SRCALPHA)) #Topo
			self.sensorObj.append(pygame.Surface([15,25],pygame.SRCALPHA)) #Front
			self.sensorObj[0].fill((255,255,0,0)) #Base
			self.sensorObj[1].fill((255,0,255,0)) #Topo
			self.sensorObj[2].fill((0,255,255,0)) #Front	
			self.sensorColl.append(Window.blit(self.sensorObj[0],(self.pos[0]+65,self.pos[1]+56)))
			self.sensorColl.append(Window.blit(self.sensorObj[1],(self.pos[0]+60,self.pos[1]+2)))
			self.sensorColl.append(Window.blit(self.sensorObj[2],(self.pos[0]+120,self.pos[1])))

		def dinoCollision(self,s,listC):
			detectGroup = False
			s = ['B','T','F'].index(s)
			if(self.sensorColl[s].collidelist(listC) != -1):
				detectGroup = True
			return(detectGroup)

		def pulo(self,res,exe,power):
			self.reset = res
			self.deltaA = power
			self.exe = exe
			self.deltaT += 0.02
			self.deltaA += self.deltaT * self.deltaG
			if(self.exe):
				if(self.deltaA > 20):
					self.deltaA = 20
				self.pos[1] += self.deltaA
				self.pos[1] = int(self.pos[1])
			if(self.reset):
				self.deltaA = power
				self.deltaT = 0
				self.reseted = True

		def blindness(self,dur):
			if(self.blindConf[0] == 1):
				if(self.blindConf[1] <= 252):
					self.blindConf[1] += 5
					self.blindDur = dur
				else:
					self.blindConf[0] += 1
					self.blindConf[1] = 252
				self.dark.set_alpha(self.blindConf[1])
				Window.blit(self.dark,(0,0))
				Window.blit(self.light,(self.pos[0]-(self.light.get_width()/2-self.spr.get_width()/2)+30,self.pos[1]-self.deltaA-(self.light.get_height()/2-self.spr.get_height()/2)))
			if(self.blindConf[0] == 2):
				self.blindDur -= 1
				if(self.blindDur < 0):
					self.blindConf[0] += 1
				self.dark.set_alpha(self.blindConf[1])
				Window.blit(self.dark,(0,0))
				Window.blit(self.light,(self.pos[0]-(self.light.get_width()/2-self.spr.get_width()/2)+30,self.pos[1]-self.deltaA-(self.light.get_height()/2-self.spr.get_height()/2)))
			if(self.blindConf[0] == 3):
				if(self.blindConf[1] >= 0):
					self.blindConf[1] -= 5
				else:
					self.blindConf[0] = 0
					self.blindConf[1] = 0
				self.dark.set_alpha(self.blindConf[1])
				Window.blit(self.dark,(0,0))
			if(self.blindConf[0] != 0): return(False)
			else: self.blindConf = [0,0]; self.blindDur = dur; return(True)
		
		def getPos(self):
			self.lastPos.append([int(self.pos[0]),int(self.pos[1])])

		def drawCopycat(self):
			try:
				Window.blit(pygame.image.load("Dinos/Dino-opc.png"),self.lastPos[self.indLP])
				self.indLP += 1
			except:
				pass


	class Scenary:
		"""docstring for Walls"""
		def __init__(self,mapLevel):
			self.pos = [200,0] #400
			self.speed = 0
			self.blocks = []
			self.listWalls = []
			self.mapLevel = mapLevel
			self.bgImages = []
			self.collH = [[],[]] #Horizontal,RED; {[Topo],[Base]}
			self.collV = [] #Vertical,GREEN
			self.collD = [[],[],[]] #Diagonal,BLUE; {[Up],[Down],[Stop]}
			self.atualSpr = 0
			self.spr = 0
			for b in range(1,17):
				try:
					self.blocks.append(pygame.image.load(f"Senario/Chao{b}.png"))
				except:
					self.blocks.append(pygame.image.load(f"Senario/Chao{b}.jpg"))
				try:
					self.bgImages.append(pygame.image.load(f"Senario/Fire/Fogo-{b-1}.png"))
					self.bgImages[b-1] = self.bgImages[b-1].convert_alpha()
					self.bgImages[b-1] = pygame.transform.scale(self.bgImages[b-1],(900,1200))
				except: pass
			self.bar = []
			self.msh = []
			self.logs = []
			for t in ['B','R','Y']:
				self.msh.append([])
				for i in range(1,3):
					self.msh[['B','R','Y'].index(t)].append(pygame.image.load(f"Senario/Mushrooms/Ms-{t}{i}.png"))

		def newMap(self,arrMap): self.mapLevel = arrMap

		def drawFlame(self):
			self.src = self.bgImages[self.atualSpr]
			self.atualSpr += 1
			if(self.atualSpr > 11): self.atualSpr = 0
			Window.blit(self.src,(-560,-430))

		def drawMap(self):
			for yG in range(self.pos[1]//96,self.pos[1]//96+7):
				for xG in range(int(-self.pos[0]//96),int(-self.pos[0]//96+15)):
					try:
						pixel = self.mapLevel[yG][xG]
						src = "Senario/Chao"
						if(pixel != 0):
							try:
								Window.blit(pygame.image.load(f"{src}{pixel}.png"),[self.pos[0]+(xG*96),self.pos[1]+yG*96])
							except:
								Window.blit(pygame.image.load(f"{src}{pixel}.jpg"),[self.pos[0]+(xG*96),self.pos[1]+yG*96])
					except: pass

		def mapColliders(self,posDino):
			self.collH = [[],[],[],[[],[]],[[],[]],[[],[]]] #Horizontal,RED; {[Topo],[Base],[Espinho],[CogumeloY],[CogumeloR]}
			self.collV = [] #Vertical,GREEN
			self.collD = [[],[],[]] #Diagonal,BLUE; {[Up],[Down],[Stop]}
			for yG in range(int(posDino[1]//96-1),int(posDino[1]//96+2)):
				for xG in range(int((-self.pos[0]+posDino[0])//96),int((-self.pos[0]+posDino[0])//96)+3):
					try:
						pixel = self.mapLevel[yG][xG]
						src = "Senario/Chao"
						if(pixel != 0):
							if(pixel == 7 or pixel == 11):
								for a in range(0,96):
									self.collD[0].append(pygame.draw.rect(Window,(0,0,255),[self.pos[0]+(xG*96)+a,self.pos[1]+((yG+1)*96)-a,5,5]))
								self.collH[1].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)],[self.pos[0]+((xG+1)*96),self.pos[1]+((yG+1)*96)],5))
							elif(pixel == 10 or pixel == 14):
								for a in range(0,96):
									self.collD[2].append(pygame.draw.rect(Window,(0,0,255),[self.pos[0]+(xG*96)+a-2,self.pos[1]+((yG+1)*96)-a-2,5,5]))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)],[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)],5))
								self.collH[0].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)],[self.pos[0]+((xG+1)*96),self.pos[1]+(yG*96)],5))
							elif(pixel == 8 or pixel == 12):
								for a in range(0,96):
									self.collD[1].append(pygame.draw.rect(Window,(255,0,255),[self.pos[0]+(xG*96)+a,self.pos[1]+(yG*96)+a,5,5]))
								self.collH[1].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)],[self.pos[0]+((xG+1)*96),self.pos[1]+((yG+1)*96)],5))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)],[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)],5))
								#coll[pixel-1].append(pygame.draw.line(Window,(0,255,0),[xG*96,yG*96],[xG*96,(yG+1)*96],5))
							elif(pixel == 9 or pixel == 13):
								for a in range(0,96):
									self.collD[2].append(pygame.draw.rect(Window,(0,0,255),[self.pos[0]+(xG*96)+a,self.pos[1]+(yG*96)+a,5,5]))
								self.collH[0].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)],[self.pos[0]+((xG+1)*96),self.pos[1]+(yG*96)],5))
								#coll[pixel-1].append(pygame.draw.line(Window,(0,255,0),[xG*96,yG*96],[xG*96,(yG+1)*96],5))
							elif(pixel == 15):
								self.collH[2].append(pygame.draw.line(Window,(255,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)+12],[self.pos[0]+((xG+1)*96),self.pos[1]+(yG*96)+12],5))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96)+3,self.pos[1]+(yG*96)],[self.pos[0]+(xG*96)+3,self.pos[1]+((yG+1)*96)-1],5))
								self.collH[1].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)-4],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+((yG+1)*96)-4],5))
							elif(pixel == 16):
								self.collH[1].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)+6],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+(yG*96)+6],5))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96)+3,self.pos[1]+(yG*96)],[self.pos[0]+(xG*96)+3,self.pos[1]+((yG+1)*96)-1],5))
								self.collH[2].append(pygame.draw.line(Window,(255,255,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)-12],[self.pos[0]+((xG+1)*96),self.pos[1]+((yG+1)*96)-12],5))

							else:
								self.collH[0].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)+6],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+(yG*96)+6],5))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96)+3,self.pos[1]+(yG*96)],[self.pos[0]+(xG*96)+3,self.pos[1]+((yG+1)*96)-1],5))
								self.collH[1].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)-4],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+((yG+1)*96)-4],5))
					except: pass

		def walk(self): self.pos[0] -= self.speed

		def setSpeed(self,s,prog=0):
			if(prog == 0): self.speed = s
			else:
				if(self.speed < s):
					self.speed += prog
				if(self.speed > s):
					self.speed -= (self.speed-s)

		def getCollideList(self,section):
			if(section == 'V'): return(self.collV)
			elif(section == 'H'): return(self.collH)
			elif(section == 'D'): return(self.collD)
			elif(section == 'A'): return([self.collV,self.collH,self.collD])
			return([])

		def setBarreir(self,probC):
			self.bar = []
			#print(probC)
			#print("------------------------------------------")
			for i in range(0,len(probC)):
				self.bar.append([f"{probC[i][0]}{random.randint(1,2)}",random.choice(probC[i][1]),random.randint(0,29)])
			#	print(f"F{i}={self.bar[i]}")
			#	print(f"------------------------------------------")
			return(self.bar)

		def drawBarreir(self,p):
			for b in self.bar:
				#print(f"{b[0][0]+2} > {(-self.pos[0]//96)+p//96} and {b[0][0]+15} < {(-self.pos[0]//96)+p//96}")
				#pygame.draw.rect(Window,(255,0,0),[self.pos[0]+b[1][0]*96,b[1][1]*96,96,5])
				#pygame.draw.rect(Window,(255,0,0),[self.pos[0]+b[1][0]*96+91,b[1][1]*96,5,96])
				#pygame.draw.rect(Window,(255,0,0),[self.pos[0]+b[1][0]*96,b[1][1]*96+91,96,5])
				#pygame.draw.rect(Window,(255,0,0),[self.pos[0]+b[1][0]*96,b[1][1]*96,5,96])
				#print("Rearrenge: {};{};{}".format(b,b[2],self.msh[0]))
				#b = ['B2', (5, 5, 1), 51]
				if((b[1][0]+6 > (-self.pos[0]//96)+p//96) and ((b[1][0]-10 < (-self.pos[0]//96)+p//96))):
					if(b[0] == 'B1'):
						if(b[1][2] == 0):
							self.collH[5][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+58,b[1][1]*96+15+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)+55],5))
						if(b[1][2] == 1):
							self.collH[5][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+55],[self.pos[0]+b[1][0]*96+b[2]+58,(b[1][1]-1)*96+55],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+55-20],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+55+55],5))
						if(b[1][2] == 2):
							self.collH[5][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+58,b[1][1]*96+15+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)+55],5))
					if(b[0] == 'B2'):
						if(b[1][2] == 0):
							self.collH[5][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+42,b[1][1]*96+15+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)-20],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],5))
						if(b[1][2] == 1):
							self.collH[5][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67],[self.pos[0]+b[1][0]*96+b[2]+42,(b[1][1]-1)*96+67],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67-30],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67+46],5))
						if(b[1][2] == 2):
							self.collH[5][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+24-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+42,b[1][1]*96+24-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+24-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+24-(b[1][1]*1.03)+46],5))
					if(b[0] == 'R1'):
						if(b[1][2] == 0):
							self.collH[4][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+43,b[1][1]*96+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+(b[1][1]*1.03)+50],5))	
						if(b[1][2] == 1):
							self.collH[4][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58],[self.pos[0]+b[1][0]*96+b[2]+43,(b[1][1]-1)*96+58],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58-20],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58+50],5))
						if(b[1][2] == 2):
							self.collH[4][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+20-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+43,b[1][1]*96+20-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+20-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+20-(b[1][1]*1.03)+50],5))
					if(b[0] == 'R2'):
						if(b[1][2] == 0):
							self.collH[4][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-5+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+37,b[1][1]*96-5+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-5+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-5+(b[1][1]*1.03)+40],5))
						if(b[1][2] == 1):
							self.collH[4][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+68],[self.pos[0]+b[1][0]*96+b[2]+37,(b[1][1]-1)*96+68],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+68-30],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+68+40],5))
						if(b[1][2] == 2):
							self.collH[4][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+37,b[1][1]*96+22-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)+40],5))
					if(b[0] == 'Y1'):
						if(b[1][2] == 0):
							self.collH[3][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+10+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+55,b[1][1]*96+10+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+55,b[1][1]*96+16-(b[1][1]*1.03)],5))
						if(b[1][2] == 1):
							self.collH[3][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67],[self.pos[0]+b[1][0]*96+b[2]+55,(b[1][1]-1)*96+67],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67-25],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67+41],5))
						if(b[1][2] == 2):
							self.collH[3][0].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+55,b[1][1]*96+16-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)+55],5))
					if(b[0] == 'Y2'):
						if(b[1][2] == 0):
							self.collH[3][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-8+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+35,b[1][1]*96-8+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-8+(b[1][1]*1.03)-30],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-8+(b[1][1]*1.03)+35],5))
						if(b[1][2] == 1):
							self.collH[3][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+70],[self.pos[0]+b[1][0]*96+b[2]+35,(b[1][1]-1)*96+70],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+70-30],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+70+35],5))
						if(b[1][2] == 2):
							self.collH[3][1].append(pygame.draw.line(Window,(255,255,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+35,b[1][1]*96+22-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)+35],5))
		
		def drawMushroon(self,p):
			for b in self.bar:
				if((b[1][0]+6 > (-self.pos[0]//96)+p//96) and ((b[1][0]-10 < (-self.pos[0]//96)+p//96))):
					if(b[0] == 'B1'):
						if(b[1][2] == 0): Window.blit(self.msh[0][0],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)))
						if(b[1][2] == 1): Window.blit(self.msh[0][0],(self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+55))
						if(b[1][2] == 2): Window.blit(self.msh[0][0],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+10-(b[1][1]*1.03)))
					if(b[0] == 'B2'):
						if(b[1][2] == 0): Window.blit(self.msh[0][1],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)))
						if(b[1][2] == 1): Window.blit(self.msh[0][1],(self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67))
						if(b[1][2] == 2): Window.blit(self.msh[0][1],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+24-(b[1][1]*1.03)))
					if(b[0] == 'R1'):
						if(b[1][2] == 0): Window.blit(self.msh[1][0],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+(b[1][1]*1.03)))
						if(b[1][2] == 1): Window.blit(self.msh[1][0],(self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58))
						if(b[1][2] == 2): Window.blit(self.msh[1][0],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+20-(b[1][1]*1.03)))
					if(b[0] == 'R2'):
						if(b[1][2] == 0): Window.blit(self.msh[1][1],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-5+(b[1][1]*1.03)))
						if(b[1][2] == 1): Window.blit(self.msh[1][1],(self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+68))
						if(b[1][2] == 2): Window.blit(self.msh[1][1],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)))
					if(b[0] == 'Y1'):
						if(b[1][2] == 0): Window.blit(self.msh[2][0],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+10+(b[1][1]*1.03)))
						if(b[1][2] == 1): Window.blit(self.msh[2][0],(self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67))
						if(b[1][2] == 2): Window.blit(self.msh[2][0],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)))
					if(b[0] == 'Y2'):
						if(b[1][2] == 0): Window.blit(self.msh[2][1],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-8+(b[1][1]*1.03)))
						if(b[1][2] == 1): Window.blit(self.msh[2][1],(self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+70))
						if(b[1][2] == 2): Window.blit(self.msh[2][1],(self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)))
			#[[(),(),()],[(),()],[(),(),()]]
			#lista{barreiras{coordenadasPossíveis{}}}

		def win(self,marg): return(self.pos[0] <= (-len(self.mapLevel[0])+marg)*96)


	class Pterossaur:
		def __init__(self,y,sp,ran):
			self.pos = [0,y]
			self.speed = sp
			self.tan = 0
			self.closeTan = ran
			self.mR = 0
			self.dead = False
			self.sprIndex = 0
			self.spr = []
			self.collBox = pygame.draw.rect(Window,(0,0,0),[-50,-50,1,1])
			for s in range(1,10):
				self.spr.append(pygame.image.load(f"Dinos/Pterossaur/Pterossaur-{s}.png"))

		def calcAngle(self,target):
			x1,x2 = self.pos[0],target[0]
			y1,y2 = self.pos[1],target[1]
			xf,yf = math.fabs(x1-x2),math.fabs(y1-y2)
			self.tan = yf/xf
			if(y1 >= y2): self.mR = 1
			else: self.mR = -1

		def attack(self):
			if(self.mR == -1):
				xf,yf = self.pos[0]+self.speed,self.pos[1]+(self.tan*self.speed)
			else:
				xf,yf = self.pos[0]+self.speed,self.pos[1]-(self.tan*self.speed)
			self.pos = [xf,yf]

		def drawPter(self):
			if(self.closeTan >= 0): self.closeTan -= 1
			self.collBox = Window.blit(pygame.transform.rotate(self.spr[int(self.sprIndex)],self.mR*self.tan*(180/math.pi)),self.pos)
			self.sprIndex += self.speed/10
			if(self.sprIndex >= 9): self.sprIndex = 0

		def verifyDead(self):
			self.dead = (self.pos[0] > 1290) or ((self.pos[0] < -90) or (self.pos[0] > 620))
			return(self.dead)


	dino = Dino()
	w = Scenary(lv[0])
	w.setBarreir(lv[1])
	clk = pygame.time.Clock()

	dino.lastPos = [[503, 361], [503, 363], [503, 366], [503, 370], [503, 375], [503, 381], [503, 388], [503, 396], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 405], [503, 390], [503, 375], [503, 361], [503, 348], [503, 336], [503, 327], [503, 319], [503, 312], [503, 306], [503, 301], [503, 297], [503, 294], [503, 292], [503, 290], [503, 289], [503, 289], [503, 290], [503, 292], [503, 295], [503, 299], [503, 304], [503, 310], [503, 317], [503, 325], [503, 334], [503, 344], [503, 354], [503, 365], [503, 375], [503, 366], [503, 344], [503, 328], [503, 313], [503, 299], [503, 286], [503, 274], [503, 265], [503, 257], [503, 250], [503, 244], [503, 239], [503, 235], [503, 232], [503, 229], [503, 227], [503, 226], [503, 226], [503, 227], [503, 229], [503, 232], [503, 236], [503, 256], [503, 276], [503, 296], [503, 316], [503, 336], [503, 356], [503, 356], [503, 359], [503, 365], [503, 374], [503, 386], [503, 386], [503, 389], [503, 395], [503, 404], [503, 416], [503, 416], [503, 419], [503, 425], [503, 434], [503, 446], [503, 446], [503, 449], [503, 455], [503, 464], [503, 476], [503, 476], [503, 479], [503, 485], [503, 494], [503, 506], [503, 506], [503, 506], [503, 506], [503, 506], [503, 506], [503, 500], [503, 494], [503, 488], [503, 482], [503, 476], [503, 470], [503, 464], [503, 458], [503, 452], [503, 446], [503, 440], [503, 434], [503, 428], [503, 422], [503, 416], [503, 410], [503, 404], [503, 398], [503, 392], [503, 386], [503, 364], [503, 348], [503, 333], [503, 319], [503, 306], [503, 294], [503, 283], [503, 272], [503, 262], [503, 253], [503, 245], [503, 238], [503, 235], [503, 232], [500, 229], [497, 214], [497, 199], [497, 185], [497, 172], [497, 160], [497, 151], [497, 143], [497, 136], [497, 130], [497, 125], [497, 121], [497, 118], [497, 116], [497, 114], [497, 113], [497, 113], [497, 114], [497, 116], [497, 119], [497, 123], [497, 128], [497, 134], [497, 141], [497, 149], [497, 143], [497, 137], [497, 131], [497, 125], [497, 119], [497, 113], [497, 107], [497, 108], [497, 110], [497, 113], [497, 107], [497, 108], [497, 110], [497, 113], [497, 107], [497, 108], [497, 110], [497, 113], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 117], [497, 118], [497, 120], [497, 123], [497, 127], [497, 132], [497, 138], [497, 145], [497, 153], [497, 162], [497, 172], [497, 183], [497, 195], [497, 195], [497, 196], [497, 198], [497, 201], [497, 205], [497, 210], [497, 216], [497, 216], [497, 216], [497, 201], [497, 186], [497, 172], [497, 161], [497, 151], [497, 142], [497, 134], [497, 127], [497, 121], [497, 116], [497, 112], [497, 109], [497, 107], [497, 105], [497, 104], [497, 104], [497, 105], [497, 107], [497, 110], [497, 114], [497, 119], [497, 125], [497, 132], [497, 140], [497, 149], [497, 159], [497, 169], [497, 180], [497, 187], [497, 169], [497, 151], [497, 134], [497, 118], [497, 103], [497, 89], [497, 76], [497, 64], [497, 53], [497, 43], [497, 34], [497, 26], [497, 19], [497, 12], [497, 6], [497, 1], [497, -2], [497, -4], [497, -5], [497, -5], [497, -4], [497, -2], [497, 0], [497, 3], [497, 7], [497, 12], [497, 17], [497, 23], [497, 30], [497, 38], [497, 47], [497, 57], [497, 68], [497, 80], [497, 93], [497, 107], [497, 122], [497, 138], [497, 154], [497, 171], [497, 189], [497, 208], [497, 228], [497, 248], [497, 268], [497, 288], [497, 308], [497, 328], [497, 348], [497, 368], [497, 388], [497, 408], [497, 428], [497, 448], [497, 468], [497, 488], [497, 505], [497, 502], [497, 487], [497, 472], [497, 458], [497, 445], [497, 433], [497, 422], [497, 412], [497, 402], [497, 393], [497, 385], [497, 378], [497, 375], [497, 373], [497, 371], [497, 370], [497, 370], [497, 371], [497, 373], [497, 376], [497, 380], [497, 385], [497, 391], [497, 398], [497, 406], [497, 400], [497, 394], [497, 388], [497, 382], [497, 376], [497, 370], [497, 364], [497, 358], [497, 352], [497, 346], [497, 340], [497, 334], [497, 328], [497, 322], [497, 316], [497, 310], [497, 304], [497, 298], [497, 292], [497, 286], [497, 280], [497, 274], [497, 268], [497, 262], [497, 256], [497, 250], [497, 244], [497, 238], [497, 232], [497, 226], [497, 220], [497, 214], [497, 208], [497, 202], [497, 196], [497, 190], [497, 184], [497, 178], [497, 172], [497, 166], [497, 160], [497, 154], [497, 148], [497, 142], [497, 136], [497, 130], [497, 124], [497, 118], [497, 112], [497, 113], [497, 107], [497, 108], [497, 110], [497, 113], [497, 107], [497, 108], [497, 110], [497, 113], [497, 107], [497, 108], [497, 110], [497, 113], [497, 115], [497, 118], [497, 115], [491, 100], [491, 86], [491, 73], [491, 61], [491, 50], [491, 40], [491, 33], [491, 27], [491, 22], [491, 18], [491, 15], [491, 13], [491, 11], [491, 10], [491, 10], [491, 11], [491, 13], [491, 16], [491, 20], [491, 25], [491, 31], [491, 38], [491, 46], [491, 55], [491, 65], [491, 75], [491, 86], [491, 98], [491, 111], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 125], [491, 110], [491, 95], [491, 81], [491, 68], [491, 56], [491, 45], [491, 35], [491, 25], [491, 16], [491, 8], [491, 1], [491, -4], [491, -5], [491, -6], [491, -6], [491, -5], [491, -3], [491, 0], [491, 3], [491, 7], [491, 12], [491, 18], [491, 25], [491, 33], [491, 42], [491, 52], [491, 62], [491, 73], [491, 85], [491, 98], [491, 112], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 127], [491, 128], [491, 130], [491, 133], [491, 137], [491, 142], [491, 148], [491, 155], [491, 163], [491, 172], [491, 182], [491, 196], [491, 200], [491, 204], [491, 209], [491, 209], [491, 209], [491, 209], [491, 209], [491, 209], [491, 209], [491, 209], [485, 209], [479, 209], [473, 209], [467, 209], [461, 209], [455, 209], [449, 209], [443, 209], [437, 209], [431, 209]]

	resJump = False
	exeJump = False
	strengthJump = 1
	addStrengthJump = 0
	t = "VIVO"
	s = 6
	blindnessFX = True
	dur = 0
	spawnDelay = 140
	begDead = True
	probability = 230
	run = True
	bgRGB = [(18,18,18),(73,73,73),(165,165,165),(221,221,211),(80,10,170),(0,24,75),(0,130,160)]
	ctrlKeys = [[pygame.K_w,pygame.K_s],[pygame.K_UP,pygame.K_DOWN]]
	ctrlKeys = ctrlKeys[stg[2]]
	#print(f"Key Group = {ctrlKeys[stg[2]]}")

	while(run):
		#print(f"{w.pos[0]} <= {(-len(w.mapLevel[0])+12)*96}")
		if(not(w.win(12))):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						print(dino.lastPos)
						dino.lastPos = []
						run = False
						
			try:
				if(pters.verifyDead()):
					if(spawnDelay <= 0):
						if(random.choice(range(0,probability)) == 0):
							spawnDelay = 140
							pters = Pterossaur(random.randint(5,510),random.randint(6,10),random.randint(40,140))
					else:
						spawnDelay -= 1
			except:
				if(begDead):
					if(spawnDelay <= 0):
						if(random.choice(range(0,probability)) == 0):
							begDead = False
							spawnDelay = 140
							pters = Pterossaur(random.randint(90,510),random.randint(6,10),random.randint(40,140))
					else:
						spawnDelay -= 1

			#dino.passSprite(3)
			w.setSpeed(s)
			if(data[5][stg[5]]):
				Window.fill(bgRGB[stg[0]])
				if(not(begDead)):
					pygame.draw.line(Window,(0,0,255),pters.pos,[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]],width=4)
					pygame.draw.line(Window,(0,0,255),pters.pos,[pters.pos[0],pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
					pygame.draw.line(Window,(0,0,255),[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]],[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
					pygame.draw.line(Window,(0,0,255),[pters.pos[0],pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
			w.mapColliders(dino.pos)
			w.drawBarreir(dino.pos[0])
			if(not(data[5][stg[5]])):
				Window.fill(bgRGB[stg[0]])
			if(data[1][stg[1]]):
				dino.drawCopycat()
			Window.blit(dino.spr,dino.pos)
			if(data[4][stg[4]]):
				w.drawMushroon(dino.pos[0])
				w.drawMap()
				w.drawFlame()
			dino.posSensor()

			try:
				if(pters.closeTan >= 0):
					pters.calcAngle([dino.pos[0]+20,dino.pos[1]+70])
					if(data[5][stg[5]]):
						pygame.draw.line(Window,(175,0,0),[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],[dino.pos[0]+20,dino.pos[1]+70],width=4)
					if(pters.closeTan == 0):
						pters.tan += random.choice([random.randint(-15,-10),random.randint(10,15)])/100
				else:
					pters.attack()
				pters.drawPter()
			except: pass

			vert = w.getCollideList('V')
			horz = w.getCollideList('H')
			diag = w.getCollideList('D')

			key = pygame.key.get_pressed()
			if(key[ctrlKeys[1]] and not(key[ctrlKeys[0]])): dino.deltaG = 138
			else: dino.deltaG = 46

			if(dino.dinoCollision('B',horz[2]) or dino.dinoCollision('T',horz[2]) or (dino.pos[0] <= 220 or\
				dino.pos[1] >= 600)):
				t = "MORTO"
				pygame.time.delay(1000)
				run = False
			if(not(begDead)):
				if(dino.dinoCollision('B',[pters.collBox]) or dino.dinoCollision('F',[pters.collBox]) or dino.dinoCollision('T',[pters.collBox])):
					pygame.time.delay(1000)
					run = False


			if(dino.dinoCollision('F',vert) or dino.dinoCollision('F',diag[2])):
				dino.pos[0] -= w.speed
			else:
				if(not(dino.exe)): addStrengthJump = 12

			if(dino.dinoCollision('B',diag[0])):
				dino.pos[1] -= int(w.speed*1.03)
				if(not(dino.reseted)): resJump = True
				exeJump = False
				if(not(dino.exe)): strengthJump = 1
			elif(not(dino.dinoCollision('B',horz[0]) or dino.dinoCollision('B',diag[1]) or dino.dinoCollision('B',horz[4][0]) or dino.dinoCollision('B',horz[4][1]) or dino.dinoCollision('B',horz[5][0]) or dino.dinoCollision('B',horz[5][1]))):
				resJump = False
				exeJump = True
				if(not(dino.exe)): strengthJump = 1
			else:
				if(not(dino.reseted)): resJump = True
				exeJump = False
				if(not(dino.exe)): strengthJump = 1
				addStrengthJump = 12
			
			if(not(dino.dinoCollision('T',horz[1]) or dino.dinoCollision('T',horz[0]) or dino.dinoCollision('T',diag[2]) or dino.dinoCollision('F',horz[1]) or dino.dinoCollision('F',diag[2]))):
				if(key[ctrlKeys[0]] and not(key[ctrlKeys[1]])):
					if(not(dino.exe)):
						exeJump = True
						strengthJump = -13
						if(dino.dinoCollision('B',diag[0])): strengthJump = -14
						if(dino.dinoCollision('B',diag[1])): strengthJump = -8
					if(addStrengthJump > 0):
						dino.pos[1] -= 2.5
						addStrengthJump -= 1		
				else:
					addStrengthJump = 12
			else:
				resJump = True
				exeJump = True
				strengthJump = 4

			if(dino.dinoCollision('B',horz[3][0])):
				dino.exe = False
				resJump = True
				exeJump = True
				strengthJump = -18
			elif(dino.dinoCollision('B',horz[3][1])):
				dino.exe = False
				resJump = True
				exeJump = True
				strengthJump = -12

			if(dino.dinoCollision('B',horz[4][0])):
				dino.pos[0] -= s*0.5
			elif(dino.dinoCollision('B',horz[4][1])):
				dino.pos[0] -= s*0.25

			if(dino.dinoCollision('B',horz[5][0]) and blindnessFX):
				dino.blindConf[0] = 1
				dur = 150
			elif(dino.dinoCollision('B',horz[5][1]) and blindnessFX):
				dino.blindConf[0] = 1
				dur = 80
			
			blindnessFX = dino.blindness(dur)
			dino.pulo(resJump,exeJump,strengthJump)
			dino.reseted = False
			dino.getPos()
			w.walk()
			clk.tick(30)
			pygame.display.update()

		else:
			print(dino.lastPos)
			dino.lastPos = []
			run = False

def settings():
	maxButtonsSettings = 7
	runSettings = True
	acIndSettings = 0
	selectSettings = []
	for button in range(maxButtonsSettings):
		selectSettings.append([255,255,255])
	while(runSettings):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if(((event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndSettings == 6) or event.key == pygame.K_ESCAPE):
					runSettings = False

				if event.key == pygame.K_UP:
					acIndSettings -= 1
					if(acIndSettings < 0): acIndSettings = maxButtonsSettings-1
				if event.key == pygame.K_DOWN:
					acIndSettings += 1
					if(acIndSettings > maxButtonsSettings-1): acIndSettings = 0
				
				if(acIndSettings == 0):
					if(event.key == pygame.K_LEFT):
						indInfoSettings[0] -= 1
						if(indInfoSettings[0] < 0): indInfoSettings[0] = 6
					if(event.key == pygame.K_RIGHT):
						indInfoSettings[0] += 1
						if(indInfoSettings[0] > 6): indInfoSettings[0] = 0
				if(acIndSettings == 1):
					if(event.key == pygame.K_LEFT):
						indInfoSettings[1] -= 1
						if(indInfoSettings[1] < 0): indInfoSettings[1] = 1
					if(event.key == pygame.K_RIGHT):
						indInfoSettings[1] += 1
						if(indInfoSettings[1] > 1): indInfoSettings[1] = 0
				if(acIndSettings == 2):
					if(event.key == pygame.K_LEFT):
						indInfoSettings[2] -= 1
						if(indInfoSettings[2] < 0): indInfoSettings[2] = 1
					if(event.key == pygame.K_RIGHT):
						indInfoSettings[2] += 1
						if(indInfoSettings[2] > 1): indInfoSettings[2] = 0
				if(acIndSettings == 3):
					if(event.key == pygame.K_LEFT):
						indInfoSettings[3] -= 1
						if(indInfoSettings[3] < 0): indInfoSettings[3] = 2
					if(event.key == pygame.K_RIGHT):
						indInfoSettings[3] += 1
						if(indInfoSettings[3] > 2): indInfoSettings[3] = 0
				if(acIndSettings == 4):
					if(event.key == pygame.K_LEFT):
						indInfoSettings[4] -= 1
						if(indInfoSettings[4] < 0): indInfoSettings[4] = 1
					if(event.key == pygame.K_RIGHT):
						indInfoSettings[4] += 1
						if(indInfoSettings[4] > 1): indInfoSettings[4] = 0
				if(acIndSettings == 5):
					if(event.key == pygame.K_LEFT):
						indInfoSettings[5] -= 1
						if(indInfoSettings[5] < 0): indInfoSettings[5] = 1
					if(event.key == pygame.K_RIGHT):
						indInfoSettings[5] += 1
						if(indInfoSettings[5] > 1): indInfoSettings[5] = 0

		
		Window.fill([80,10,170])

		selectSettings = []
		for button in range(maxButtonsSettings):
			selectSettings.append([255,255,255])
		selectSettings.insert(acIndSettings,[45,0,54])

		tit = pygame.font.SysFont("VCR OSD Mono",48,)
		tit = tit.render(f"Settings",True,(255,255,255))
		Window.blit(tit,(1280/2-tit.get_width()/2,50))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<BackGround Color: {infoSettinsg[0][indInfoSettings[0]]}>",True,selectSettings[0])
		Window.blit(b,(1280/2-b.get_width()/2,250))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Shadow Clone: {infoSettinsg[1][indInfoSettings[1]]}>",True,selectSettings[1])
		Window.blit(b,(1280/2-b.get_width()/2,300))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Act Key: {infoSettinsg[2][indInfoSettings[2]]}>",True,selectSettings[2])
		Window.blit(b,(1280/2-b.get_width()/2,350))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Pass Level: {infoSettinsg[3][indInfoSettings[3]]}>",True,selectSettings[3])
		Window.blit(b,(1280/2-b.get_width()/2,400))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Draw map: {infoSettinsg[4][indInfoSettings[4]]}>",True,selectSettings[4])
		Window.blit(b,(1280/2-b.get_width()/2,450))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Draw colliders: {infoSettinsg[5][indInfoSettings[5]]}>",True,selectSettings[5])
		Window.blit(b,(1280/2-b.get_width()/2,500))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Exit>",True,selectSettings[6])
		Window.blit(b,(1280/2-b.get_width()/2,550))

		pygame.display.update()

def tutorial():
	
	def ctrl():
		runCtrl = True
		sld = 0
		videoInd = 0
		while(runCtrl):
			Window.fill([80,10,170])
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.KEYDOWN:
					if(((event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndTutorial == 3) or event.key == pygame.K_ESCAPE):
						runCtrl = False
					if(event.key == pygame.K_LEFT):
						sld -= 1
						videoInd = 0
						if(sld < 0): sld = 2
					if(event.key == pygame.K_RIGHT):
						sld += 1
						videoInd = 0
						if(sld > 2): sld = 0

			tit = pygame.font.SysFont("VCR OSD Mono",36,)
			tit = tit.render(f"<Controls>",True,(255,255,255))
			Window.blit(tit,(1280/2-tit.get_width()/2,50))

			if(sld == 0):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Jump:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Button: W or ↑",True,[255,255,255])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 1):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Down:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Button: S or ↓",True,[255,255,255])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 2):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Squat:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Button: S or ↓ (on air)",True,[255,255,255])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))

			pygame.display.update()

	def mush():
		runMush = True
		sld = 0
		videoInd = 0
		while(runMush):
			Window.fill([80,10,170])
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.KEYDOWN:
					if(((event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndTutorial == 3) or event.key == pygame.K_ESCAPE):
						runMush = False
					if(event.key == pygame.K_LEFT):
						sld -= 1
						videoInd = 0
						if(sld < 0): sld = 2
					if(event.key == pygame.K_RIGHT):
						sld += 1
						videoInd = 0
						if(sld > 2): sld = 0

			tit = pygame.font.SysFont("VCR OSD Mono",36,)
			tit = tit.render(f"<Mushrooms>",True,(255,255,255))
			Window.blit(tit,(1280/2-tit.get_width()/2,50))

			if(sld == 0):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Blacks:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Effect: blindness",True,[255,255,255])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 1):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Reds:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Effect: slowness",True,[255,255,255])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 2):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Yellows:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Effect: trampoline",True,[255,255,255])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))

			pygame.display.update()

	def pter():
		runPter = True
		sld = 0
		videoInd = 0
		while(runPter):
			Window.fill([80,10,170])
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.KEYDOWN:
					if(((event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndTutorial == 3) or event.key == pygame.K_ESCAPE):
						runPter = False
					if(event.key == pygame.K_LEFT):
						sld -= 1
						videoInd = 0
						if(sld < 0): sld = 1
					if(event.key == pygame.K_RIGHT):
						sld += 1
						videoInd = 0
						if(sld > 1): sld = 0

			tit = pygame.font.SysFont("VCR OSD Mono",36,)
			tit = tit.render(f"<Pterossaurs>",True,(255,255,255))
			Window.blit(tit,(1280/2-tit.get_width()/2,50))

			if(sld == 0):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Prepair:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"The pterossaur calc the angle of attack",True,[255,255,255])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 1):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Attack:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"The pterossaur move to attack the dino",True,[255,255,255])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))

			pygame.display.update()
	
	maxButtonsTutorial = 4
	runTutorial = True
	acIndTutorial = 0
	selectTutorial = []
	for button in range(maxButtonsTutorial):
		selectTutorial.append([255,255,255])
	while(runTutorial):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if(((event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndTutorial == 3) or event.key == pygame.K_ESCAPE):
					runTutorial = False

				if event.key == pygame.K_UP:
					acIndTutorial -= 1
					if(acIndTutorial < 0): acIndTutorial = maxButtonsTutorial-1
				if event.key == pygame.K_DOWN:
					acIndTutorial += 1
					if(acIndTutorial > maxButtonsTutorial-1): acIndTutorial = 0
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndTutorial == 0:
					ctrl()
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndTutorial == 1:
					mush()
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndTutorial == 2:
					pter()
					
		
		Window.fill([80,10,170])

		selectTutorial = []
		for button in range(maxButtonsTutorial):
			selectTutorial.append([255,255,255])
		selectTutorial.insert(acIndTutorial,[45,0,54])

		tit = pygame.font.SysFont("VCR OSD Mono",48,)
		tit = tit.render(f"Tutorial",True,(255,255,255))
		Window.blit(tit,(1280/2-tit.get_width()/2,50))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Controls>",True,selectTutorial[0])
		Window.blit(b,(1280/2-b.get_width()/2,250))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Mushrooms>",True,selectTutorial[1])
		Window.blit(b,(1280/2-b.get_width()/2,300))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Pterossaurs>",True,selectTutorial[2])
		Window.blit(b,(1280/2-b.get_width()/2,350))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"Exit",True,selectTutorial[3])
		Window.blit(b,(1280/2-b.get_width()/2,550))

		pygame.display.update()

def credits():
	maxButtonsCredits = 7
	runCredits = True
	acIndCredits = 0
	selectCredits = []
	completeCredits = [
	"Idealização: -------------------------> Lucas L. Valenga / Marco A. Z. Bee / Matheus Z. Balbinot",
	"Programação: ------------------------------------------------------> Marco Antônio Zerbielli Bee",
	"Arte: -------------------------------------------------------------> Marco Antônio Zerbielli Bee",
	"Construção de mapas: ----------------------------------------------------> Matheus Zuck Balbinot",
	"Office Boy do lanche: ------------------------------------------------------> Lucas Lodi Valenga",
	"Palpiteiro: -------------------------------------------------------------> Matheus Zuck Balbinot",
	]
	passChar = 1
	for button in range(maxButtonsCredits):
		selectCredits.append([255,255,255])
	while(runCredits):
		selectCredits = []
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if(((event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndCredits == 6) or event.key == pygame.K_ESCAPE):
					runCredits = False
				if event.key == pygame.K_UP:
					acIndCredits -= 1
					if(acIndCredits < 0): acIndCredits = maxButtonsCredits-1
					passChar = 1
				if event.key == pygame.K_DOWN:
					acIndCredits += 1
					if(acIndCredits > maxButtonsCredits-1): acIndCredits = 0
					passChar = 1

		Window.fill([80,10,170])
		
		for button in range(maxButtonsCredits):
			selectCredits.append([255,255,255])
		selectCredits.insert(acIndCredits,[45,0,54])

		tit = pygame.font.SysFont("VCR OSD Mono",48,)
		tit = tit.render(f"Credits",True,(255,255,255))
		Window.blit(tit,(1280/2-tit.get_width()/2,50))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"Idealização: ",True,selectCredits[0])
		Window.blit(b,(25,250))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"Programação: ",True,selectCredits[1])
		Window.blit(b,(25,300))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"Arte: ",True,selectCredits[2])
		Window.blit(b,(25,350))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"Construção de mapas: ",True,selectCredits[3])
		Window.blit(b,(25,400))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"Office Boy do lanche: ",True,selectCredits[4])
		Window.blit(b,(25,450))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"Palpiteiro: ",True,selectCredits[5])
		Window.blit(b,(25,500))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Exit>",True,selectCredits[6])
		Window.blit(b,(25,550))

		if(acIndCredits != 6):
			b = pygame.font.SysFont("VCR OSD Mono",22,)
			b = b.render(f"{completeCredits[acIndCredits][:passChar-1]}",True,selectCredits[acIndCredits])
			Window.blit(b,(25,250+(acIndCredits*50)))
			pygame.time.delay(20)
			b = pygame.font.SysFont("VCR OSD Mono",22,)
			b = b.render(f"{completeCredits[acIndCredits][:passChar]}",True,selectCredits[acIndCredits])
			Window.blit(b,(25,250+(acIndCredits*50)))
			if(passChar <= 95):
				passChar += 1
		pygame.display.update()

menu()