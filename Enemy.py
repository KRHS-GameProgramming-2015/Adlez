import sys, pygame, math, random
from NPC import *
#From Manpac V2

class Enemy(pygame.sprite.Sprite):
    def __init__(self, images, maxSpeed, pos = [0,0]):
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
        
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
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
        self.collideScreen(size)
        
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
        
    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                self.move()
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                selfdidBounceY = True
                self.move()
    
    #def collidePlayer(self, other):
        
    def collideWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.move()
                self.speed = [0,0]
                while self.speed == [0,0]:
                    self.speedx = self.maxSpeed * random.randint(-1,1)
                    self.speedy = self.maxSpeed * random.randint(-1,1)
                    self.speed = [self.speedx, self.speedy]
                return True
        return False
