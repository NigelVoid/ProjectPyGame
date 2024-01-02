import runpy

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 400
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 150, 100),
    32: (245, 125, 95),
    64: (245, 95, 60),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}

FONT = pygame.font.Font(None, 64)

GRID_SIZE = 4

grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]


def generate_number():
    if any(0 in row for row in grid):
        while True:
            x = random.randint(0, GRID_SIZE - 1)
            y = random.randint(0, GRID_SIZE - 1)
            if grid[x][y] == 0:
                grid[x][y] = random.choice([2, 4])
                break


def draw_grid():
    WINDOW.fill(BACKGROUND_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            number = grid[row][col]
            color = TILE_COLORS.get(number, (255, 255, 255))
            pygame.draw.rect(WINDOW, color, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            if number != 0:
                text_surface = FONT.render(str(number), True, (0, 0, 0))
                text_rect = text_surface.get_rect(
                    center=(col * TILE_SIZE + TILE_SIZE / 2, row * TILE_SIZE + TILE_SIZE / 2))
                WINDOW.blit(text_surface, text_rect)


def move_left():
    for row in range(GRID_SIZE):
        for col in range(1, GRID_SIZE):
            if grid[row][col] != 0:
                x = col
                while x > 0 and grid[row][x - 1] == 0:
                    grid[row][x - 1] = grid[row][x]
                    grid[row][x] = 0
                    x -= 1
                if x > 0 and grid[row][x - 1] == grid[row][x]:
                    grid[row][x - 1] *= 2
                    grid[row][x] = 0


def move_left():
    for row in range(GRID_SIZE):
        for col in range(1, GRID_SIZE):
            if grid[row][col] != 0:
                x = col
                while x > 0 and grid[row][x - 1] == 0:
                    grid[row][x - 1] = grid[row][x]
                    grid[row][x] = 0
                    x -= 1
                if x > 0 and grid[row][x - 1] == grid[row][x]:
                    grid[row][x - 1] *= 2
                    grid[row][x] = 0


def move_right():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE - 2, -1, -1):
            if grid[row][col] != 0:
                x = col
                while x < GRID_SIZE - 1 and grid[row][x + 1] == 0:
                    grid[row][x + 1] = grid[row][x]
                    grid[row][x] = 0
                    x += 1
                if x < GRID_SIZE - 1 and grid[row][x + 1] == grid[row][x]:
                    grid[row][x + 1] *= 2
                    grid[row][x] = 0


def move_up():
    for col in range(GRID_SIZE):
        for row in range(1, GRID_SIZE):
            if grid[row][col] != 0:
                y = row
                while y > 0 and grid[y - 1][col] == 0:
                    grid[y - 1][col] = grid[y][col]
                    grid[y][col] = 0
                    y -= 1
                if y > 0 and grid[y - 1][col] == grid[y][col]:
                    grid[y - 1][col] *= 2
                    grid[y][col] = 0


def move_down():
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE - 2, -1, -1):
            if grid[row][col] != 0:
                y = row
                while y < GRID_SIZE - 1 and grid[y + 1][col] == 0:
                    grid[y + 1][col] = grid[y][col]
                    grid[y][col] = 0
                    y += 1
                if y < GRID_SIZE - 1 and grid[y + 1][col] == grid[y][col]:
                    grid[y + 1][col] *= 2
                    grid[y][col] = 0


def handle_events():
    global flag
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            runpy.run_module('main')
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                move_left()
                generate_number()
            if event.key == pygame.K_RIGHT:
                move_right()
                generate_number()
            if event.key == pygame.K_UP:
                move_up()
                generate_number()
            if event.key == pygame.K_DOWN:
                move_down()
                generate_number()


TILE_SIZE = WIDTH // GRID_SIZE
generate_number()
flag = True
while flag:
    handle_events()
    draw_grid()
    pygame.display.update()
