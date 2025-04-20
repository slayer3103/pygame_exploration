import pygame
import sys 
pygame.init()

WIDTH, HEIGHT =800,600
screen= pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("keyboard and mouse input ")
clock = pygame.time.Clock()

square_x = 100
square_y = 100
sqaure_speed =5

#main loo[p 

running= True
while running:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square_x -= sqaure_speed
    if keys[pygame.K_RIGHT]:
        square_x += sqaure_speed
    if keys[pygame.K_UP]:
        square_y -= sqaure_speed
    if keys[pygame.K_DOWN]:
            square_y += sqaure_speed

    screen.fill((30,30,30))
    pygame.draw.rect(screen,(255,0,0),(square_x,square_y,50,50))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
