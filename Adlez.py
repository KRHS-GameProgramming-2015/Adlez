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

mode = "game"

while True:
    while mode == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    mode = "continue"
                if event.key == pygame.K_2:
                    mode = "start"
                if event.key == pygame.K_3:
                    mode = "how to play"
                if event.key == pygame.K_q:
                    mode = "quit"
                    
        screen.fill(bgColor)
        pygame.display.flip()
        clock.tick(60)

    while mode == "continue":

    while mode == "start":
        
    while mode == "how to play":
        
    while mode == "quit":
