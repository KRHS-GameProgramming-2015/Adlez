import sys, pygame, math, random
from Level import *
from Player import *
from NPC import *
from Menu import *
pygame.init()

clock = pygame.time.Clock()

width = 1000
height = 700
size = width, height

bgColor = r,b,g = 255,255,255

screen = pygame.display.set_mode(size)

mode = "test"

boundries = pygame.sprite.Group()
backGrounds = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

SoftBlock.containers = (boundries, all)
HardBlock.containers = (boundries, all)

def loadNewLev(direction):
    if direction == "up":
        if levy >1:
            levy-=1
    for s in all.sprites():
        s.kill()
    levFile = "Levels/map" + str(levLayer) + str(levy) + str(levx) + ".lvl"
    level=Level(levFile) 

while True:
    while mode == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "start"
                if event.key == pygame.K_2:
                    mode = "how to play"
                if event.key == pygame.K_q:
                    mode = "quit"
                    
        bg = pygame.image.load("Resources/mainmenu.png")
        bgrect = bg.get_rect(center = [width/2,height/2])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        pygame.display.flip()
        clock.tick(60)
        
    levLayer =0
    levx = 3
    levy = 3
    levFile = "Levels/map" + str(levLayer) + str(levy) + str(levx) + ".lvl"
    level=Level(levFile)
    
    while mode == "test":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    loadNewLev("up")
                elif event.key == pygame.K_s:
                    if levy <3:
                        levy+=1
                        loadNewLev()
                elif event.key == pygame.K_a:
                    if levx >1:
                        levx-=1
                        loadNewLev()
                elif event.key == pygame.K_d:
                    if levx <3:
                        levx+=1
                        loadNewLev()
                
        print len(all.sprites())
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
                
    while mode == "how to play":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "game"    
            
        bg = pygame.image.load("Resources/howtoplay.png")
        bgrect = bg.get_rect(center = [width/2,height/1.9])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        pygame.display.flip()
        clock.tick(60)
        
    while mode == "quit":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()
