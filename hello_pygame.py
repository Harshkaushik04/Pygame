import pygame #importing pygame library
pygame.init() #initialising pygame
screen=pygame.display.set_mode((640,480),0,32) #setting up display, dont know about flags and depth
pygame.display.set_caption("hello pygame") #title
screen.fill((0,0,0)) #dont know mechanism of color setting
game_over=False #key for closing application
#this is the main game loop:
while not game_over: #untill game_over=true
    for event in pygame.event.get(): #pygame.event.get() retreives a list of all events that has occurred between the time frame it was called last time and it has been called this time
        #print(pygame.QUIT) => value coming to be 256, when event.type=256 it stops(256 is probably random value by pygame developers)
        #print(event.type)
        if event.type==pygame.QUIT: #pygame.QUIT represents clicking close option(=256), therefore when close button is clicked, this statement becomes true
            game_over=True #when game_over becomes true, the outer loop breaks
#print(type(pygame.event.get())) =>list

def simple_application_screen_size(l,b):
    pygame.init()
    screen=pygame.display.set_mode((l,b),0,32)
    pygame.display.set_caption("hello pygame")
    screen.fill((0,0,0))
    game_over=False
    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
    return "application completed"
#l=int(input("enter length:"))
#b=int(input("enter breadth:"))
#screen_size(l,b)
