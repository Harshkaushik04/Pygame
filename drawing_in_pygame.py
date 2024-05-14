import pygame
pygame.init()
screen=pygame.display.set_mode((640,480),0,32)
pygame.display.set_caption("hello pygame")
sprite1=pygame.image.load('/home/harsh/PycharmProjects/pygame_tutorial/images/football.png')
screen.fill((0,0,0))
game_over=False
#this is the main game loop:
while not game_over: #untill game_over=true
    for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
    screen.blit(sprite1,(0,0)) #displaying image at (0,0), (0,0) is at top left corner
    pygame.display.update() #updates display after each loop
#for displaying at centre of screen, co ordinates taken would be (304,224), as these co ordinates are for left edge of image and top edge of image respectively


