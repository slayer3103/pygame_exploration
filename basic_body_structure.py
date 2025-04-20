import pygame
import sys
pygame.init()

WIDTH, HEIGHT= 800,600
screen= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("screen transition")

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    
    

    pygame.display.flip()
pygame.quit()
sys.exit()
