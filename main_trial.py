import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("First_trial")

#10 to 13 put text at location 300, 50 
font =pygame.font.SysFont(None, 45)


# main loop

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        if event.type ==pygame.MOUSEBUTTONDOWN:
            if event.button == 1 :
                pos= pygame.mouse.get_pos()
                print("mouse clicked at ", pos)

        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left arrow preesed")
            elif event.key == pygame.K_SPACE:
                print("space is pressed ")



    screen.fill((0,128,255))
    pygame.draw.rect(screen,(255,0,0),(100,100,200,100))
    pygame.draw.circle(screen,(0,255,0),(400,300),50)
    pygame.draw.line(screen,(255,255,0),(0,0),(800,600),5)

    text=  font.render("hello", True,(255,255,255))
    screen.blit(text, (300,50))
    pygame.display.flip()

pygame.quit()
sys.exit()
