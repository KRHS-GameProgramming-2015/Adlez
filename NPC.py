import sys, pygame, math

class NPC(pygame.sprite.Sprite):
    def __init__(self, maxSpeed, pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #Images From: URL: http://opengameart.org/content/classic-knight-animated
        playerSize = [25,25]
        self.rightImages = [pygame.transform.scale(pygame.image.load("NPC\NPC Images\walkRight0.png"), playerSize)
                            ]
                           
        self.leftImages = [pygame.transform.scale(pygame.image.load("NPC\NPC Images\walkLeft0.png"), playerSize)
                           ]
                           
        self.upImages = [pygame.transform.scale(pygame.image.load("NPC\NPC Images\walkUp0.png"), playerSize)
                         ]
        
        self.downImages = [pygame.transform.scale(pygame.image.load("NPC\NPC Images\walkDown0.png"), playerSize)
                           ]
        
        
        self.images = self.rightImages
        self.frame = 0
        self.maxFrame = len(self.images)-1
        
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        
        self.xDirection = "right"
        self.yDirection = "none"
        
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        
        self.maxSpeedx = maxSpeed[0]
        self.maxSpeedy = maxSpeed[1]
        
        self.timer = 0
        self.timerMax = .25* 60
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.rect = self.rect.move(pos)
        
        self.living = True
        self.lives = 3
        
        self.score = 0
        
    def die(self):
        self.lives -= 1
        self.lives
        if self.lives <= 0:
            self.living = False

    def update(*args):
        self = args[0]
        size = args[1]
        self.move()
        self.animate()
        self.collideScreen(size)
    
    def collideObject(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceTo(other.rect.center):
                    return True
        return False
    
    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceX:
            if self.rect.center[0] < -1: 
                self.rect.center = (width, self.rect.center[1])
            elif self.rect.center[0] > width+1:
                self.rect.center = (0, self.rect.center[1])
                
    def collideHardblock(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.move()
                self.speedx = 0
                self.speedy = 0
                 
    def animate(self):
        if self.timer < self.timerMax:
            self.timer += 1
        else:
            self.timer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        self.image = self.images[self.frame]
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.didBounceX = False
        self.didBounceY = False 
                     
    def distanceTo(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
        
        
        
            
            

