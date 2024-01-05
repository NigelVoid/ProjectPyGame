import random

import pygame
from pygame.locals import *
import runpy

pygame.init()

WIDTH = 800
HEIGHT = 400
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
FPS = 60

place = (70, 130, 180)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PING-PONG")
r1 = True
r2 = False
r3 = False
r4 = False
clock = pygame.time.Clock()

paddle1_pos = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_pos = (HEIGHT - PADDLE_HEIGHT) // 2
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [3, -3]
score1 = 0
score2 = 0
shrift = pygame.font.SysFont('arial', 45)
running = True
ball = pygame.mixer.Sound('music/ping-pong/Ball.mp3')
r4_bong = False
rr1 = False
rr2 = False
rr3 = False
rr4 = False
ach_write = False
COLOR_circle = (255, 255, 255)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            runpy.run_module('main')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                r1 = True
                r2 = False
                r3 = False
                r4 = False
                rr1 = True
            if event.key == pygame.K_2:
                r2 = True
                r1 = False
                r3 = False
                r4 = False
                rr2 = True
            if event.key == pygame.K_3:
                r3 = True
                r2 = False
                r1 = False
                r4 = False
                rr3 = True
            if event.key == pygame.K_4:
                r1 = False
                r2 = False
                r3 = False
                r4 = True
                rr4 = True

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        if r4:
            if paddle2_pos - 8 >= 0:
                paddle2_pos -= 8
        else:
            if paddle2_pos - 5 >= 0:
                paddle2_pos -= 5
    if keys[K_DOWN]:
        if r4:
            if paddle2_pos + 60 + 8 <= 400:
                paddle2_pos += 8
        else:
            if paddle2_pos + 60 + 5 <= 400:
                paddle2_pos += 5
    if keys[K_w]:
        if r4:
            if paddle1_pos - 8 >= 0:
                paddle1_pos -= 8
        else:
            if paddle1_pos - 5 >= 0:
                paddle1_pos -= 5
    if keys[K_s]:
        if r4:
            if paddle1_pos + 60 + 8 <= 400:
                paddle1_pos += 8
        else:
            if paddle1_pos + 60 + 5 <= 400:
                paddle1_pos += 5
    if r4:
        if ball_vel[0] < 0:
            ball_pos[0] += ball_vel[0] - 2
        else:
            ball_pos[0] += ball_vel[0] + 2
        if 0 > ball_vel[1]:
            ball_pos[1] += ball_vel[1] - 3
        else:
            ball_pos[1] += ball_vel[1] + 3
    if r3:
        if ball_vel[0] < 0:
            ball_pos[0] += ball_vel[0] - 8
        else:
            ball_pos[0] += ball_vel[0] + 8
        if 0 > ball_vel[1]:
            ball_pos[1] += ball_vel[1] + 4
        else:
            ball_pos[1] += ball_vel[1] - 4
    if r2:
        if ball_vel[0] < 0:
            ball_pos[0] += ball_vel[0] - 2
        else:
            ball_pos[0] += ball_vel[0] + 2
        if 0 > ball_vel[1]:
            ball_pos[1] += ball_vel[1] - 2
        else:
            ball_pos[1] += ball_vel[1] + 2
    if r1:
        ball_pos[0] += ball_vel[0]
        ball_pos[1] += ball_vel[1]

    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
        if r4 and not r4_bong:
            ball_vel[0] = -ball_vel[0]
            r4_bong = True
        ball.play()

    if (ball_pos[0] <= PADDLE_WIDTH and paddle1_pos - BALL_RADIUS <= ball_pos[
        1] <= paddle1_pos + PADDLE_HEIGHT + BALL_RADIUS) or \
            (ball_pos[0] >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and paddle2_pos - BALL_RADIUS <= ball_pos[
                1] <= paddle2_pos + PADDLE_HEIGHT + BALL_RADIUS):
        ball_vel[0] = -ball_vel[0]
        if r4 and not r4_bong:
            ball_vel[1] = -ball_vel[1]
            ball_vel[0] = -ball_vel[0]
            r4_bong = True
        ball.play()

    screen.fill(place)
    pygame.draw.line(screen, WHITE, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(screen, WHITE, [PADDLE_WIDTH, 0], [PADDLE_WIDTH, HEIGHT], 1)
    pygame.draw.line(screen, WHITE, [WIDTH - PADDLE_WIDTH, 0], [WIDTH - PADDLE_WIDTH, HEIGHT], 1)
    pygame.draw.circle(screen, COLOR_circle, [WIDTH // 2, HEIGHT // 2], 50, 1)
    pygame.draw.circle(screen, COLOR_circle, [WIDTH // 2, HEIGHT // 2], 2)
    pygame.draw.rect(screen, WHITE, Rect((PADDLE_WIDTH, paddle1_pos), (PADDLE_WIDTH, PADDLE_HEIGHT)))
    pygame.draw.rect(screen, WHITE, Rect((WIDTH - PADDLE_WIDTH * 2, paddle2_pos), (PADDLE_WIDTH, PADDLE_HEIGHT)))
    pygame.draw.circle(screen, WHITE, ball_pos, BALL_RADIUS)
    if ball_pos[0] > 800:
        score1 += 1
    if ball_pos[0] < 0:
        score2 += 1
    if ball_pos[0] > 800 or ball_pos[0] < 0:
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_vel[0] = -ball_vel[0]
        r4_bong = False
    if (WIDTH // 2 - 50 < ball_pos[0] < WIDTH // 2 + 50) and HEIGHT // 2 - 50 < ball_pos[1] < HEIGHT // 2 + 50 and r4:
        ball_vel[0] = -ball_vel[0]
        COLOR_circle = (0, 255, 100)
    else:
        COLOR_circle = (255, 255, 255)
    if score1 < 10:
        screen.blit(shrift.render(f'{score1} : {score2}', 1, (190, 190, 190)), (364, 350))
    else:
        screen.blit(shrift.render(f'{score1} : {score2}', 1, (190, 190, 190)), (344, 350))
    if not ach_write and rr1 and rr2 and rr3 and rr4:
        with open('ping-pong.txt', mode='w', encoding='utf8') as f:
            print('efwgyufgweuyffGyeskkkkkkkkkkkkkkrngrjkngnrjngrgj', file=f)
        ach_write = True
    pygame.display.flip()
    clock.tick(FPS)
