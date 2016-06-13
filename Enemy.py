import sys, pygame, math, random
from NPC import *
#From Manpac V2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, images, maxSpeed, pos = [200,200]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #Images From: URL: http://opengameart.org/content/ye-oldy-armored-knife-guy-animated
        
        self.rightImages = [pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight0.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight1.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight2.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight3.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight4.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight5.png"), [25,25])]

      
        self.leftImages = [pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight0.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight1.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight2.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight3.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight4.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGRight5.png"), [25,25])]
                           
        self.attackrImages = [pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGAttackR0.png"), [25,25]),
                              pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGAttackR0.png"), [25,25]),
                              pygame.transform.scale(pygame.image.load("Enemy/Enemy Images/KGAttackR0.png"), [25,25])]
                            
        
        self.startPos = pos
        
        self.images = self.rightImages
        self.frame = 0
        self.maxFrame = len(self.images)-1
        
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        
        self.direction = "stop right"

        self.speed = [0,0]
        
        self.maxSpeed = 3
        
        self.timer = 0
        self.timerMax = .10* 60
        
        self.speed = [0,0]
        while self.speed == [0,0]:
            self.speedx = self.maxSpeed * random.randint(-1,1)
            self.speedy = self.maxSpeed * random.randint(-1,1)
            self.speed = [self.speedx, self.speedy]
        
        self.radius = self.rect.width/2 - 2
        self.living = True
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.rect.center = pos
    
    def update(*args):
        self = args[0]
        size = args[1]
        self.move()
        self.animate()
        
    def die(self):
        self.kill()
        self.deadtimer = 1
    
    def move(self):
        if random.randint(0,90) == 0:
            self.speed = [0,0]
            while self.speed == [0,0]:
                self.speedx = self.maxSpeed * random.randint(-1,1)
                self.speedy = self.maxSpeed * random.randint(-1,1)
                self.speed = [self.speedx, self.speedy]
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.didBounceX = False
        self.didBounceY = False
    
    #def collidePlayer(self, other):
        
    def collideHardblock(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.move()
                self.speedx = 0
                self.speedy = 0
                
    def animate(self):
        if self.direction[0:4] == "stop":
            self.frame = 0
        elif self.timer < self.timerMax:
            self.timer += 1
        else:
            self.timer = 0
            #print self.frame, self.maxFrame
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        self.image = self.images[self.frame]
                
    def distanceTo(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
        
