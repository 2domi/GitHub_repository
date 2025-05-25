"""import pygame

def object_pos_xpos_ypos_width_height(a,b,c,d):
    return((a-(c/2),b-(d/2)))

pygame.init()

image_background=pygame.image.load("Image/파이썬_산호색하늘과구름배경.jfif")
background_width=image_background.get_size()[0] #가로
background_height=image_background.get_size()[1] #세로

image_key=pygame.image.load("Image/파이썬_키아이콘.jfif")
key_width=image_key.get_size()[0] #가로
key_height=image_key.get_size()[1] #세로
image_key=pygame.transform.scale(image_key,((key_width//5),(key_height//5)))
key_width=image_key.get_size()[0] #가로
key_height=image_key.get_size()[1] #세로

background=pygame.display.set_mode((720,480))  
pygame.display.set_caption("2domi") 
playing=True
background.fill((0,0,0))
while playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            playing=False
    background.blit(image_background,(0,0))
    image_background.blit(image_key,object_pos_xpos_ypos_width_height(360,240,key_width,key_height))
    pygame.display.update()"""

import pygame

pygame.init()
info=pygame.display.Info()
background=pygame.display.set_mode((960,540))

Playing=True 
while Playing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Playing=False
    for i in range(960):
        x=i*255//960
        pygame.draw.line(background,(30,200,x),(i,0),(i,540))
    pygame.display.update()
pygame.quit()