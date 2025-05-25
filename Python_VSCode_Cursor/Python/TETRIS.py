#테트리스게임을 만들자!
import pygame as pg,pygame
import random

pg.init()

background=pg.display.set_mode((300,600))
pg.display.set_caption("테트리스 게임")

red=(255,0,0)
yellow=(255,255,0)
green=(0,255,0)
blue=(0,0,255)

for i in range(11): #격자그리기
    pg.draw.line(background,(189,189,189),(i*30,0),(i*30,600))
for i in range(21):
    pg.draw.line(background,(189,189,189),(0,i*30),(300,i*30))

play=True
while play:
    
    for event in pg.event.get(): #종료 코드
        if event.type==pg.QUIT:
            play=False
    

    pg.display.update()


pygame.quit()