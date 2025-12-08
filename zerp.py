from pygame.locals import *
import pygame
pygame.init()
running=True
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
screen=pygame.display.set_mode((640,240))
while running:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            running=False
    screen.fill(YELLOW)
    pygame.display.update() 

        
pygame.quit()