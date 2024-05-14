import pygame
pygame.init()
butterfly=pygame.image.load('/home/harsh/PycharmProjects/pygame_tutorial/images/butterfly.png')
butterfly=pygame.transform.scale(butterfly,(50,50)) #resized buttlerfly
#middle_width_of_butterfly=butterfly.get_width()/2 => butterfly.get_width() for getting width of butterfly png
#middle_height_of_butterfly=butterfly.get_height()/2
screen=pygame.display.set_mode((500,500),0,32)
screen.fill((0,0,0))
pygame.display.set_caption("hello resize")
game_over=False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    screen.blit(butterfly,(screen.get_width()/2-butterfly.get_width()/2,screen.get_height()/2-butterfly.get_height()/2)) #screen.get_width() for getting width of screen and butterfly.get_width() for getting width of butterfly png
    pygame.display.update()
