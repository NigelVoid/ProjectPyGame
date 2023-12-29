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
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            runpy.run_module('main')

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        if paddle2_pos - 5 >= 0:
            paddle2_pos -= 5
    if keys[K_DOWN]:
        if paddle2_pos + 60 + 5 <= 400:
            paddle2_pos += 5
    if keys[K_w]:
        if paddle1_pos - 5 >= 0:
            paddle1_pos -= 5
    if keys[K_s]:
        if paddle1_pos + 60 + 5 <= 400:
            paddle1_pos += 5

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
        ball.play()

    if (ball_pos[0] <= PADDLE_WIDTH and paddle1_pos - BALL_RADIUS <= ball_pos[
        1] <= paddle1_pos + PADDLE_HEIGHT + BALL_RADIUS) or \
            (ball_pos[0] >= WIDTH - PADDLE_WIDTH - BALL_RADIUS and paddle2_pos - BALL_RADIUS <= ball_pos[
                1] <= paddle2_pos + PADDLE_HEIGHT + BALL_RADIUS):
        ball_vel[0] = -ball_vel[0]
        ball.play()

    screen.fill(place)
    pygame.draw.line(screen, WHITE, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(screen, WHITE, [PADDLE_WIDTH, 0], [PADDLE_WIDTH, HEIGHT], 1)
    pygame.draw.line(screen, WHITE, [WIDTH - PADDLE_WIDTH, 0], [WIDTH - PADDLE_WIDTH, HEIGHT], 1)
    pygame.draw.circle(screen, WHITE, [WIDTH // 2, HEIGHT // 2], 50, 1)
    pygame.draw.circle(screen, WHITE, [WIDTH // 2, HEIGHT // 2], 2)
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
    if score1 < 10:
        screen.blit(shrift.render(f'{score1} : {score2}', 1, (190, 190, 190)), (364, 350))
    else:
        screen.blit(shrift.render(f'{score1} : {score2}', 1, (190, 190, 190)), (344, 350))
    pygame.display.flip()
    clock.tick(FPS)
