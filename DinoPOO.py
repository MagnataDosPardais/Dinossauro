import pygame
import random
import math
import json
import ast

pygame.init()
pygame.font.init()

class DataBank:
	def __init__(self,fileWay):
		self.fileWay = fileWay
		self.db = 0
		self.dbSTR = ''
		with open(self.fileWay,'r') as self.dbSTR:
			self.db = self.dbSTR.read()
			self.db = ast.literal_eval(self.db)
			self.dbSTR.close()

	def saveValueByKey(self,keyWord,val):
		with open(self.fileWay,'w') as self.dbSTR:
			self.db[keyWord[0]][keyWord[1]] = val
			json.dump(self.db,self.dbSTR, sort_keys=True,indent=4,separators=(",",":"))
			self.dbSTR.close()

	def readValueByKey(self,keyWord): return(self.db[keyWord[0]][keyWord[1]])

	def readValues(self): return(self.db)

dataBank = DataBank("DataBanks/DB_Fix.json")
Window = pygame.display.set_mode([1280,600],pygame.FULLSCREEN)
#Window = pygame.display.set_mode([800,600])
indInfoSettings = dataBank.readValueByKey(["gSystem","Settings"])
infoSettings = [
	["Preto","Cinza-Escuro","Cinza-Claro","Branco","Roxo","Azul","Ciano"],
	["Standart","Gaudélio","Chaves","Mazuttissauro"],
	["WASD","↑←↓→"],
	["auto","exit"],
	[True,False],
	[False,True],
]
lev = 1

def menu():
	global lev
	maxButtonsMenu = 6
	acInd = 0
	select = []
	for button in range(maxButtonsMenu):
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
					if(acInd < 0): acInd = maxButtonsMenu-1
				if event.key == pygame.K_DOWN:
					acInd += 1
					if(acInd > maxButtonsMenu-1): acInd = 0
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 0:
					game(lev,dataBank.readValues(),infoSettings,indInfoSettings,[180,420])
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 1:
					settings()
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 2:
					lev = level(dataBank)
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 3:
					tutorial()
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 4:
					credits()
				if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 5:
					pygame.quit()
					exit()
		
		Window.fill([80,10,170])
		select = []
		for button in range(maxButtonsMenu):
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
		b = b.render(f"<Levels>",True,select[2])
		Window.blit(b,(1280/2-b.get_width()/2,350))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Tutorial>",True,select[3])
		Window.blit(b,(1280/2-b.get_width()/2,400))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Credits>",True,select[4])
		Window.blit(b,(1280/2-b.get_width()/2,450))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Exit>",True,select[5])
		Window.blit(b,(1280/2-b.get_width()/2,550))

		pygame.display.update()

def game(lv,db,data,stg,pSet):
	def passLevel(runPL,beh):
		global lev
		maxButtonsPL = 2
		acInd = 0
		select = []
		runLve = True
		for button in range(maxButtonsPL):
			select.append([255,255,255])
		while(runLve):
			if(runPL and (beh == 0)):
				if(lev <= 2): lev += 1
				runLve = False
				game(lev,dataBank.readValues(),infoSettings,indInfoSettings,[180,420])
			elif(runPL and (beh == 1)):
				runLve = False
				menu()
			elif(not(runPL)):
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
							if(acInd < 0): acInd = maxButtonsPL-1
						if event.key == pygame.K_DOWN:
							acInd += 1
							if(acInd > maxButtonsPL-1): acInd = 0
						if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 0:
							game(lev,dataBank.readValues(),infoSettings,indInfoSettings,[180,420])
						if(event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acInd == 1:
							runLve = False
				
				Window.fill([80,10,170])
				select = []
				for button in range(maxButtonsPL):
					select.append([255,255,255])
				select.insert(acInd,[45,0,54])
				
				tit = pygame.font.SysFont("VCR OSD Mono",48,)
				tit = tit.render(f"Play Again?",True,(255,255,255))
				Window.blit(tit,(1280/2-tit.get_width()/2,50))

				b = pygame.font.SysFont("VCR OSD Mono",22,)
				b = b.render(f"<YES>",True,select[0])
				Window.blit(b,(1280/2-b.get_width()/2,250))

				b = pygame.font.SysFont("VCR OSD Mono",22,)
				b = b.render(f"<NO>",True,select[1])
				Window.blit(b,(1280/2-b.get_width()/2,300))

				pygame.display.update()

	
	class Dino:
		"""docstring for Dino"""
		def __init__(self,sk,beginY):
			self.sensorColl = []
			self.sensorObj = []
			self.jump = 0
			self.death = False
			self.allSpr = []
			self.atualSpr = 1
			for s in range(0,2):
				self.allSpr.append((pygame.image.load(f"Dinos/Dino-{sk}_{s}.png").convert_alpha()))
			self.spr = self.allSpr[self.atualSpr]
			self.pos = [640-pygame.Surface.get_width(self.spr),beginY]
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
			self.indLP = 2

		def getPos(self,axis='a'): 
			if(axis == 'a'): return(self.pos)
			elif(axis == 'x'): return(self.pos[0])
			elif(axis == 'y'): return(self.pos[1])
			else: return([None,None])

		def drawChar(self):
			self.spr = self.allSpr[self.atualSpr]
			Window.blit(self.spr,self.pos)

		def squat(self,do):
			self.atualSpr = do

		def blocked(self,spd):
			self.pos[0] -= spd

		def ramp(self,multiply):
			self.pos[1] -= multiply

		def posSensor(self):
			self.sensorColl = []
			self.sensorObj = []
			self.sensorObj.append(pygame.Surface([55,25],pygame.SRCALPHA)) #Base
			self.sensorObj.append(pygame.Surface([60,10],pygame.SRCALPHA)) #Topo
			self.sensorObj.append(pygame.Surface([15,25],pygame.SRCALPHA)) #Front
			self.sensorObj[0].fill((255,255,0,0)) #Base
			self.sensorObj[1].fill((255,0,255,0)) #Topo
			self.sensorObj[2].fill((0,255,255,0)) #Front	
			self.sensorColl.append(Window.blit(self.sensorObj[0],(self.pos[0]+65,self.pos[1]+56)))
			self.sensorColl.append(Window.blit(self.sensorObj[1],(self.pos[0]+60,self.pos[1]+40+(-self.atualSpr*20))))
			self.sensorColl.append(Window.blit(self.sensorObj[2],(self.pos[0]+120,self.pos[1]+24+(-self.atualSpr*20))))

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

		def isExe(self):
			return(self.exe)

		def setExe(self,bo):
			self.exe = bo

		def isReseted(self):
			return(self.reset)

		def setReseted(self,bo):
			self.reseted = bo

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
		
		def activateBlindness(self):
			self.blindConf[0] = 1


	class Scenary:
		"""docstring for Walls"""
		def __init__(self,mapLevel):
			self.pos = [200,0] #-9500
			self.speed = 0
			self.blocks = []
			self.listWalls = []
			self.mapLevel = mapLevel
			self.bgImages = []
			self.collH = [[],[]] #Horizontal,RED; {[Topo],[Base]}
			self.collV = [] #Vertical,GREEN
			self.collD = [[],[],[]] #Diagonal,BLUE; {[Up],[Down],[Stop]}
			self.atualSpr = 0
			for b in range(1,17):
				try:
					self.blocks.append(pygame.image.load(f"Cenario/Chao{b}.png"))
				except:
					self.blocks.append(pygame.image.load(f"Cenario/Chao{b}.jpg"))
				try:
					self.bgImages.append(pygame.image.load(f"Cenario/Fire/Fogo-{b-1}.png"))
					self.bgImages[b-1] = self.bgImages[b-1].convert_alpha()
					self.bgImages[b-1] = pygame.transform.scale(self.bgImages[b-1],(900,1200))
				except: pass
			self.bar = []
			self.msh = []
			self.logs = []
			for t in ['B','R','Y']:
				self.msh.append([])
				for i in range(1,3):
					self.msh[['B','R','Y'].index(t)].append(pygame.image.load(f"Cenario/Mushrooms/Ms-{t}{i}.png"))
			self.indFlag = 0
			self.flgImg = []
			for f in range(0,4):
				self.flgImg.append(pygame.image.load(f"Cenario/Flag/Flag-{f}.png"))

		def newMap(self,arrMap):
			self.mapLevel = arrMap

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
						if(pixel != 0):
							Window.blit(self.blocks[pixel-1],[self.pos[0]+(xG*96),self.pos[1]+yG*96])
					except: pass

		def mapColliders(self,posDino):
			self.collH = [[],[],[],[[],[]],[[],[]],[[],[]]] #Horizontal,RED; {[Topo],[Base],[Espinho],[CogumeloY],[CogumeloR]}
			self.collV = [] #Vertical,GREEN
			self.collD = [[],[],[]] #Diagonal,BLUE; {[Up],[Down],[Stop]}
			for yG in range(int(posDino[1]//96-1),int(posDino[1]//96+2)):
				for xG in range(int((-self.pos[0]+posDino[0])//96),int((-self.pos[0]+posDino[0])//96)+3):
					try:
						pixel = self.mapLevel[yG][xG]
						src = "Cenario/Chao"
						if(pixel != 0):
							if(pixel == 7 or pixel == 11):
								for a in range(0,96):
									self.collD[0].append(pygame.draw.rect(Window,(0,255,0),[self.pos[0]+(xG*96)+a,self.pos[1]+((yG+1)*96)-a,5,5]))
								self.collH[1].append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)],[self.pos[0]+((xG+1)*96),self.pos[1]+((yG+1)*96)],5))
							elif(pixel == 10 or pixel == 14):
								for a in range(0,96):
									self.collD[2].append(pygame.draw.rect(Window,(0,255,0),[self.pos[0]+(xG*96)+a-2,self.pos[1]+((yG+1)*96)-a-2,5,5]))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)],[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)],5))
								self.collH[0].append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)],[self.pos[0]+((xG+1)*96),self.pos[1]+(yG*96)],5))
							elif(pixel == 8 or pixel == 12):
								for a in range(0,96):
									self.collD[1].append(pygame.draw.rect(Window,(0,255,0),[self.pos[0]+(xG*96)+a,self.pos[1]+(yG*96)+a,5,5]))
								self.collH[1].append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)],[self.pos[0]+((xG+1)*96),self.pos[1]+((yG+1)*96)],5))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)],[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)],5))
								#coll[pixel-1].append(pygame.draw.line(Window,(0,255,0),[xG*96,yG*96],[xG*96,(yG+1)*96],5))
							elif(pixel == 9 or pixel == 13):
								for a in range(0,96):
									self.collD[2].append(pygame.draw.rect(Window,(0,255,0),[self.pos[0]+(xG*96)+a,self.pos[1]+(yG*96)+a,5,5]))
								self.collH[0].append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)],[self.pos[0]+((xG+1)*96),self.pos[1]+(yG*96)],5))
								#coll[pixel-1].append(pygame.draw.line(Window,(0,255,0),[xG*96,yG*96],[xG*96,(yG+1)*96],5))
							elif(pixel == 15):
								self.collH[2].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)+18],[self.pos[0]+((xG+1)*96),self.pos[1]+(yG*96)+18],5))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96)+3,self.pos[1]+(yG*96)],[self.pos[0]+(xG*96)+3,self.pos[1]+((yG+1)*96)-1],5))
								self.collH[1].append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)-4],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+((yG+1)*96)-4],5))
							elif(pixel == 16):
								self.collH[1].append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)+6],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+(yG*96)+6],5))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96)+3,self.pos[1]+(yG*96)],[self.pos[0]+(xG*96)+3,self.pos[1]+((yG+1)*96)-1],5))
								self.collH[2].append(pygame.draw.line(Window,(255,0,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)-12],[self.pos[0]+((xG+1)*96),self.pos[1]+((yG+1)*96)-12],5))

							else:
								self.collH[0].append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+(yG*96)+6],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+(yG*96)+6],5))
								self.collV.append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96)+3,self.pos[1]+(yG*96)],[self.pos[0]+(xG*96)+3,self.pos[1]+((yG+1)*96)-1],5))
								self.collH[1].append(pygame.draw.line(Window,(0,255,0),[self.pos[0]+(xG*96),self.pos[1]+((yG+1)*96)-6],[self.pos[0]+((xG+1)*96)-1,self.pos[1]+((yG+1)*96)-6],5))
					except: pass

		def walk(self):
			self.pos[0] -= self.speed

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
							self.collH[5][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+58,b[1][1]*96+15+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)+55],5))
						if(b[1][2] == 1):
							self.collH[5][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+55],[self.pos[0]+b[1][0]*96+b[2]+58,(b[1][1]-1)*96+55],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+55-20],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+55+55],5))
						if(b[1][2] == 2):
							self.collH[5][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+58,b[1][1]*96+15+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)+55],5))
					if(b[0] == 'B2'):
						if(b[1][2] == 0):
							self.collH[5][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+42,b[1][1]*96+15+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)-20],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+15+(b[1][1]*1.03)],5))
						if(b[1][2] == 1):
							self.collH[5][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67],[self.pos[0]+b[1][0]*96+b[2]+42,(b[1][1]-1)*96+67],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67-30],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67+46],5))
						if(b[1][2] == 2):
							self.collH[5][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+24-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+42,b[1][1]*96+24-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+24-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+24-(b[1][1]*1.03)+46],5))
					if(b[0] == 'R1'):
						if(b[1][2] == 0):
							self.collH[4][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+43,b[1][1]*96+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+(b[1][1]*1.03)+50],5))	
						if(b[1][2] == 1):
							self.collH[4][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58],[self.pos[0]+b[1][0]*96+b[2]+43,(b[1][1]-1)*96+58],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58-20],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+58+50],5))
						if(b[1][2] == 2):
							self.collH[4][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+20-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+43,b[1][1]*96+20-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+20-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+20-(b[1][1]*1.03)+50],5))
					if(b[0] == 'R2'):
						if(b[1][2] == 0):
							self.collH[4][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-5+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+37,b[1][1]*96-5+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-5+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-5+(b[1][1]*1.03)+40],5))
						if(b[1][2] == 1):
							self.collH[4][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+68],[self.pos[0]+b[1][0]*96+b[2]+37,(b[1][1]-1)*96+68],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+68-30],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+68+40],5))
						if(b[1][2] == 2):
							self.collH[4][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+37,b[1][1]*96+22-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)+40],5))
					if(b[0] == 'Y1'):
						if(b[1][2] == 0):
							self.collH[3][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+10+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+55,b[1][1]*96+10+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+55,b[1][1]*96+16-(b[1][1]*1.03)],5))
						if(b[1][2] == 1):
							self.collH[3][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67],[self.pos[0]+b[1][0]*96+b[2]+55,(b[1][1]-1)*96+67],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67-25],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+67+41],5))
						if(b[1][2] == 2):
							self.collH[3][0].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+55,b[1][1]*96+16-(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+16-(b[1][1]*1.03)+55],5))
					if(b[0] == 'Y2'):
						if(b[1][2] == 0):
							self.collH[3][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-8+(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+35,b[1][1]*96-8+(b[1][1]*1.03)],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-8+(b[1][1]*1.03)-30],[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96-8+(b[1][1]*1.03)+35],5))
						if(b[1][2] == 1):
							self.collH[3][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+70],[self.pos[0]+b[1][0]*96+b[2]+35,(b[1][1]-1)*96+70],5))
							self.collV.append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+70-30],[self.pos[0]+b[1][0]*96+b[2],(b[1][1]-1)*96+70+35],5))
						if(b[1][2] == 2):
							self.collH[3][1].append(pygame.draw.line(Window,(0,0,255),[self.pos[0]+b[1][0]*96+b[2],b[1][1]*96+22-(b[1][1]*1.03)],[self.pos[0]+b[1][0]*96+b[2]+35,b[1][1]*96+22-(b[1][1]*1.03)],5))
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
			return(self.pos[0] <= (-len(self.mapLevel[0])+marg)*96)

		def getSpeed(self):
			return(self.speed)

		def drawFlag(self,indXY):
			#if(len(self.mapLevel[0])):
			Window.blit(self.flgImg[int(self.indFlag)],(self.pos[0]+indXY[0]*96+45,indXY[1]*96-60))
			self.indFlag += 0.5
			if(self.indFlag > 3): self.indFlag = 0
			

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

		def getPos(self,axis='a'): 
			if(axis == 'a'): return(self.pos)
			elif(axis == 'x'): return(self.pos[0])
			elif(axis == 'y'): return(self.pos[1])
			else: return([None,None])

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


	skin = range(4)
	skin = skin[stg[1]]
	dino = Dino(skin,db[f"LV{lv}"]["y"])
	w = Scenary(db[f"LV{lv}"]["bg"])
	w.setBarreir(db[f"LV{lv}"]["ms"])
	clk = pygame.time.Clock()

	global lev
	mBehav = range(3)
	mBehav = mBehav[stg[3]]
	resJump = False
	exeJump = False
	strengthJump = 1
	addStrengthJump = 0
	s = 6
	blindnessFX = True
	dur = 0
	spawnDelay = pSet[0]
	begDead = True
	probability = pSet[1]
	run = True
	bgRGB = [(8,8,8),(53,53,53),(165,165,165),(231,231,231),(80,10,170),(0,24,75),(0,130,160)]
	ctrlKeys = [[pygame.K_w,pygame.K_s],[pygame.K_UP,pygame.K_DOWN]]
	ctrlKeys = ctrlKeys[stg[2]]
	levelPass = True
	ply = True

	while(run):
		#print(f"{w.pos[0]} <= {(-len(w.mapLevel[0])+12)*96}")
		if(not(w.win(11)) and ply):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						levelPass = False
						ply = False
						
			try:
				if(pters.verifyDead()):
					if(spawnDelay <= 0):
						if(random.choice(range(0,probability)) == 0):
							spawnDelay = 140
							pters = Pterossaur(random.randint(5,510),random.randint(2,8),random.randint(40,140))
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

			w.setSpeed(s)
			if(data[5][stg[5]]):
				Window.fill(bgRGB[stg[0]])
				if(not(begDead)):
					pygame.draw.line(Window,(255,0,0),pters.pos,[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]],width=4)
					pygame.draw.line(Window,(255,0,0),pters.pos,[pters.pos[0],pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
					pygame.draw.line(Window,(255,0,0),[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]],[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
					pygame.draw.line(Window,(255,0,0),[pters.pos[0],pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],width=4)
			w.mapColliders(dino.getPos())
			w.drawBarreir(dino.getPos('x'))
			if(not(data[5][stg[5]])):
				Window.fill(bgRGB[stg[0]])
			dino.drawChar()
			if(data[4][stg[4]]):
				w.drawFlag(db[f"LV{lv}"]["flag"])
				w.drawMushroon(dino.getPos('x'))
				w.drawMap()
				w.drawFlame()
			dino.posSensor()

			try:
				if(pters.closeTan >= 0):
					pters.calcAngle([dino.getPos('x')+20,dino.getPos('y')+70])
					if(data[5][stg[5]]):
						pygame.draw.line(Window,(175,0,0),[pters.pos[0]+pters.spr[int(pters.sprIndex)].get_width(),pters.pos[1]+pters.spr[int(pters.sprIndex)].get_height()],[dino.pos[0]+20,dino.pos[1]+70],width=4)
					if(pters.closeTan == 0):
						pters.tan += random.choice([random.randint(-25,-20),random.randint(20,25)])/100
				else:
					pters.attack()
				pters.drawPter()
			except: pass

			vert = w.getCollideList('V')
			horz = w.getCollideList('H')
			diag = w.getCollideList('D')

			key = pygame.key.get_pressed()
			if(key[ctrlKeys[1]] and not(key[ctrlKeys[0]])):
				dino.deltaG = 138
			else:
				dino.deltaG = 46

			dino.squat(1)
			if(key[ctrlKeys[1]] and not(key[ctrlKeys[0]])):
				if(not(dino.dinoCollision('B',diag[0]) or dino.dinoCollision('B',horz[0]) or dino.dinoCollision('B',diag[1]) or dino.dinoCollision('B',horz[4][0]) or dino.dinoCollision('B',horz[4][1]) or dino.dinoCollision('B',horz[5][0]) or dino.dinoCollision('B',horz[5][1]))):
					dino.squat(1)
				else:
					dino.squat(0)


			if(dino.dinoCollision('B',horz[2]) or dino.dinoCollision('T',horz[2]) or (dino.getPos('x') <= 220 or\
				dino.getPos('y') >= 600)):
				levelPass = False
				ply = False
			if(not(begDead)):
				if(dino.dinoCollision('B',[pters.collBox]) or dino.dinoCollision('F',[pters.collBox]) or dino.dinoCollision('T',[pters.collBox])):
					pygame.time.delay(100)
					levelPass = False
					ply = False

			if(data[5][stg[5]]):
				pygame.draw.rect(Window,(255,54,0),[210,0,10,600])

			if(dino.dinoCollision('F',vert) or dino.dinoCollision('F',diag[2])):
				dino.blocked(w.getSpeed())
			else:
				if(not(dino.isExe())): addStrengthJump = 12

			if(dino.dinoCollision('B',diag[0])):
				dino.ramp(int(w.getSpeed()*1.03))
				if(not(dino.isReseted())): resJump = True
				exeJump = False
				if(not(dino.isExe())): strengthJump = 1
			elif(not(dino.dinoCollision('B',horz[0]) or dino.dinoCollision('B',diag[1]) or dino.dinoCollision('B',horz[4][0]) or dino.dinoCollision('B',horz[4][1]) or dino.dinoCollision('B',horz[5][0]) or dino.dinoCollision('B',horz[5][1]))):
				resJump = False
				exeJump = True
				if(not(dino.isExe())): strengthJump = 1
			else:
				if(not(dino.isReseted())): resJump = True
				exeJump = False
				if(not(dino.isExe())): strengthJump = 1
				addStrengthJump = 12
			
			if(not(dino.dinoCollision('T',horz[1]) or dino.dinoCollision('T',horz[0]) or dino.dinoCollision('T',diag[2]) or dino.dinoCollision('F',horz[1]) or dino.dinoCollision('F',diag[2]))):
				if(key[ctrlKeys[0]] and not(key[ctrlKeys[1]])):
					if(not(dino.isExe())):
						exeJump = True
						strengthJump = -13
						if(dino.dinoCollision('B',diag[0])): strengthJump = -14
						if(dino.dinoCollision('B',diag[1])): strengthJump = -8
					if(addStrengthJump > 0):
						dino.ramp(2.5)
						addStrengthJump -= 1		
				else:
					addStrengthJump = 12
			else:
				resJump = True
				exeJump = True
				strengthJump = 4

			if(dino.dinoCollision('B',horz[3][0])):
				dino.setExe(False)
				resJump = True
				exeJump = True
				strengthJump = -18
			elif(dino.dinoCollision('B',horz[3][1])):
				dino.setExe(False)
				resJump = True
				exeJump = True
				strengthJump = -12

			if(dino.dinoCollision('B',horz[4][0])):
				dino.blocked(s*0.5)
			elif(dino.dinoCollision('B',horz[4][1])):
				dino.blocked(s*0.25)

			if(dino.dinoCollision('B',horz[5][0]) and blindnessFX):
				dino.activateBlindness()
				dur = 150
			elif(dino.dinoCollision('B',horz[5][1]) and blindnessFX):
				dino.activateBlindness()
				dur = 80
			
			blindnessFX = dino.blindness(dur)
			dino.pulo(resJump,exeJump,strengthJump)
			dino.setReseted(False)
			w.walk()
			clk.tick(30)
			pygame.display.update()

		else:
			run = False
			if(levelPass):
				if(not(lv+1 in db["gSystem"]["unlckLevel"]) and (lv < 3)):
					newLevel = db["gSystem"]["unlckLevel"]
					newLevel.append(lv+1)
					dataBank.saveValueByKey(["gSystem","unlckLevel"],newLevel)
			passLevel(levelPass,mBehav)
			

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
					dataBank.saveValueByKey(["gSystem","Settings"],indInfoSettings)


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
						if(indInfoSettings[1] < 0): indInfoSettings[1] = 3
					if(event.key == pygame.K_RIGHT):
						indInfoSettings[1] += 1
						if(indInfoSettings[1] > 3): indInfoSettings[1] = 0
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
						if(indInfoSettings[3] < 0): indInfoSettings[3] = 1
					if(event.key == pygame.K_RIGHT):
						indInfoSettings[3] += 1
						if(indInfoSettings[3] > 1): indInfoSettings[3] = 0
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
		b = b.render(f"<BackGround Color: {infoSettings[0][indInfoSettings[0]]}>",True,selectSettings[0])
		Window.blit(b,(1280/2-b.get_width()/2,250))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Skin: {infoSettings[1][indInfoSettings[1]]}>",True,selectSettings[1])
		Window.blit(b,(1280/2-b.get_width()/2,300))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Act Key: {infoSettings[2][indInfoSettings[2]]}>",True,selectSettings[2])
		Window.blit(b,(1280/2-b.get_width()/2,350))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Pass Level: {infoSettings[3][indInfoSettings[3]]}>",True,selectSettings[3])
		Window.blit(b,(1280/2-b.get_width()/2,400))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Draw map: {infoSettings[4][indInfoSettings[4]]}>",True,selectSettings[4])
		Window.blit(b,(1280/2-b.get_width()/2,450))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Draw colliders: {infoSettings[5][indInfoSettings[5]]}>",True,selectSettings[5])
		Window.blit(b,(1280/2-b.get_width()/2,500))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Exit>",True,selectSettings[6])
		Window.blit(b,(1280/2-b.get_width()/2,550))

		pygame.display.update()

def level(db):
	global lev
	maxButtonsMap = 3
	runMap = True
	acIndMap = 0
	selectMap = []
	pos = [0,0]
	bgRGB = [(8,8,8),(53,53,53),(165,165,165),(231,231,231),(80,10,170),(0,24,75),(0,130,160)]
	mp = lev
	nMaps = db.readValueByKey([f"LV{mp}","bg"])
	for button in range(maxButtonsMap):
		selectMap.append([255,255,255])
	while(runMap):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
			if event.type == pygame.KEYDOWN:
				if(((event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) and acIndMap == 2) or event.key == pygame.K_ESCAPE):
					runMap = False
				if event.key == pygame.K_UP:
					acIndMap -= 1
					if(acIndMap < 0): acIndMap = maxButtonsMap-1
				if event.key == pygame.K_DOWN:
					acIndMap += 1
					if(acIndMap > maxButtonsMap-1): acIndMap = 0

				if(acIndMap == 0):
					if event.key == pygame.K_LEFT:
						pos[0] = 0
						mp -= 1
						if(mp < 1): mp = 3
					if event.key == pygame.K_RIGHT:
						pos[0] = 0
						mp += 1
						if(mp > 3): mp = 1
		
		key = pygame.key.get_pressed()
		if(key[pygame.K_LEFT] and (acIndMap == 1) and (mp in db.readValueByKey(["gSystem","unlckLevel"]))):
			pos[0] += 30
			if(pos[0] >= 0):
				pos[0] = 0
			pygame.time.delay(75)
		if(key[pygame.K_RIGHT] and (acIndMap == 1) and (mp in db.readValueByKey(["gSystem","unlckLevel"]))):
			pos[0] -= 30
			if(pos[0] <= (-len(db.readValueByKey([f"LV{mp}","bg"])[0])+16)*30):
				pos[0] = (-len(db.readValueByKey([f"LV{mp}","bg"])[0])+16)*30
			pygame.time.delay(75)

		Window.fill([80,10,170])

		selectMap = []
		for button in range(maxButtonsMap):
			selectMap.append([255,255,255])
		selectMap.insert(acIndMap,[45,0,54])

		tit = pygame.font.SysFont("VCR OSD Mono",48,)
		tit = tit.render(f"Levels",True,(255,255,255))
		Window.blit(tit,(1280/2-tit.get_width()/2,50))

		b = pygame.font.SysFont("VCR OSD Mono",26,)
		b = b.render(f"<Map: {mp}>",True,selectMap[0])
		Window.blit(b,(1280/2-b.get_width()/2,250))
		if((mp in db.readValueByKey(["gSystem","unlckLevel"]))):
			pygame.draw.rect(Window,bgRGB[db.readValueByKey(["gSystem","Settings"])[0]],[410,295,455,220])
			for yG in range(pos[1]//30,pos[1]//30+7):
				for xG in range(int(-pos[0]//30),int(-pos[0]//30+15)):
					pixel = db.readValueByKey([f"LV{mp}","bg"])[yG][xG]
					if(pixel != 0):
						try: img = pygame.image.load(f"Cenario/Chao{pixel}.png")
						except: img = pygame.image.load(f"Cenario/Chao{pixel}.jpg")
						Window.blit(pygame.transform.scale(img,[30,30]),[pos[0]+(xG*30)+(1280/2-450/2),pos[1]+yG*30+300])
		else:
			pygame.draw.rect(Window,(0,0,0),[410,295,455,220])
		pygame.draw.rect(Window,(255,255,255),[410,295,455,5])
		pygame.draw.rect(Window,(255,255,255),[410,295,5,220])
		pygame.draw.rect(Window,(255,255,255),[410,510,455,5])
		pygame.draw.rect(Window,(255,255,255),[865,295,5,220])

		if(pos[0] < 0):
			b = pygame.font.SysFont("VCR OSD Mono",42,)
			b = b.render(f"<",True,selectMap[1])
			Window.blit(b,(377,400))
		if((mp in db.readValueByKey(["gSystem","unlckLevel"]))):
			if(pos[0] > (-len(db.readValueByKey([f"LV{mp}","bg"])[0])+16)*30):
				b = pygame.font.SysFont("VCR OSD Mono",42,)
				b = b.render(f">",True,selectMap[1])
				Window.blit(b,(878,400))
		else:
			b = pygame.font.SysFont("VCR OSD Mono",62,)
			b = b.render(f"X",True,selectMap[1])
			Window.blit(b,(1280/2-b.get_width()/2,380))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Exit>",True,selectMap[2])
		Window.blit(b,(1280/2-b.get_width()/2,550))

		pygame.display.update()
	if((mp in db.readValueByKey(["gSystem","unlckLevel"]))):
		return(int(mp))
	else:
		return(lev)

def tutorial():
	
	def ctrl():
		runCtrl = True
		sld = 0
		videos = []
		for n in [["Jump",0],["Down",1],["Squat",2]]:
			videos.append([])
			for f in range(11):
				videos[n[1]].append(f"XYZ/{n[0]}-{f}")
		print(videos)
		rgb = [(45,0,54),(255,255,255)]
		videoInd = 0
		back = 0
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
						if(back): runCtrl = False
						else:
							sld -= 1
							videoInd = 0
							if(sld < 0): sld = 2
					if(event.key == pygame.K_RIGHT):
						if(back): runCtrl = False
						else:
							sld += 1
							videoInd = 0
							if(sld > 2): sld = 0
					if(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
						back = not(back)


			tit = pygame.font.SysFont("VCR OSD Mono",36,)
			tit = tit.render(f"<Controls>",True,(255,255,255))
			Window.blit(tit,(1280/2-tit.get_width()/2,50))

			pygame.draw.rect(Window,(0,255,0),[(1280/2-340/2),300,340,220])
			if(sld == 0):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"<Jump>",True,rgb[back])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Button: W or ↑",True,rgb[back])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))

			if(sld == 1):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"<Down>",True,rgb[back])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Button: S or ↓  (on air)",True,rgb[back])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 2):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"<Squat>",True,rgb[back])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Button: S or ↓",True,rgb[back])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			
			b = pygame.font.SysFont("VCR OSD Mono",22,)
			if(back): b = b.render(f"<Exit>",True,(45,0,54))
			else: b = b.render(f"<Exit>",True,(255,255,255))
			Window.blit(b,(1280/2-b.get_width()/2,550))


			pygame.display.update()

	def mush():
		runMush = True
		sld = 0
		videoInd = 0
		back = False
		rgb = [(45,0,54),(255,255,255)]
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
						if(back): runMush = False
						else:
							sld -= 1
							videoInd = 0
							if(sld < 0): sld = 2
					if(event.key == pygame.K_RIGHT):
						if(back): runMush = False
						else:
							sld += 1
							videoInd = 0
							if(sld > 2): sld = 0
					if(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
						back = not(back)

			tit = pygame.font.SysFont("VCR OSD Mono",36,)
			tit = tit.render(f"<Mushrooms>",True,(255,255,255))
			Window.blit(tit,(1280/2-tit.get_width()/2,50))

			if(sld == 0):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Blacks:",True,rgb[back])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Effect: blindness",True,rgb[back])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 1):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Reds:",True,[255,255,255])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Effect: slowness",True,rgb[back])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 2):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Yellows:",True,rgb[back])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))	
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"Effect: trampoline",True,rgb[back])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))

			b = pygame.font.SysFont("VCR OSD Mono",22,)
			if(back): b = b.render(f"<Exit>",True,(45,0,54))
			else: b = b.render(f"<Exit>",True,(255,255,255))
			Window.blit(b,(1280/2-b.get_width()/2,550))

			pygame.display.update()

	def pter():
		runPter = True
		sld = 0
		videoInd = 0
		back = False
		rgb = [(45,0,54),(255,255,255)]
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
						if(back): runPter = False
						else:
							sld -= 1
							videoInd = 0
							if(sld < 0): sld = 1
					if(event.key == pygame.K_RIGHT):
						if(back): runPter = False
						else:
							sld += 1
							videoInd = 0
							if(sld > 1): sld = 0
					if(event.key == pygame.K_UP or event.key == pygame.K_DOWN):
						back = not(back)

			tit = pygame.font.SysFont("VCR OSD Mono",36,)
			tit = tit.render(f"<Pterossaurs>",True,(255,255,255))
			Window.blit(tit,(1280/2-tit.get_width()/2,50))

			if(sld == 0):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Prepair:",True,rgb[back])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"The pterossaur calc the angle of attack",True,rgb[back])
				Window.blit(ans,(1280/2-ans.get_width()/2,250))
			if(sld == 1):
				subTit = pygame.font.SysFont("VCR OSD Mono",28,)
				subTit = subTit.render(f"Attack:",True,rgb[back])
				Window.blit(subTit,(1280/2-subTit.get_width()/2,200))
				
				ans = pygame.font.SysFont("VCR OSD Mono",22,)
				ans = ans.render(f"The pterossaur move to attack the dino",True,rgb[back])
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
		b = b.render(f"<Exit>",True,selectTutorial[3])
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
	"Arte geral: -------------------------------------------------------> Marco Antônio Zerbielli Bee",
	"Construção de mapas: ----------------------------------> Marco A. Z. Bee / Matheus Zuck Balbinot",
	"Design de Dinossauros: -----------------------------------------------------> Lucas Lodi Valenga",
	"Vídeo-tutoriais: --------------------------------------------------------> Matheus Zuck Balbinot",
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
		b = b.render(f"{completeCredits[0][:completeCredits[0].index(':')+1]}",True,selectCredits[0])
		Window.blit(b,(25,250))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"{completeCredits[1][:completeCredits[1].index(':')+1]}",True,selectCredits[1])
		Window.blit(b,(25,300))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"{completeCredits[2][:completeCredits[2].index(':')+1]}",True,selectCredits[2])
		Window.blit(b,(25,350))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"{completeCredits[3][:completeCredits[3].index(':')+1]}",True,selectCredits[3])
		Window.blit(b,(25,400))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"{completeCredits[4][:completeCredits[4].index(':')+1]}",True,selectCredits[4])
		Window.blit(b,(25,450))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"{completeCredits[5][:completeCredits[5].index(':')+1]}",True,selectCredits[5])
		Window.blit(b,(25,500))

		b = pygame.font.SysFont("VCR OSD Mono",22,)
		b = b.render(f"<Exit>",True,selectCredits[6])
		Window.blit(b,(25,550))

		if(acIndCredits != 6):
			b = pygame.font.SysFont("VCR OSD Mono",22,)
			b = b.render(f"{completeCredits[acIndCredits][:passChar-1]}",True,selectCredits[acIndCredits])
			Window.blit(b,(25,250+(acIndCredits*50)))
			pygame.time.delay(5)
			b = pygame.font.SysFont("VCR OSD Mono",22,)
			b = b.render(f"{completeCredits[acIndCredits][:passChar]}",True,selectCredits[acIndCredits])
			Window.blit(b,(25,250+(acIndCredits*50)))
			if(passChar <= 95):
				passChar += 1
		pygame.display.update()

menu()