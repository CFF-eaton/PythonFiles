import pygame
import random
from pygame.locals import *
import sys
pygame.init()
screen_width=700
screen_height=400
DISPLAYSURF=pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption("Hello Game!")
green=(0,255,0)
red=(255,0,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

class Block(pygame.sprite.Sprite):
    
    def __init__(self,color,width,height):
        super().__init__()
        self.image=pygame.Surface([width,height])
        self.image.fill(color)
        self.image.set_colorkey(white)
        
        pygame.draw.rect(self.image,color,[0,0,width,height])
        self.rect=self.image.get_rect()

block_list=pygame.sprite.Group()
for i in range(50):
    block=Block(black,50,50)
    block.rect.x=random.randrange(screen_width)
    block.rect.y=random.randrange(screen_height)
    block_list.add(block)

object1=pygame.Rect((100,100),(200,150))

pygame.draw.rect(DISPLAYSURF,green,object1)
pygame.draw.circle(DISPLAYSURF,red,(100,150),50)
pygame.draw.line(DISPLAYSURF,blue,(0,0),(300,300))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            #sys.exit()
    DISPLAYSURF.fill(white)
    block_list.draw(DISPLAYSURF)
    pygame.display.update()