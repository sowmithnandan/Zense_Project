import pygame
import random
pygame.init()
win=pygame.display.set_mode((1423,800))
pygame.display.set_caption("marble shooter")
bg=pygame.image.load('zense_illusion.jpg')
char=pygame.image.load('standing.png')
rightk=[pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]
leftk=[pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]
clock=pygame.time.Clock()
balls=[]
pballs=[]
bulletsound=pygame.mixer.Sound('bullet.wav')
hitsound=pygame.mixer.Sound('hit.wav')
music=pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


class player(object):
	def __init__(self,x,y,width,h):
		self.x=x
		self.y=y
		self.width=width
		self.h=h
		self.vel=22
		self.left=0
		self.right=0
		self.walkcount=0
		self.hitbox=(self.x+20,self.y,28,60)
	def draw(self,win):
		if len(balls)!=0:
			mini=least_height_ball(balls)
			if mini.h1==1:					
				if mini.xc+(mini.width/2)>mrbubble.x+(mrbubble.width/2):
					if mrbubble.x<1423-mrbubble.width-mrbubble.vel:
						mrbubble.x+=mrbubble.vel
						mrbubble.right =1
						mrbubble.left= 0
					if mini.xc+(mini.width/2)-2<mrbubble.x:
						if len(bullets)==0:
							bullet=bulle_t(mrbubble.xmrbubble.width,mrbubble.y)
							bullets.append(bullet)
							bulletsound.play()
								
				if mini.xc+(mini.width/2)<mrbubble.x+(mrbubble.width/2):
					if mrbubble.x>mrbubble.vel:
						mrbubble.x-=mrbubble.vel
						mrbubble.left=1
						mrbubble.right=0
					if mrbubble.x+(mrbubble.width)<mini.xc+(mini.width):
						if len(bullets)==0:
							bullet=bulle_t(mrbubble.x+mrbubble.width,mrbubble.y)
							bullets.append(bullet)
							bulletsound.play()
																
		
			else:
					
				if mini.xc+(mini.width/2)>mrbubble.x+(mrbubble.width/2):
					if mrbubble.x<1423-mrbubble.width-mrbubble.vel:
						mrbubble.x+=mrbubble.vel
						mrbubble.right =1
						mrbubble.left= 0
					if mini.xc<mrbubble.x:
						if len(bullets)==0:
							bullet=bulle_t(mrbubble.x,mrbubble.y)
							bullets.append(bullet)
							bulletsound.play()
							print("123")	
				if mini.xc+(mini.width/2)<mrbubble.x+(mrbubble.width/2):
					if mrbubble.x>mrbubble.vel:
						mrbubble.x-=mrbubble.vel
						mrbubble.left=1
						mrbubble.right=0
					if mrbubble.x+(mrbubble.width)<mini.xc+(mini.width/2)+4:
						if len(bullets)==0:
							bullet=bulle_t(mrbubble.x-5,mrbubble.y)
							bullets.append(bullet)
							bulletsound.play()
								
			
		if self.walkcount>=26:
			self.walkcount=0
		if self.right==1:
			win.blit(rightk[((self.walkcount%26)/3)],(self.x,self.y))
			self.walkcount+=1
		elif self.left==1:
			win.blit(leftk[self.walkcount/3],(self.x,self.y))
			self.walkcount+=1
		else:
			win.blit(char,(self.x,self.y))
			self.walkcount=0
		self.hitbox=(self.x+17,self.y+12,33,63)
		#pygame.draw.rect(win,(0,0,0),self.hitbox,2)
	def hit(self):
		run=False

def createballclasses(x,y,h,w,i,l):
	if balls[i][l].divisionofballs==True:
		if len(bullets)!=0:
			del bullets[0]
		balls[i].append(rectangles(x,y,h-30,w-30))
		balls[i][l+1].listchecker=l+1
		balls[i].append(rectangles(x,y,h-30,w-30))
		balls[i][l+2].listchecker=l+2
		balls[i][l+1].ballvel=6
		balls[i][l+2].ballvel=6
		balls[i][l+1].h1=-balls[i][l+2].h1
		balls[i][l].divisionofballs=False
		balls[i][l].parameter=1
	
def createnewballclasses(i,l):
	if balls[i][l].divisionofballs==True:
		pballs.append(1)
		x=random.randint(70,1350)
		l1=[]
		l1.append(rectangles(x,10,100,100))
		balls.append(l1)
		balls[i][l].divisionofballs=False
		balls[i][l].parameter=1

class rectangles(object):
	def __init__(self,x1,y1,width,height):
		self.xc=x1
		self.yc=y1
		self.width=width
		self.height=height
		self.colour=(34,34,34)
		self.h1=1
		self.ballvel=0
		self.vballvel=0
		self.v1=1
		self.flag=False
		self.countingvariable=len(pballs)
		self.healthreduce=False
		self.divisionofballs=True
		self.parameter=0
		self.listchecker=0
	def hit(self):
		self.flag=True	
		if len(bullets)!=0:
			del bullets[0]
		bullet_flag=0
	
	def draw(self,win):
		flag=False
		if flag==True:
			mrbubble.hit()
		if self.xc<=0:
			self.h1=1
		if self.xc>=1423-self.width:
			self.h1=-1
		if self.h1==1:
			self.xc=self.xc+self.ballvel
		else:
			self.xc=self.xc-self.ballvel
		if self.yc>=800-self.height :
			self.v1=-1
		if self.vballvel==0:
			self.v1=1
		if self.v1==1:
			self.vballvel+=0.5
			self.yc=self.yc+self.vballvel
		else:
			self.yc=self.yc-self.vballvel
			self.vballvel=self.vballvel-0.5
		if self.flag==False:
			pygame.draw.rect(win,(34,34,34),(self.xc,self.yc,self.width,self.height))
			if len(bullets)!=0:
				if bullets[0].x>=self.xc and bullets[0].x<=self.xc+self.width:
					if bullets[0].y<=self.yc+self.height and bullets[0]. y>=self.yc:
						self.hit()
						
				elif bullets[0].x+10>=self.xc and bullets[0].x+10<=self.xc+self.width:
					if bullets[0].y<=self.yc+self.height and bullets[0].y>=self.yc:
						self.hit()
								
			if  self.xc>=mrbubble.hitbox[0] and self.xc<=(mrbubble.hitbox[0]+mrbubble.hitbox[2]):
				if self.yc+self.height>mrbubble.hitbox[1]:
					flag=True
			if (self.xc+self.width)>=mrbubble.hitbox[0] and (self.xc+self.width)<=mrbubble.hitbox[2]:
				if self.yc+self.height>mrbubble.hitbox[1] :
					flag=True
			if (self.xc+(self.width/2))>=mrbubble.hitbox[0] and (self.xc+(self.width/2))<=mrbubble.hitbox[2]:
				if self.yc+self.height>mrbubble.hitbox[1] :
					flag=True
			if mrbubble.hitbox[0]>=self.xc and mrbubble.hitbox[0]<=(self.xc+self.width):
				if self.yc+self.height>mrbubble.hitbox[1]:
					flag=True
			if (mrbubble.hitbox[0]+mrbubble.hitbox[2])>=self.xc and (mrbubble.hitbox[0]+mrbubble.hitbox[2])<=(self.xc+self.width):
				if self.yc+self.height>mrbubble.hitbox[1]:
					flag=True
			
			if flag==True:
				mrbubble.hit()
		else:	
			if self.width>=100:		
				createballclasses(self.xc,self.yc,self.height,self.width,self.countingvariable,self.listchecker)
			else:
				count=0			
				for i in balls[self.countingvariable]:
					if i.divisionofballs==True:
						count=count+1
				if count==1:
					createnewballclasses(self.countingvariable,self.listchecker)
				else:
					self.divisionofballs=False
min=0
def least_height_ball(l):
	min=-1
	for j in l:
		for i in j:
			if i.divisionofballs==True:
				min=i.yc
				break 
		if  len(j)!=0:
			if min==i.yc:
				break
	for j in l:
		for i in j:
			if i.yc<min and i.divisionofballs==True:
				min=i.yc
	for i in l:
		for j in i:
			if j.yc==min and j.divisionofballs==True:
				return j
				
class bulle_t(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y
		self.width=10
		self.length=10
		self.vel=0
	def draw(self):
		pygame.draw.rect(win,(34,34,34),(self.x,self.y,self.length,self.width))		

bullets=[]
run=True
def GameWindowUpdater():	
	win.blit(bg,(0,0))
	
	mrbubble.draw(win)
	if len(bullets)!=0:
		bullets[0].draw()
		
	for i in balls:
		for j in i:
			j.draw(win)
	pygame.display.update()
l1=[]
mrbubble=player(800,735,64,64)
l1.append(rectangles(100,10,100,100))	
balls.append(l1)

while run:
	clock.tick(54)
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False			
				
	keys=pygame.key.get_pressed()
	if keys[pygame.K_LEFT]and mrbubble.x>mrbubble.vel:
		mrbubble.x-=mrbubble.vel
		mrbubble.left=1
		mrbubble.right=0
	elif keys[pygame.K_RIGHT]and mrbubble.x<1423-mrbubble.width-mrbubble.vel:
		mrbubble.x+=mrbubble.vel
		mrbubble.right =1
		mrbubble.left= 0
	else:
		mrbubble.right=0
		mrbubble.left=0
	if keys[pygame.K_SPACE]:
		if len(bullets)==0:
			bullet=bulle_t(mrbubble.x,mrbubble.y)
			bullets.append(bullet)
			bulletsound.play()
		
	if len(bullets)!=0:
		bullets[0].y=bullets[0].y-70
		if bullets[0].y<=0:
			del bullets[0]
			
				
	GameWindowUpdater()
pygame.quit()
