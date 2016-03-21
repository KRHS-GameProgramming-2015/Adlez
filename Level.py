import pygame, sys, math, random
from Wall import *

class Level():
    def __init__(self, lev, sizeX, sizeY):
        #self.loadLevel(lev)
        self.loadAllLevels(lev, sizeX, sizeY)
    
    def loadAllLevels(self, lev, sizeX, sizeY):
        for fy in range(sizeY):
            for fx in range(sizeX):
                fileName = lev+str(fy+1)+str(fx+1)+".lvl"
                print fileName
                
                self.blockSize = 8
                screenHeight = 28*self.blockSize
                screenWidth = 40*self.blockSize
                
                file = open(fileName, 'r')
                lines = file.readlines()
                file.close()
                
                newlines = []
                for line in lines:
                    newline = ""
                    for c in line:
                        if c != '\n':
                            newline+= c
                    newlines += [newline]
                lines = newlines

                for line in lines:
                    print line
                    
                for y, line in enumerate(lines):
                    for x, c in enumerate(line):
                        if c == '#':
                            Wall("Block/Block Images/wall.png", 
                                 [self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                        
            
if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()

    width = 8*40*3
    height = 8*28*3
    size = width, height

    bgColor = r,b,g = 255,255,255

    screen = pygame.display.set_mode(size)
    
    boundries = pygame.sprite.Group()
    all = pygame.sprite.OrderedUpdates()
    
    Wall.containers = (boundries, all)
    
    myLev = Level("Levels/Map0", 3,3)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
    