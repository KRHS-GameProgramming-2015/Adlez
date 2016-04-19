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

mode = "game"

boundries = pygame.sprite.Group()
backGrounds = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

SoftBlock.containers = (boundries, all)
HardBlock.containers = (boundries, all)

levLayer =0
levx = 3
levy = 3

def loadNewLev(direction, levx, levy):
    if direction == "up":
        if levy >1:
            levy-=1
        if levy <3:
            levy+=1
            
            loadNewLev("down")
        if levx >1:
            levx-=1
            loadNewLev("left")
        if levx <3:
            levx+=1
            loadNewLev("right")
    for s in all.sprites():
        s.kill()
    levFile = "Levels/map" + str(levLayer) + str(levy) + str(levx) + ".lvl"
    level=Level(levFile) 
    return levx, levy

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
        
    levFile = "Levels/map" + str(levLayer) + str(levy) + str(levx) + ".lvl"
    level=Level(levFile)
    
    while mode == "start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    levx, levy = loadNewLev("up", levx, levy)
                elif event.key == pygame.K_s:
                    levx, levy = loadNewLev("down", levx, levy)
                elif event.key == pygame.K_a:
                    levx, levy = loadNewLev("left", levx, levy)
                elif event.key == pygame.K_d:
                    levx, levy = loadNewLev("right", levx, levy)
                
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
