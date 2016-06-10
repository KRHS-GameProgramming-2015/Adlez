import pygame, sys, math, random, time
from Wall import *
from Sand import *
from Rock import *
from Water import *
from Grass import *
from CaveWall import *
from CaveFloor import *
from HardBlock import *
from SoftBlock import *
from Enemy import *

class Level():
    def __init__(self, lev, sizeX=0, sizeY=0, allLevels = False):
        #self.loadLevel(lev)
        self.start = time.time()

        if allLevels:
            self.loadAllLevels(lev, sizeX, sizeY)
        else:
            self.loadLevel(lev)
    
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
                            Wall([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                        if c == ':':
                            Sand([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                        if c == '=':
                            Water([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                        if c == 'G':
                            Grass([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                        if c == 'g':
                            BigGrass([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize*5)
                        if c == 'c':
                            CaveFloor([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                        if c == 'f':
                            BigCaveFloor([self.blockSize*x+self.blockSize/2,
                                self.blockSize*y+self.blockSize/2],
                                  self.blockSize*5)
                        if c == 'C':
                            CaveWall([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                        if c == 'R':
                            Rock([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
    
    def loadLevel(self, lev):
        now = time.time() - self.start
        self.start = time.time()
        print "before start ", now
        fileName = lev+".lvl"
        print fileName
        
        self.blockSize = 25
        
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

        #for line in lines:
            #print line
            
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == '#':
                    Wall([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize)
                if c == ':':
                    Sand([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize)
                if c == '=':
                    Water([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize)
                if c == 'G':
                    Grass([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize)
                if c == 'g':
                    BigGrass([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize*5)
                if c == 'c':
                    CaveFloor([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize)
                if c == 'f':
                    BigCaveFloor([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize*5)
                if c == 'C':
                    CaveWall([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize)
                if c == 'R':
                    Rock([self.blockSize*x+self.blockSize/2,
                          self.blockSize*y+self.blockSize/2],
                          self.blockSize)
        
        fileName = lev+".ene"
        print fileName
        
        self.blockSize = 25
        
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

        #for line in lines:
            #print line
            
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == 'K':
                    Enemy([5,5], [200,200])
                                  
        now = time.time() - self.start
        self.start = time.time()
        print "after start ", now
if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()

    width = 8*40*3
    height = 8*28*3
    size = width, height

    bgColor = r,b,g = 255,255,255

    screen = pygame.display.set_mode(size)
    
    boundries = pygame.sprite.Group()
    backGrounds = pygame.sprite.Group()
    all = pygame.sprite.OrderedUpdates()
    
    SoftBlock.containers = (boundries, all)
    HardBlock.containers = (boundries, all)
    
    myLev = Level("Levels/map0", 3,3, True)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for s in all.sprites():
                        s.kill()
                    myLev = Level("Levels/map0", 3,3)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
    
