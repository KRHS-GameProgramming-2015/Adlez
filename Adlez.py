import sys, pygame, math, random, time
from Level import *
from Player import *
from Enemy import *
from NPC import *
from Menu import *
from Item import *
pygame.init()

clock = pygame.time.Clock()

width = 1000
height = 700
size = width, height

bgColor = r,b,g = 255,255,255

screen = pygame.display.set_mode(size)

mode = "menu"

enemies = pygame.sprite.Group()
boundries = pygame.sprite.Group()
backGrounds = pygame.sprite.Group()
people = pygame.sprite.Group()
items = pygame.sprite.Group()
players = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Enemy.containers = (enemies, all)
SoftBlock.containers = (backGrounds, all)
HardBlock.containers = (boundries, all)
NPC.containers = (people, all)
Item.containers = (items, all)
Player.containers = (people, players, all)

levLayer =0
levx = 3
levy = 3

start = time.time()

def loadNewLev(direction, levx, levy):
    if direction == "up":
        if levy >1:
            levy-=1
    elif direction == "down":
        if levy <3:
            levy+=1
    elif direction == "left":
        if levx >1:
            levx-=1
    elif direction == "right":
        if levx <3:
            levx+=1
    for s in all.sprites():
        s.kill()
    levFile = "Levels/map" + str(levLayer) + str(levy) + str(levx)
    level=Level(levFile) 
    return levx, levy

while True:
    while mode == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "game"
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
        
    while mode == "how to play":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    mode = "menu"    
            
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
    
    
    levFile = "Levels/map" + str(levLayer) + str(levy) + str(levx)
    level=Level(levFile)
    player = Player([5,5], [900,500])
    
    
    
    while mode == "test":
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
                
        #print len(all.sprites())
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
                
    while mode == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")



        all.update(size)
        #print len(all.sprites())
        
        #From Manpac V2
        if player.rect.center[0] > size[0]:
            levx, levy = loadNewLev("right", levx, levy)
            player = Player([5,5], [0, player.rect.center[1]])
        elif player.rect.center[0] < 0:
            levx, levy = loadNewLev("left", levx, levy)
            player = Player([5,5], [size[0], player.rect.center[1]])
        elif player.rect.center[1] > size[1]:
            levx, levy = loadNewLev("down", levx, levy)
            player = Player([5,5], [player.rect.center[0], 0])
        elif player.rect.center[1] < 0:
            levx, levy = loadNewLev("up", levx, levy)
            player = Player([5,5], [player.rect.center[0], size[1]])
            
        playersHitsBoundries = pygame.sprite.groupcollide(players, boundries, False, False)
        
        for p in playersHitsBoundries:
            for boundry in playersHitsBoundries[p]:
                p.collideHardblock(boundry)
                
        #playersHitsItems = pygame.sprite.groupcollide(players, items, False, False)
        
        #for p in playersHitsitems:
            #for item in playersHitsitems[p]:

        enemiesHitsBoundries = pygame.sprite.groupcollide(enemies, boundries, False, False)
        
        for e in enemiesHitsBoundries:
            for boundry in enemiesHitsBoundries[e]:
                e.collideHardblock(boundry)
                
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    
