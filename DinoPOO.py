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
['Y',[(78,4,2)]],['Y',[(80,4,0),(81,5,1),(82,4,2)]],['Y',[(83,3,2),(84,3,1),(85,3,0)]],]
]

lv1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	   [0,0,0,0,0,0,0,0,0,13,3,3,12,0,0,0,0,0],
	   [5,5,5,5,5,5,5,5,12,0,13,3,3,5,5,5,5,5],
	   [13,14,13,14,13,14,13,14,13,12,0,13,6,6,6,6,6,6],
	   [11,12,11,12,11,12,11,12,11,3,12,0,0,0,0,0,0,0],
	   [3,3,3,3,3,3,3,3,3,3,3,5,5,5,5,5,5,5]]



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
		self.sensorObj[0].fill((255,255,0,80)) #Base
		self.sensorObj[1].fill((255,0,255,80)) #Topo
		self.sensorObj[2].fill((0,255,255,80)) #Front	
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
			Window.blit(self.light,(dino.pos[0]-(self.light.get_width()/2-dino.spr.get_width()/2)+30,dino.pos[1]-dino.deltaA-(self.light.get_height()/2-dino.spr.get_height()/2)))
		if(self.blindConf[0] == 2):
			self.blindDur -= 1
			if(self.blindDur < 0):
				self.blindConf[0] += 1
			self.dark.set_alpha(self.blindConf[1])
			Window.blit(self.dark,(0,0))
			Window.blit(self.light,(dino.pos[0]-(self.light.get_width()/2-dino.spr.get_width()/2)+30,dino.pos[1]-dino.deltaA-(self.light.get_height()/2-dino.spr.get_height()/2)))
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


class Senary:
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
							self.collH[2].append(pygame.draw.line(Window,(255,255,0),[self.pos[0]+(xG*96)+10,self.pos[1]+(yG*96)+16],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+(yG*96)+16],5))
							self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96)+3,self.pos[1]+(yG*96)],[self.pos[0]+(xG*96)+3,self.pos[1]+((yG+1)*96)-1],5))
							self.collH[1].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)-4],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+((yG+1)*96)-4],5))
						elif(pixel == 16):
							self.collH[1].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)+6],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+(yG*96)+6],5))
							self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96)+3,self.pos[1]+(yG*96)],[self.pos[0]+(xG*96)+3,self.pos[1]+((yG+1)*96)-1],5))
							self.collH[2].append(pygame.draw.line(Window,(255,255,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)-12],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+((yG+1)*96)-12],5))

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
						self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58+50],5))
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

	def win(self,marg):
		return(self.pos[0] <= (-len(self.mapLevel[0])+4)*96)


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
		if((self.pos[0] > 1290) or ((self.pos[0] < -90) or (self.pos[0] > 620))):
			Window.blit(pygame.image.load("Dinos/Animation/DinoD-15.png"),(0,0))
			self.dead = True
		return(self.dead)



dino = Dino()
w = Senary(lv[0])
w.setBarreir(lv[1])
clk = pygame.time.Clock()

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
probability = 50
drawColliders = True

while(True):
	print(f"not({w.pos[0]} <= {(-len(w.mapLevel[0])+4)*96})")
	if(not(w.win(4))):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
		try:
			if(pters.verifyDead()):
				if(spawnDelay <= 0):
					if(random.choice(range(0,100-(probability-1),1)) == 0):
						spawnDelay = 140
						pters = Pterossaur(random.randint(5,510),random.randint(6,10),random.randint(40,140))
				else:
					spawnDelay -= 1
		except:
			if(begDead):
				if(spawnDelay <= 0):
					if(random.choice(range(0,100//probability,1)) == 0):
						begDead = False
						spawnDelay = 90
						pters = Pterossaur(random.randint(5,510),random.randint(6,10),random.randint(40,140))
				else:
					spawnDelay -= 1

		
		key = pygame.key.get_pressed()
		#dino.passSprite(3)
		w.setSpeed(s)
		if(drawColliders):
			Window.fill((0,0,0))
			if(not(begDead)):
				pygame.draw.line(Window,(0,0,255),pters.pos,[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]],width=4)
				pygame.draw.line(Window,(0,0,255),pters.pos,[pters.pos[0],pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
				pygame.draw.line(Window,(0,0,255),[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]],[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
				pygame.draw.line(Window,(0,0,255),[pters.pos[0],pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
		w.mapColliders(dino.pos)
		w.drawBarreir(dino.pos[0])
		if(not(drawColliders)):
			Window.fill((0,0,0))
		Window.blit(dino.spr,dino.pos)
		w.drawMushroon(dino.pos[0])
		w.drawMap()
		dino.posSensor()
		w.drawFlame()

		vert = w.getCollideList('V')
		horz = w.getCollideList('H')
		diag = w.getCollideList('D')

		if(key[pygame.K_DOWN] and not(key[pygame.K_UP])): dino.deltaG = 138
		else: dino.deltaG = 46

		if(dino.dinoCollision('B',horz[2]) or dino.dinoCollision('T',horz[2]) or (dino.pos[0] <= 220 or\
			dino.pos[1] >= 600)):
			t = "MORTO"
			pygame.time.delay(1000)
			pygame.quit()
			exit()
		if(not(begDead)):
			if(dino.dinoCollision('B',[pters.collBox]) or dino.dinoCollision('F',[pters.collBox]) or dino.dinoCollision('T',[pters.collBox])):
				pygame.time.delay(1000)
				pygame.quit()
				exit()


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
			if(key[pygame.K_UP] and not(key[pygame.K_DOWN])):
				if(not(dino.exe)):
					exeJump = True
					strengthJump = -13
					if(dino.dinoCollision('B',diag[0])): strengthJump = -14
					if(dino.dinoCollision('B',diag[1])): strengthJump = -4
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

		try:
			if(pters.closeTan >= 0):
				pters.calcAngle([dino.pos[0]+20,dino.pos[1]+70])
				pygame.draw.line(Window,(175,0,0),[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],[dino.pos[0]+20,dino.pos[1]+70],width=4)
				if(pters.closeTan == 0):
					pters.tan += random.randrange(-104,104)/100
			else:
				pters.attack()
			pters.drawPter()
		except: pass

		w.walk()
		clk.tick(30)
		pygame.display.update()

	else:
		Window.fill([0,255,80])
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
					exit()
		pygame.display.update()
