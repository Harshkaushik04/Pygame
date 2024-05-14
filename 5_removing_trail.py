import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((700,700),0,32)
pygame.display.set_caption("Hello repeating key")
screen.fill((0,0,0))
butterfly=pygame.image.load('/home/harsh/PycharmProjects/pygame_tutorial/images/butterfly.png')
butterfly=pygame.transform.scale(butterfly,(50,50))
game_over=False
x,y=0,0
clock=pygame.time.Clock() #for fps
while not game_over:
    dt = clock.tick(100) #100=max fps
    #print(dt)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    #when these outside, for loop,on holding key, it works.
    pressed=pygame.key.get_pressed()
    if pressed[K_UP]:
        y+=-0.5*dt
    elif pressed[K_DOWN]:
        y+=0.5*dt
    elif pressed[K_LEFT]:
        x+=-0.5*dt
    elif pressed[K_RIGHT]:
        x+=0.5*dt
    elif pressed[K_SPACE]:
        x,y=0,0
    screen.fill((0,0,0))
    screen.blit(butterfly,(x,y))
    pygame.display.update()