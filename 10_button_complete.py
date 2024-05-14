import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((700,700),0,32)
screen.fill((100,100,100))
button_colour=(0,0,170)
button_over_colour=(255,50,50)
button_width=100
button_height=50
text_colour=(255,255,255)
button_Rect=[(screen.get_width()-button_width)/2,(screen.get_height()-button_height)/2,button_width,button_height]
button_font=pygame.font.SysFont('Arial',20)
button_text=button_font.render("Quit",True,text_colour)
x,y=0,0
list_colour=[button_colour,button_over_colour]
colour=list_colour[0]
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        elif event.type==MOUSEMOTION:
            x,y=event.pos
        elif event.type==MOUSEBUTTONDOWN and x>(screen.get_width()-button_width)/2 and x<(screen.get_width()+button_width)/2 and y>(screen.get_height()-button_height)/2 and y<(screen.get_height()+button_height)/2:
            game_over=True
    if x > (screen.get_width() - button_width) / 2 and x < (screen.get_width() + button_width) / 2 and y > (screen.get_height() - button_height) / 2 and y < (screen.get_height() + button_height) / 2:
        colour = list_colour[1]
    else:
        colour=list_colour[0]
    pygame.draw.rect(screen,colour,button_Rect)
    screen.blit(button_text,(((screen.get_width()-button_text.get_width())/2,(screen.get_height()-button_text.get_height())/2)))
    pygame.display.update()