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

# Sprite 불러오기
spaceship = pygame.image.load(r"C:\2domi_VSC_repository\GitHub_repository\나도코딩_Pygame\spaceship.png")
spaceship = pygame.transform.scale(spaceship, (50, 50)) # 크기 조정 (50x50)
spaceship_x = 215
spaceship_y = 590

# 이동할 장소
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.5

# FPS
clock = pygame.time.Clock()

# Event Roop
Running = True
while Running :
    dt = clock.tick(144) # 초당 프레임수 설정

    for event in pygame.event.get(): # 이벤트 발생 상시 체크중...
        if event.type == pygame.QUIT : # 종료 이벤트가 있을때
            Running = False # while문 탈출

        if event.type == pygame.KEYDOWN : # 아무 키나 눌렸을때
            if event.key == pygame.K_a :
                to_x -= character_speed
            if event.key == pygame.K_d :
                to_x += character_speed
            if event.key == pygame.K_w :
                to_y -=  character_speed
            if event.key == pygame.K_s :
                to_y +=  character_speed    
            
        if event.type == pygame.KEYUP : 
            if event.key == pygame.K_w or event.key == pygame.K_s :   
                to_y = 0
            if event.key == pygame.K_a or event.key == pygame.K_d : 
                to_x = 0

    # 화면 경계 체크
    spaceship_x = max(0, min(screen_width - 50, spaceship_x))
    spaceship_y = max(0, min(screen_height - 50, spaceship_y))


    spaceship_x += to_x * dt
    spaceship_y += to_y * dt

    screen.blit(background, (0,0)) # 백그라운드 (0,0)에 넣기.
    screen.blit(spaceship, (spaceship_x, spaceship_y))

    pygame.display.update() # 화면 업데이트

pygame.quit() # 종료