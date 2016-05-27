import sys, pygame, math
#From Manpac V2

class Item(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], blockSize = 50):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Items/Items Images/healthpotion.png")
        self.image = pygame.transform.scale(self.image, [blockSize/2,blockSize/2])
        self.rect = self.image.get_rect(center = pos)
        self.radius = self.rect.width/2 - 2
        self.living = True
        self.value = 2
        self.kind = "normal"
        
    def update(*args):
        pass
        
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
    
    def update(*args):
        self = args[0]
        self.animate()
