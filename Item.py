import sys, pygame, math
#From Manpac V2

class Item(pygame.sprite.Sprite):
    def __init__(self, image, pos=[0,0], blockSize = 25):
        pygame.sprite.Sprite.__init__(self, self.containers)
        
        self.image = pygame.transform.scale(pygame.image.load(image), [blockSize,blockSize])
        self.rect = self.images[0].get_rect(center = pos)

        self.living = True
        self.kind = "normal"
        
    def update(*args):
        pass
        
class Coin(Item):
    def __init__(self, pos, blockSize):
        Item.__init__(self, "Items/Items Images/coin.png", pos, blockSize)
        self.kind = "coin"
        
class HP(Item):
    def __init__(self, pos, blockSize):
        Item.__init__(self, "Items/Items Images/healthpotion.png", pos, blockSize)
        self.kind = "healthpotion"
