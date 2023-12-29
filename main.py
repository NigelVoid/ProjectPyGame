import pygame
import runpy
from sys import exit
pygame.init()
win = pygame.display.set_mode((1000, 600))
flag = True
fons = [pygame.image.load('images/фон.png'), pygame.image.load('images/фон2.png')]
c = 0
pygame.display.set_caption('Mini Mini Games')
mouse_position = 0
change_music = False
pygame.mixer.music.load('music/music_fon1.wav')
pygame.mixer.music.play(-1)
show_games = False

while flag:
    win.blit(fons[int(c)], (0, 0))
    win.blit(pygame.image.load('images/logo.png'), (300, 50))
    win.blit(pygame.image.load('images/change_music.png'), (20, 30))
    win.blit(pygame.image.load('images/buttons/start_button.png'), (20, 220))
    pygame.draw.rect(win, (255, 0, 0), (20, 320, 300, 80), 4)
    win.blit(pygame.image.load('images/buttons/ach_button.png'), (20, 320))
    c += 0.25
    if c == 2:
        c = 0
    if show_games:
        pygame.draw.rect(win, (180, 180, 180), (325, 50, 350, 500))
        win.blit(pygame.image.load('images/buttons/close_games.png'), (615, 50))
        pygame.draw.rect(win, (0, 255, 0), (340, 130, 250, 80), 4)
        win.blit(pygame.image.load('images/hungry_fat_man_logo.png'), (340, 130))
        pygame.draw.rect(win, (255, 255, 0), (340, 230, 250, 80), 4)
        win.blit(pygame.image.load('images/ПОЧТА РОССИИ_лого.png'), (340, 230))
        pygame.draw.rect(win, (0, 255, 0), (340, 330, 250, 80), 4)
        win.blit(pygame.image.load('images/ping-pong_logo.png'), (340, 330))
        pygame.draw.rect(win, (0, 255, 0), (340, 430, 250, 80), 4)
    if change_music:
        pygame.draw.rect(win, (150, 150, 150), (140, 30, 290, 100))
        pygame.draw.rect(win, (0, 0, 0), (160, 45, 70, 70))
        pygame.draw.rect(win, (0, 0, 0), (250, 45, 70, 70))
        pygame.draw.rect(win, (0, 0, 0), (340, 45, 70, 70))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            exit()
        elif event.type == pygame.MOUSEMOTION:
            mouse_position = event.pos
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 20 <= mouse_position[0] <= 120 and 30 <= mouse_position[1] <= 130:
                if not change_music:
                    change_music = True
                else:
                    change_music = False
            if 20 <= mouse_position[0] <= 320 and 220 <= mouse_position[1] <= 300:
                show_games = True
            if show_games:
                if 615 <= mouse_position[0] <= 675 and 50 <= mouse_position[1] <= 110:
                    show_games = False
                elif 340 <= mouse_position[0] <= 590 and 130 <= mouse_position[1] <= 210:
                    pygame.mixer.music.stop()
                    runpy.run_module('GAME1')
                elif 340 <= mouse_position[0] <= 590 and 230 <= mouse_position[1] <= 310:
                    pygame.mixer.music.stop()
                    pygame.display.set_icon(pygame.image.load('images/icons/иконка2.bmp'))
                    runpy.run_module('GAME2')
                elif 340 <= mouse_position[0] <= 590 and 330 <= mouse_position[1] <= 410:
                    pygame.mixer.music.stop()
                    runpy.run_module('GAME3')
                elif 340 <= mouse_position[0] <= 590 and 330 <= mouse_position[1] <= 510:
                    pygame.mixer.music.stop()
                    runpy.run_module('GAME4')
            if change_music:
                if 160 <= mouse_position[0] <= 230 and 45 <= mouse_position[1] <= 115:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('music/music_fon1.wav')
                    pygame.mixer.music.play(-1)
                elif 250 <= mouse_position[0] <= 320 and 45 <= mouse_position[1] <= 115:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('music/music_fon2.wav')
                    pygame.mixer.music.play(-1)
                elif 340 <= mouse_position[0] <= 410 and 45 <= mouse_position[1] <= 115:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load('music/music_fon3.wav')
                    pygame.mixer.music.play(-1)

    pygame.display.update()
