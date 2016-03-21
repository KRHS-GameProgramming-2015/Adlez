import pygame, sys, math, random
from Wall import *

class Level():
    def __init__(self, lev):
        #self.loadLevel(lev)
        self.loadAllLevels(lev)
    
    def loadAllLevels(self, lev):
        for fx in range(3):
            for fy in range(3):
                fileName = lev+str(fx+1)+str(fy+1)+".lvl"
                print fileName
                
                blockSize = 10
                screenHeight = 28*blockSize
                screenWidth = 40*blockSize
                
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
                            Wall("wall.png", 
                                 [blockSize*x+blockSize/2+fx*screenWidth,
                                  blockSize*y+blockSize/2]+fy*screenHeight)
                        
                """
if __name__ == "__main__":
    myLev = Level("Levels/Map0")
