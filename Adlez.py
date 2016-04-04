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

bgColor = r,b,g = 0,0,0

screen = pygame.display.set_mode(size)

mode = "start"

while True:
    while mode == "start":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "pvp"
                if event.key == pygame.K_2:
                    mode = "practice"
                    
        bg = pygame.image.load("Pics/menubackground.png")
        bgrect = bg.get_rect(center = [width/2,height/2])
        option = pygame.image.load("Pics/Gamemodeimageoptions.png")
        optionrect = option.get_rect(center = [width/2, 3*height/4])
        
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        screen.blit(option, optionrect)
        pygame.display.flip()
        clock.tick(60)
