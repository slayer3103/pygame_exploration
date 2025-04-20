import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("buttons trial ")
font= pygame.font.SysFont(None, 45)
clock = pygame.time.Clock()


button_color= (0,200,100)
hover_color= (0,255,150)
text_color =(255,255,255)
button_rect= pygame.Rect(300,250,200,60)

def draw_button(mouse_pos):

    if button_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen,hover_color,button_rect,)
    else:
        pygame.draw.rect(screen,button_color,button_rect)


    text =font.render("start",True, text_color)
    text_rect= text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

running=True
while running:
    screen.fill((30,30,30))

    mouse_pos = pygame.mouse.get_pos()
    draw_button(mouse_pos)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                print("starting new game ")

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
