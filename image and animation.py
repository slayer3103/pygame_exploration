import pygame
import sys

pygame.init()

WIDTH, HEIGHT=800,600
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("sound testing")
font=pygame.font.SysFont(None, 45)
clock= pygame.time.Clock()

player_img=pygame.image.load("assets/pieces/wK.png")
player_pos=[100,100]


running =True
while running:
    screen.fill((30,30,30))
    screen.blit(player_img, player_pos)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False
    
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0]-=5
    if keys[pygame.K_RIGHT]:
        player_pos[0] +=5
    if keys[pygame.K_DOWN]:
        player_pos[1] -= 5
    if keys[pygame.K_DOWN]:
        player_pos[1] += 5





    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
