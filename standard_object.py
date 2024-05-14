import pygame
from pygame.locals import *
def object_restricted_motion(object_location,l_screen,w_screen,l_object,w_object,movement,fps,title_of_application):
    pygame.init()
    screen=pygame.display.set_mode((l_screen,w_screen),0,32)
    screen.fill((0,0,0))
    pygame.display.set_caption(title_of_application)
    object=pygame.image.load(object_location)
    object=pygame.transform.scale(object,(l_object,w_object))
    game_over=False
    x,y=0,0
    clock=pygame.time.Clock()
    while not game_over:
        dt=clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            elif event.type==pygame.MOUSEMOTION:
                x,y=event.pos
                x-=object.get_width()/2
                y-=object.get_height()/2
        pressed=pygame.key.get_pressed()
        if pressed[K_UP] and y>0:
            y-=movement*dt
        elif pressed[K_DOWN] and y<screen.get_height()-object.get_height():
            y+=movement*dt
        elif pressed[K_LEFT] and x>0:
            x-=movement*dt
        elif pressed[K_RIGHT] and x<screen.get_width()-object.get_width():
            x+=movement*dt
        elif pressed[K_SPACE]:
            x,y=0,0
        screen.fill((0,0,0))
        screen.blit(object,(x,y))
        pygame.display.update()