import pygame
import os
import time
import random

pygame.init()
os.environ["SDL_VIDEO_CENTERED"] = "1" # 화면 중앙정렬

screen = pygame.display.set_mode((480,480))
pygame.display.set_caption("Snake Game")

score = 0
snakeX = 24
snakeY = 240
snake_position = [snakeX,snakeY,24,24]          
ALlSNAKEPOSITION = [[72,240,24,24],[0,240,24,24],[-12,240,24,24],[-24,240,24,24]]
snake_length = 4
GoingX = 24
GoingY = 0
apple_position = [random.randint(0,19)*24,random.randint(0,19)*24,24,24]
Play = True
clock = pygame.time.Clock()








while Play:
    clock.tick(8)
    screen.fill((0,0,0)) #화면 초기화

    for i in range(20):
        pygame.draw.line(screen,(100,100,100),(i*24,0),(i*24,480))
        pygame.draw.line(screen,(100,100,100),(0,i*24),(480,i*24))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Play = False

        if event.type == pygame.KEYDOWN: #방향키 감지
            if event.key == pygame.K_UP and GoingY != 24:
                GoingX, GoingY = 0,-24
            if event.key == pygame.K_DOWN and GoingY != -24:
                GoingX, GoingY = 0,24
            if event.key == pygame.K_RIGHT and GoingX != -24:
                GoingX,GoingY = 24,0
            if event.key == pygame.K_LEFT and GoingX != 24:
                GoingX,GoingY = -24,0


    snakeX += GoingX
    snakeY += GoingY
    snake_position = [snakeX,snakeY,24,24]

    if snake_position in ALlSNAKEPOSITION[:-1]: #스네이크가 자기 몸에 부딪힌다면
        Play = False

    if snakeX >= 480 or snakeX < 0 or snakeY >= 480 or snakeY < 0: #스네이크가 화면에서 벗어난다면
        Play = False

    if snake_position == apple_position:
        score += 1
        snake_length += 1

        possible_positions = [
            [x * 24, y * 24, 24, 24]
            for x in range(20)
            for y in range(20)
            if [x * 24, y * 24, 24, 24] not in ALlSNAKEPOSITION
        ]
        apple_position = random.choice(possible_positions)

    ALlSNAKEPOSITION.append(snake_position[:])


    for i in range(snake_length):
        pygame.draw.rect(screen,(0,255,255-(i*(255//(snake_length+1)))),(ALlSNAKEPOSITION[-(i+1)]))

    pygame.draw.rect(screen, (255,0,0), apple_position)
    screen.blit(pygame.font.Font(None,40).render(f"score: {score}",True, (255,255,255)),(0,0))

    if len(ALlSNAKEPOSITION) > snake_length:
        ALlSNAKEPOSITION.pop(0) 
    

    pygame.display.update()
pygame.quit()