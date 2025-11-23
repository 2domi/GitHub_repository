import pygame
import random

pygame.init() # 그냥 기본으로 이건 해야함

## Set Screen
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("2domi Game") # 게임 이름

## Background
try : background = pygame.image.load(r"C:\2domi_VSC_repository\GitHub_repository\나도코딩_Pygame\spacebackground.png")
except : 
    print("error : Can't Upload background image")
    background = None

## Main Character
character = pygame.image.load(r"C:\2domi_VSC_repository\GitHub_repository\나도코딩_Pygame\spaceship.png")
character = pygame.transform.scale(character, (50,50))
character_x = screen_width // 2 - 25
character_y = screen_height - 50
character_speed = 0.6
to_x = 0
to_y = 0

## Meteor
meteor = pygame.image.load(r"C:\2domi_VSC_repository\GitHub_repository\나도코딩_Pygame\meteor.png")
meteor = pygame.transform.scale(meteor, (50,50))
meteor_x = screen_width//2 - 25
meteor_y = -50
meteor_state = 0 # 0:재생성함, 1: 이동중.

## FPS  
clock = pygame.time.Clock()

## Font 
try :
    game_font = pygame.font.Font(r"파일명")
except :
    game_font = None

Running = True
while Running :
    dt = clock.tick(144) # 초당 프레임수 설정

    for event in pygame.event.get(): # Event Checking
        ## 종료코드
        if event.type == pygame.QUIT : 
            Running = False 

    ## Main Character 좌우이동
    keys = pygame.key.get_pressed()  # 현재 눌린 키 상태 확인
    to_x = 0

    if keys[pygame.K_a]:
        to_x -= character_speed
    if keys[pygame.K_d]:
        to_x += character_speed

    ## Meteor 이동
    if meteor_state == 0:
        meteor_x = random.uniform(0,430)
        meteor_y = -50
        meteor_state = 1
    else :
        meteor_y += 0.5 * dt

    if meteor_y >= 640:
        meteor_state = 0

    character_x += to_x * dt

    ## 화면 경계 처리
    if character_x < 0:
        character_x = 0
    if character_x > screen_width - 50:  # 캐릭터 크기(50)를 고려q  q
        character_x = screen_width - 50
        
    ## 화면에 띄우기 (screen.blit())
    screen.blit(background, (0,0))
    screen.blit(character, (character_x, character_y))
    screen.blit(meteor, (meteor_x, meteor_y))

    ## Meteor - Character collided
    character_rect = character.get_rect(top=character_y,left=character_x)
    meteor_rect = meteor.get_rect(top=meteor_y,left=meteor_x)

    if meteor_rect.colliderect(character_rect):
        Running = False

    pygame.display.update() # 화면 업데이트

pygame.quit() # 종료