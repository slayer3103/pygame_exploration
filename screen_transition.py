import pygame
import sys
pygame.init()

WIDTH,HEIGHT  =800,600
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("transition trial")
font= pygame.font.SysFont(None, 45)
clock= pygame.time.Clock()

button_color=(0,200,100)
hover_color=(0,255,150)
text_color=(255,255,255)
button_box=pygame.Rect(300,250,200,60)

current_screen= "welcome"

def draw_button(mouse_pos):
    color=hover_color if button_box.collidepoint(mouse_pos) else button_color
    pygame.draw.rect(screen, color,button_box)

    text= font.render("start the game", True, text_color)
    text_rect= text.get_rect(center=button_box.center)
    screen.blit(text, text_rect)

def draw_welcome_screen():
    screen.fill((0,0,50))
    title=font.render("welcome to the game",True,text_color)
    screen.blit(title,(220,100))
    draw_button(pygame.mouse.get_pos())

def draw_game_screen():
    screen.fill((20,20,20))
    text=font.render("this is the game screen",True,text_color)
    screen.blit(text,(240,280))

running= True
while running:

    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running=False

        #new - handel click on welcome screen to game screen
        if current_screen=="welcome" and event.type == pygame.MOUSEBUTTONDOWN:
            print("starting game screen")
            current_screen="game"

    #drawing the current screens
    if current_screen=="welcome":
        draw_welcome_screen()
    elif current_screen=="game":
        draw_game_screen()



    pygame.display.flip()

    clock.tick(60)
pygame.quit()
sys.exit()
