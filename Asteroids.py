import pygame
import os


WIDTH,HEIGHT = 900,900
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
FPS = 60 #frames per second

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

pygame.display.set_caption("Shoot the blocks")

#load a new image from a file "spaceship_yellow.png" using pygame.image.load
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))

#create a new surface for this image using pygame.Surface.convert_alpha
YELLOW_SPACESHIP = pygame.Surface.convert_alpha(YELLOW_SPACESHIP_IMAGE)
# rotate this image and scale it using pygame.transform 
#YELLOW_SPACESHIP = 

#define a draw_window function that displays all elements on the screen
def draw_window():
    pass
    # Display the YELLOW_SPACESHIP surface using pygame.surface.blit
    #     
    
   
game_running = True
while game_running:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    #check for all the events that can occur
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_running = False
    
    draw_window()
    pygame.display.update()
    


    
    

pygame.quit()