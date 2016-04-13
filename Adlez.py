import sys, pygame, math, random
from Level import *
from Player import *
from NPC import *
from Menu import *
pygame.init()

clock = pygame.time.Clock()

width = 960
height = 672
size = width, height

bgColor = r,b,g = 255,255,255

screen = pygame.display.set_mode(size)

mode = "game"

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

    while mode == "start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player.go("up")
                elif event.key == pygame.K_s:
                    player.go("down")
                elif event.key == pygame.K_a:
                    player.go("left")
                elif event.key == pygame.K_d:
                    player.go("right")
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player.go("stop up")
                elif event.key == pygame.K_s:
                    player.go("stop down")
                elif event.key == pygame.K_a:
                    player.go("stop left")
                elif event.key == pygame.K_d:
                    player.go("stop right")
                
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
