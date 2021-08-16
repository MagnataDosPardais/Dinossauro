import pygame

Window = pygame.display.set_mode([600,600])

class Dino:
	"""docstring for Dino"""
	def __init__(self):
		self.pos = [0,50]
		self.jump = 0
		self.death = False
		self.ramp = 0 #0:Baixo; 1:Reto; 2:Alto.
		self.speed = 0
		self.allSpr = [[],[],[]]
		self.atualSpr = 0
		for g,i in [['D',0],['S',1],['C',2]]:
			for s in range(0,16):
				try:
					self.allSpr[i].append((pygame.image.load(f"Dinos/Animation/Dino{g}-{s}.png").convert_alpha()))
				except NameError:
					self.allSpr[i].append((pygame.image.load(f"Dinos/Animation/Dino{g}-{s}.jpg").convert_alpha()))
				except: pass
		self.spr = self.allSpr[self.ramp][self.atualSpr]

	def passSprite(self,limit,sen=1):
		self.atualSpr += sen
		if(self.atualSpr > limit): self.atualSpr = 0
		if(self.atualSpr < 0): self.atualSpr = limit
		try:
			self.spr = self.allSpr[self.ramp][self.atualSpr]
		except: pass
	
	def setAlt(self,alt):
		self.ramp = alt
		self.atualSpr = 0
		print(self.allSpr[1])
		self.spr = self.allSpr[self.ramp][self.atualSpr]

	def walk(self):
		self.pos[0] += self.speed
		if(self.ramp == 0): self.pos[1] += self.speed+1
		if(self.ramp == 2): self.pos[1] -= self.speed+1

	def setSpeed(self,s,prog=0):
		if(prog == 0): self.speed = s
		else:
			if(self.speed < s):
				self.speed += prog
			if(self.speed > s):
				self.speed -= (self.speed-s)

	def getCollideBlock(self,listColl,n):
		for b in range(0,n):
			if(collDino.collidelist(listColl[b]) != -1):
				if(b == 7 or b == 11): return([b,2])
				elif(b == 8 or b == 12): return([b,0])
				else: return([b,1])


class Walls:
	"""docstring for Walls"""
	def __init__(self):
		self.blocks = []
		self.collType = []
		for b in range(1,17):
			try:
				self.blocks[b].append(pygame.image.load(f"Senario/Chao{b}.png"))
			except:
				self.blocks[b].append(pygame.image.load(f"Senario/Chao{b}.jpg"))
			if(b >= 1 and b <= 6):	self.collType.append([b,"sqr/UN-GR"])
			if(b == 7 or b == 11):	self.collType.append([b,"trg/BT-GU"])
			if(b == 8 or b == 12):	self.collType.append([b,"trg/TB-GD"])
			if(b == 9 or b == 13):	self.collType.append([b,"trg/TB-AD"])
			if(b == 10 or b == 14):	self.collType.append([b,"trg/BT-AU"])
			if(b == 15):				self.collType.append([b,"sqr/UN-GP"])
			if(b == 16):				self.collType.append([b,"sqr/UN-AP"])

			#---------------------------------------------------------
			#Datasheet do código de ação:
			#"Forma do bloco:{SQuaRe,TRianGle}/
			#Contorno (da colisão): {UNiform,BaseTop,TopBase}-
			#Local de colisão (chão ou teto){Ground,Air}
			#Qual a direção o dinossauro deve tomar{Rect,Up,Down,Perish(morre),Slow}"
			#---------------------------------------------------------



class Senary:
	"""docstring for Senary"""
	def __init__(self,pos,gType):
		pass
		

		
dino = Dino()
dino.setAlt(1)
c = 0

while(True):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				exit()
	Window.fill((0,0,0))
	Window.blit(dino.spr,dino.pos)
	Window.blit(pygame.image.load("Senario/Chao8.png"),[10,75])
	dino.passSprite(14)
	dino.walk()
	dino.setSpeed(5,0.1)
	pygame.time.delay(15)
	c += 1
	pygame.display.update()