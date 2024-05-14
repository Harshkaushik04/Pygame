from standard_object import object_restricted_motion
#object_restricted_motion('/home/harsh/PycharmProjects/pygame_tutorial/images/butterfly.png',700,700,50,50,0.5,100,"Hello Butterfly)

import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((500,500),0,32)
pygame.display.set_caption("Hello Button")
text_colour=(255,255,255) #white colour
button_colour=(0,0,170) #blue colour
button_over_colour=(255,50,50) #red colour
button_width=100
button_height=50
x,y=0,0
button_rect=[screen.get_width()/2-button_width/2,screen.get_height()/2-button_height/2,button_width,button_height]
#button_rect is a list
button_font=pygame.font.SysFont('Arial',20)
button_text=button_font.render('Quit',True,text_colour) #button_text is from class 'pygame.surface.Surface'
print(type(button_text))
screen.fill((100,100,100)) #grey colour
#first 2 co ordinates of button_rect are co ordinates of leftmost and topmost respectively
list_colour=[button_colour,button_over_colour]
colour=list_colour[0]
GAME_OVER=False
while not GAME_OVER:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            GAME_OVER=True
        if event.type==MOUSEMOTION:
            x,y=event.pos
        if event.type==MOUSEBUTTONDOWN and x>(screen.get_width()-button_width)/2 and x<(screen.get_width()+button_width)/2 and y>(screen.get_height()-button_height)/2 and y<(screen.get_height()+button_height)/2:
            colour=list_colour[(list_colour.index(colour)+1)%2] #keep changing colour after clicking
    #continuous events-to be placed outside for loop
    #event management to be done inside for loop- by event management it means to change variable values(and not change anything in output from there
    #incase you need to do both continuous events and event management, then just initialise a new variable and change its value by event management inside for loop and then implement continuous event outside for loop by that variable
    pygame.draw.rect(screen,colour,button_rect)
    #for placing text on top left corner
    #screen.blit(button_text,(button_rect[0],button_rect[1])) #button_rect is a list
    text_width=button_text.get_width()
    text_height=button_text.get_height()
    screen.blit(button_text,(screen.get_width()/2-text_width/2,screen.get_height()/2-text_height/2)) #when text is to be placed in centre of button
    pygame.display.update()
pygame.quit()