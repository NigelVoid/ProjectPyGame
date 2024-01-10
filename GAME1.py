import runpy

import pygame
import random

pygame.init()
win = pygame.display.set_mode((500, 600))
pygame.display.set_caption('HUNGRY FAT MAN')

flag = True
x = 200
y = 450
shrift = pygame.font.SysFont('arial', 25)
points = 0
images = [pygame.image.load('images/food.png'), pygame.image.load('images/bomb.png')]
wr = [pygame.image.load('images/fat_man_walk1(1).png'), pygame.image.load('images/fat_man_walk1(2).png')]
wl = [pygame.image.load('images/fat_man_walk2(1).png'), pygame.image.load('images/fat_man_walk2(2).png')]
right = False
left = False
anim = 0
stpos = 'right'
record = ''
pygame.mixer.music.load('music/hfm.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
with open('hfm.txt', mode='r', encoding='utf8') as f:
    l = f.readlines()
    record = int((l[0].rstrip())[80:])


class Object1:
    def __init__(self):
        self.x = random.randint(0, 450)
        self.y = random.randint(-500, -100)
        self.role = random.randint(0, 1)

    def draw(self):
        global x, y, points, images
        if not pause:
            self.y += 5
            if points > 3000:
                self.y += 3
            if points > 7000:
                self.y += 3
            if points > 10000:
                self.y += 3
            if points > 20000:
                self.y += 3
            if points > 30000:
                self.y += 3
            win.blit(images[self.role], (self.x, self.y))
            if self.y > y:
                self.x = random.randint(0, 450)
                self.y = random.randint(-300, -100)
                self.role = random.randint(0, 1)
            if (x < self.x < x + 80 and y < self.y + 50 < y + 100) or (
                    x < self.x + 50 < x + 80 and y < self.y + 50 < y + 100):
                if self.role == 0:
                    points += 60
                else:
                    points -= 240
                self.x = random.randint(0, 450)
                self.y = random.randint(-500, -100)
                self.role = random.randint(0, 1)


class Object2:
    def __init__(self):
        self.x = random.randint(0, 450)
        self.y = random.randint(-500, -100)
        self.role = random.randint(0, 1)

    def draw(self):
        global x, y, points, images
        if not pause:
            self.y += 5
            if points > 3000:
                self.y += 3
            if points > 7000:
                self.y += 3
            if points > 10000:
                self.y += 3
            if points > 20000:
                self.y += 3
            if points > 30000:
                self.y += 3
            win.blit(images[self.role], (self.x, self.y))
            if self.y > y:
                self.x = random.randint(0, 450)
                self.y = random.randint(-300, -100)
                self.role = random.randint(0, 1)
            if (x < self.x < x + 80 and y < self.y + 50 < y + 100) or (
                    x < self.x + 50 < x + 80 and y < self.y + 50 < y + 100):
                if self.role == 0:
                    points += 60
                else:
                    points -= 240
                self.x = random.randint(0, 450)
                self.y = random.randint(-500, -100)
                self.role = random.randint(0, 1)


class Object3:
    def __init__(self):
        self.x = random.randint(0, 450)
        self.y = random.randint(-500, -100)
        self.role = random.randint(0, 1)

    def draw(self):
        global x, y, points, images
        if not pause:
            self.y += 5
            if points > 3000:
                self.y += 3
            if points > 7000:
                self.y += 3
            if points > 10000:
                self.y += 3
            if points > 20000:
                self.y += 3
            if points > 30000:
                self.y += 3
            win.blit(images[self.role], (self.x, self.y))
            if self.y > y:
                self.x = random.randint(0, 450)
                self.y = random.randint(-300, -100)
                self.role = random.randint(0, 1)
            if (x < self.x < x + 80 and y < self.y + 50 < y + 100) or (
                    x < self.x + 50 < x + 80 and y < self.y + 50 < y + 100):
                if self.role == 0:
                    points += 60
                else:
                    points -= 240
                self.x = random.randint(0, 450)
                self.y = random.randint(-500, -100)
                self.role = random.randint(0, 1)


class Object4:
    def __init__(self):
        self.x = random.randint(0, 450)
        self.y = random.randint(-500, -100)
        self.role = random.randint(0, 1)

    def draw(self):
        global x, y, points, images
        if not pause:
            self.y += 5
            if points > 3000:
                self.y += 3
            if points > 7000:
                self.y += 3
            if points > 10000:
                self.y += 3
            if points > 20000:
                self.y += 3
            if points > 30000:
                self.y += 3
            win.blit(images[self.role], (self.x, self.y))
            if self.y > y:
                self.x = random.randint(0, 450)
                self.y = random.randint(-300, -100)
                self.role = random.randint(0, 1)
            if (x < self.x < x + 80 and y < self.y + 50 < y + 100) or (
                    x < self.x + 50 < x + 80 and y < self.y + 50 < y + 100):
                if self.role == 0:
                    points += 60
                else:
                    points -= 240
                self.x = random.randint(0, 450)
                self.y = random.randint(-500, -100)
                self.role = random.randint(0, 1)


class Object5:
    def __init__(self):
        self.x = random.randint(0, 450)
        self.y = random.randint(-500, -100)
        self.role = random.randint(0, 1)

    def draw(self):
        global x, y, points, images
        if not pause:
            self.y += 5
            if points > 3000:
                self.y += 3
            if points > 7000:
                self.y += 3
            if points > 10000:
                self.y += 3
            if points > 20000:
                self.y += 3
            if points > 30000:
                self.y += 3
            win.blit(images[self.role], (self.x, self.y))
            if self.y > y:
                self.x = random.randint(0, 450)
                self.y = random.randint(-300, -100)
                self.role = random.randint(0, 1)
            if (x < self.x < x + 80 and y < self.y + 50 < y + 100) or (
                    x < self.x + 50 < x + 80 and y < self.y + 50 < y + 100):
                if self.role == 0:
                    points += 60
                else:
                    points -= 240
                self.x = random.randint(0, 450)
                self.y = random.randint(-500, -100)
                self.role = random.randint(0, 1)


object1 = Object1()
object2 = Object2()
object3 = Object3()
object4 = Object4()
object5 = Object5()
pause = False
while flag:
    left = False
    right = False
    pygame.time.delay(30)
    win.blit(pygame.image.load('images/фон_fat_man.jpg'), (0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and not pause:
        if x - 10 >= 0:
            x -= 10
        left = True
        right = False
        stpos = 'left'
    if keys[pygame.K_d] and not pause:
        if x + 80 + 10 <= 500:
            x += 10
        right = True
        left = False
        stpos = 'right'
    if anim + 1 >= 10:
        anim = 0
    if right:
        win.blit(wr[int(anim // 5)], (x, y))
        anim += 1
    elif left:
        win.blit(wl[int(anim // 5)], (x, y))
        anim += 1
    else:
        if stpos == 'right':
            win.blit(pygame.image.load('images/fat_man_stand1.png'), (x, y))
        elif stpos == 'left':
            win.blit(pygame.image.load('images/fat_man_stand2.png'), (x, y))
    object1.draw()
    object2.draw()
    object3.draw()
    object4.draw()
    object5.draw()
    win.blit(shrift.render(f'Счёт: {points}', 1, (255, 255, 255)), (10, 20))
    win.blit(shrift.render(f'Рекорд: {record}', 1, (255, 255, 255)), (10, 60))
    win.blit(shrift.render(f'Управление: влево[A] и вправо[D], пауза[P]', 1, (0, 0, 0)), (10, 570))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if points > int(record):
                with open('hfm.txt', mode='w', encoding='utf8') as f:
                    print(f'pokgpo[erkgergklreklgker0-kg0reg856945860=wgotkhojkethkjorthkty0nk0-jo-0tojo-=th{points}',
                          file=f)
            flag = False
            runpy.run_module('main')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause = not pause

    pygame.display.update()
