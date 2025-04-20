import pygame
import sys
pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT= 800,600
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("sound")
font=pygame.font.SysFont(None, 45)
clock=pygame.time.Clock()

BUTTON_RECT= pygame.Rect(200,120,200,50)
click_sound= pygame.mixer.Sound("click.wav")

def draw_button(mouse_pos):
    color=(0,255,100) if not BUTTON_RECT.collidepoint(mouse_pos) else (0,255,250)
    pygame.draw.rect(screen,color,BUTTON_RECT)
    text=font.render("click to play", True, (255,255,255))
    text_rect=text.get_rect(center=BUTTON_RECT.center)
    screen.blit(text,text_rect)

pygame.mixer.music.load("click.wav")  
pygame.mixer.music.play(-1)

running= True
while running:
    screen.fill((30,30,30))
    draw_button(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running= False

        if event.type==pygame.MOUSEBUTTONDOWN:
            if BUTTON_RECT.collidepoint(event.pos):
                click_sound.play()
                print("button is clicked now playing sound")

    
    pygame.display.flip()
    clock.tick(60)
               
pygame.quit()
sys.exit()
