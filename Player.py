import sys, pygame, math
#From Manpac V2

class Player(pygame.sprite.Sprite):
    def __init__(self, maxSpeed, pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        #Images From: URL: http://opengameart.org/content/classic-knight-animated
        
        self.rightImages = [pygame.transform.scale(pygame.image.load("Player/Player Images/walkRight0.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Player/Player Images/walkRight1.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Player/Player Images/walkRight2.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Player/Player Images/walkRight3.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Player/Player Images/walkRight4.png"), [25,25]),
                            pygame.transform.scale(pygame.image.load("Player/Player Images/walkRight5.png"), [25,25])]
                           
        self.leftImages = [pygame.transform.scale(pygame.image.load("Player/Player Images/walkLeft0.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Player/Player Images/walkLeft1.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Player/Player Images/walkLeft2.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Player/Player Images/walkLeft3.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Player/Player Images/walkLeft4.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Player/Player Images/walkLeft5.png"), [25,25])]
                           
        self.upImages = [pygame.transform.scale(pygame.image.load("Player/Player Images/walkUp0.png"), [25,25]),
                         pygame.transform.scale(pygame.image.load("Player/Player Images/walkUp1.png"), [25,25])]
        
        self.downImages = [pygame.transform.scale(pygame.image.load("Player/Player Images/walkDown0.png"), [25,25]),
                           pygame.transform.scale(pygame.image.load("Player/Player Images/walkDown1.png"), [25,25])]
        
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
        self.timerMax = .10* 60
        
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
            print self.frame, self.maxFrame
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
                     
    def go(self, direction):
        if direction == "up":
            self.yDirection = "up"
            self.speedy = -self.maxSpeedy
            self.images = self.upImages
            self.frame = 0
        elif direction == "down":
            self.speedy = self.maxSpeedy
            self.images = self.downImages
            self.frame = 0
        if direction == "right":
            self.speedx = self.maxSpeedx
            self.images = self.rightImages
            self.frame = 0
        elif direction == "left":
            self.speedx = -self.maxSpeedx
            self.images = self.leftImages
            self.frame = 0
            
            
        if direction == "stop up":
            self.speedy = 0
            self.yDirection = "none"
        elif direction == "stop down":
            self.speedy = 0
        if direction == "stop right":
            self.speedx = 0
        elif direction == "stop left":
            self.speedx = 0
        
        print self.maxFrame
        self.maxFrame = len(self.images)-1    
        
            
    def distanceTo(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
        
        
        
            
            

