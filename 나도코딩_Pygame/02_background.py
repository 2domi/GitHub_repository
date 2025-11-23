import pygame

pygame.init() # 그냥 기본으로 이건 해야함

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # tuple로

# 화면 타이틀 설정
pygame.display.set_caption("2domi Game") # 게임 이름

# 배경 설정
background = pygame.image.load(r"C:\2domi_VSC_repository\GitHub_repository\나도코딩_Pygame\spacebackground.png")

# Event Roop
Running = True
while Running :
    for event in pygame.event.get(): # 이벤트 발생 상시 체크중...
        if event.type == pygame.QUIT : # 종료 이벤트가 있을때
            Running = False # while문 탈출
    screen.blit(background, (0,0)) # 백그라운드 (0,0)에 넣기.
    pygame.display.update() # 화면 업데이트

pygame.quit() # 종료