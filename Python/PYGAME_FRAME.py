import pygame

pygame.init() # 그냥 기본으로 이건 해야함

## Set Screen
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("2domi Game") # 게임 이름

## Background
try : background = pygame.image.load(r"파일주소")
except : 
    print("error : Can't Upload background image")
    background = None
## Sprites (정의, 불러오기, xy좌표 지정, 속도 지정 등등)

## FPS
clock = pygame.time.Clock()

## Font 
game_font = pygame.font.Font(r"파일명")

Running = True
while Running :
    dt = clock.tick(144) # 초당 프레임수 설정

    for event in pygame.event.get(): # Event Checking
        ## 종료코드
        if event.type == pygame.QUIT : 
            Running = False 

        ## 추가적인 코드들

        ## 화면에 띄우기 (pygame.blit())

    pygame.display.update() # 화면 업데이트

pygame.quit() # 종료