import pygame
from pygame.locals import * #for importing arrow keys movemenets and much more....
pygame.init()
butterfly=pygame.image.load('/home/harsh/PycharmProjects/pygame_tutorial/images/butterfly.png')
butterfly=pygame.transform.scale(butterfly,(50,50)) #resized buttlerfly
#middle_width_of_butterfly=butterfly.get_width()/2 => butterfly.get_width() for getting width of butterfly png
#middle_height_of_butterfly=butterfly.get_height()/2
screen=pygame.display.set_mode((500,500),0,32)
screen.fill((0,0,0))
pygame.display.set_caption("hello resize")
game_over=False
x,y=0,0
while not game_over:
    for event in pygame.event.get():#whenever an event happens, this loop becomes active
        #for example, when up key is pressed, event is recorded and hence pygame,event.get() gets non empty
#imp    #the condition in a for loop is evaluated once, at the beginning of the loop, and it does not re-evaluate during the loop's execution. Changing the value of a variable used in the loop's condition within the loop itself will not affect the loop's behavior.
        if event.type==pygame.QUIT:
            game_over=True
        pressed=pygame.key.get_pressed() #pressed is of class "pygame.key.ScancodeWrapper"
        #butterfly moves but it remains a trail behind it(previous image doesnt gets erased)
        if pressed[K_UP]:
            y+=-3
        elif pressed[K_DOWN]:
            y+=3
        elif pressed[K_LEFT]:
            x+=-3
        elif pressed[K_RIGHT]:
            x+=3
    screen.blit(butterfly,(x,y)) #screen.get_width() for getting width of screen and butterfly.get_width() for getting width of butterfly png
    pygame.display.update()
