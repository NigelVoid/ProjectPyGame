import datetime
import runpy
from datetime import datetime, timedelta
import pygame
import random

pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ПОЧТА РОССИИ')
pygame.display.set_icon(pygame.image.load('images/icons/logo.png'))

class object1:
    def __init__(self):
        self.role = random.randint(1, 2)
        self.y = random.randint(y - 50, y + 100)
        self.warning = pygame.Surface((800, 60))
        self.warning.fill((255, 0, 0))
        self.warning.set_alpha(100)
        if self.role == 2:
            self.y = random.randint(250, 500)
            self.warning = pygame.Surface((60, 80))
            self.warning.fill((255, 0, 0))
            self.warning.set_alpha(100)
        self.t = datetime.now()
        self.delta = timedelta(seconds=1)
        self.x = 800
        self.shot = False
        self.hole = False

    def draw(self):
        global y, stop
        if not stop:
            if self.role == 1:
                if datetime.now() < self.t + self.delta:
                    win.blit(self.warning, (0, self.y))
                else:
                    if not self.shot:
                        shot.play()
                        self.shot = True
                    self.x -= 45
                    win.blit(pygame.image.load('images/квас.png'), (self.x, self.y))
                    if 160 < self.x < 360 and y + 80 > self.y > y:
                        stop = True
                    if self.x < -300:
                        self.role = random.randint(1, 2)
                        self.y = random.randint(y - 50, y + 100)
                        self.warning = pygame.Surface((800, 60))
                        self.warning.fill((255, 0, 0))
                        self.warning.set_alpha(100)
                        if self.role == 2:
                            self.y = random.randint(250, 500)
                            self.warning = pygame.Surface((60, 80))
                            self.warning.fill((255, 0, 0))
                            self.warning.set_alpha(100)
                        self.x = 800
                        self.t = datetime.now()
                        self.delta = timedelta(seconds=1)
                        self.shot = False

            if self.role == 2:
                if datetime.now() < self.t + self.delta:
                    win.blit(self.warning, (self.x - 60, self.y))
                else:
                    if not self.hole:
                        hole.play()
                        self.hole = True
                    self.x -= 20
                    win.blit(pygame.image.load('images/дыра.png'), (self.x, self.y))
                    if 260 < self.x < 360 and (self.y < y + 80 < self.y + 80 or self.y < y + 85 < self.y + 80):
                        stop = True
                    if self.x < -300:
                        self.role = random.randint(1, 2)
                        self.y = random.randint(y - 50, y + 100)
                        self.warning = pygame.Surface((800, 60))
                        self.warning.fill((255, 0, 0))
                        self.warning.set_alpha(100)
                        if self.role == 2:
                            self.y = random.randint(250, 500)
                            self.warning = pygame.Surface((60, 80))
                            self.warning.fill((255, 0, 0))
                            self.warning.set_alpha(100)
                        self.x = 800
                        self.t = datetime.now()
                        self.delta = timedelta(seconds=1)
                        self.hole = False


class object2:
    def __init__(self):
        self.role = random.randint(1, 2)
        self.y = random.randint(y - 50, y + 100)
        self.warning = pygame.Surface((800, 60))
        self.warning.fill((255, 0, 0))
        self.warning.set_alpha(100)
        if self.role == 2:
            self.y = random.randint(250, 500)
            self.warning = pygame.Surface((60, 80))
            self.warning.fill((255, 0, 0))
            self.warning.set_alpha(100)
        self.t = datetime.now()
        self.delta = timedelta(seconds=1)
        self.x = 800
        self.shot = False
        self.hole = False

    def draw(self):
        global y, stop
        if not stop:
            if self.role == 1:
                if datetime.now() < self.t + self.delta:
                    win.blit(self.warning, (0, self.y))
                else:
                    if not self.shot:
                        shot.play()
                        self.shot = True
                    self.x -= 45
                    win.blit(pygame.image.load('images/квас.png'), (self.x, self.y))
                    if 160 < self.x < 360 and y + 80 > self.y > y:
                        stop = True
                    if self.x < -300:
                        self.role = random.randint(1, 2)
                        self.y = random.randint(y - 50, y + 100)
                        self.warning = pygame.Surface((800, 60))
                        self.warning.fill((255, 0, 0))
                        self.warning.set_alpha(100)
                        if self.role == 2:
                            self.y = random.randint(250, 500)
                            self.warning = pygame.Surface((60, 80))
                            self.warning.fill((255, 0, 0))
                            self.warning.set_alpha(100)
                        self.x = 800
                        self.t = datetime.now()
                        self.delta = timedelta(seconds=1)
                        self.shot = False

            if self.role == 2:
                if datetime.now() < self.t + self.delta:
                    win.blit(self.warning, (self.x - 60, self.y))
                else:
                    if not self.hole:
                        hole.play()
                        self.hole = True
                    self.x -= 20
                    win.blit(pygame.image.load('images/дыра.png'), (self.x, self.y))
                    if 260 < self.x < 360 and (self.y < y + 80 < self.y + 80 or self.y < y + 85 < self.y + 80):
                        stop = True
                    if self.x < -300:
                        self.role = random.randint(1, 2)
                        self.y = random.randint(y - 50, y + 100)
                        self.warning = pygame.Surface((800, 60))
                        self.warning.fill((255, 0, 0))
                        self.warning.set_alpha(100)
                        if self.role == 2:
                            self.y = random.randint(250, 500)
                            self.warning = pygame.Surface((60, 80))
                            self.warning.fill((255, 0, 0))
                            self.warning.set_alpha(100)
                        self.x = 800
                        self.t = datetime.now()
                        self.delta = timedelta(seconds=1)
                        self.hole = False


class object3:
    def __init__(self):
        self.role = random.randint(1, 2)
        self.y = random.randint(y - 50, y + 100)
        self.warning = pygame.Surface((800, 60))
        self.warning.fill((255, 0, 0))
        self.warning.set_alpha(100)
        if self.role == 2:
            self.y = random.randint(250, 500)
            self.warning = pygame.Surface((60, 80))
            self.warning.fill((255, 0, 0))
            self.warning.set_alpha(100)
        self.t = datetime.now()
        self.delta = timedelta(seconds=1)
        self.x = 800
        self.shot = False
        self.hole = False

    def draw(self):
        global y, stop
        if not stop:
            if self.role == 1:
                if datetime.now() < self.t + self.delta:
                    win.blit(self.warning, (0, self.y))
                else:
                    if not self.shot:
                        shot.play()
                        self.shot = True
                    self.x -= 45
                    win.blit(pygame.image.load('images/квас.png'), (self.x, self.y))
                    if 160 < self.x < 360 and y + 80 > self.y > y:
                        stop = True
                    if self.x < -300:
                        self.role = random.randint(1, 2)
                        self.y = random.randint(y - 50, y + 100)
                        self.warning = pygame.Surface((800, 60))
                        self.warning.fill((255, 0, 0))
                        self.warning.set_alpha(100)
                        if self.role == 2:
                            self.y = random.randint(250, 500)
                            self.warning = pygame.Surface((60, 80))
                            self.warning.fill((255, 0, 0))
                            self.warning.set_alpha(100)
                        self.x = 800
                        self.t = datetime.now()
                        self.delta = timedelta(seconds=1)
                        self.shot = False

            if self.role == 2:
                if datetime.now() < self.t + self.delta:
                    win.blit(self.warning, (self.x - 60, self.y))
                else:
                    if not self.hole:
                        hole.play()
                        self.hole = True
                    self.x -= 20
                    win.blit(pygame.image.load('images/дыра.png'), (self.x, self.y))
                    if 260 < self.x < 360 and (self.y < y + 80 < self.y + 80 or self.y < y + 85 < self.y + 80):
                        stop = True
                    if self.x < -300:
                        self.role = random.randint(1, 2)
                        self.y = random.randint(y - 50, y + 100)
                        self.warning = pygame.Surface((800, 60))
                        self.warning.fill((255, 0, 0))
                        self.warning.set_alpha(100)
                        if self.role == 2:
                            self.y = random.randint(250, 500)
                            self.warning = pygame.Surface((60, 80))
                            self.warning.fill((255, 0, 0))
                            self.warning.set_alpha(100)
                        self.x = 800
                        self.t = datetime.now()
                        self.delta = timedelta(seconds=1)
                        self.hole = False


class object4:
    def __init__(self):
        self.warning = pygame.Surface((80, 80))
        self.warning.fill((255, 0, 0))
        self.warning.set_alpha(100)
        self.y = -300
        self.con_y = random.randint(200, 520)
        self.x = random.randint(200, 700)
        self.t = datetime.now()
        self.delta = timedelta(seconds=1)
        self.bread = False

    def draw(self):
        global y, stop
        if not stop:
            if datetime.now() <= self.t + self.delta:
                win.blit(self.warning, (self.x, self.con_y))
            if self.y + 200 < self.con_y:
                self.y += 10
                win.blit(pygame.image.load('images/хлеб.png'), (self.x, self.y))
                if not self.bread:
                    bread.play()
                    self.bread = True
            elif self.x > 0:
                self.x -= 20
                win.blit(pygame.image.load('images/хлеб2.png'), (self.x, self.con_y))
                if 260 < self.x < 360 and (
                        self.con_y < y + 50 < self.con_y + 80 or self.con_y < y + 70 < self.con_y + 80):
                    stop = True
            else:
                self.y = -300
                self.con_y = random.randint(200, 520)
                self.x = random.randint(200, 700)
                self.t = datetime.now()
                self.delta = timedelta(seconds=1)
                self.bread = False


class object5:
    def __init__(self):
        self.warning = pygame.Surface((80, 80))
        self.warning.fill((255, 0, 0))
        self.warning.set_alpha(100)
        self.y = -300
        self.con_y = random.randint(200, 520)
        self.x = random.randint(200, 700)
        self.t = datetime.now()
        self.delta = timedelta(seconds=1)
        self.bread = False

    def draw(self):
        global y, stop
        if not stop:
            if datetime.now() <= self.t + self.delta:
                win.blit(self.warning, (self.x, self.con_y))
            if self.y + 200 < self.con_y:
                self.y += 10
                win.blit(pygame.image.load('images/хлеб.png'), (self.x, self.y))
                if not self.bread:
                    bread.play()
                    self.bread = True
            elif self.x > 0:
                self.x -= 20
                win.blit(pygame.image.load('images/хлеб2.png'), (self.x, self.con_y))
                if 260 < self.x < 360 and (
                        self.con_y < y + 50 < self.con_y + 80 or self.con_y < y + 70 < self.con_y + 80):
                    stop = True
            else:
                self.y = -300
                self.con_y = random.randint(200, 520)
                self.x = random.randint(200, 700)
                self.t = datetime.now()
                self.delta = timedelta(seconds=1)
                self.bread = False


flag = True
shrift = pygame.font.SysFont('arial', 30)
fons = [pygame.image.load('images/fons_pr/fon_pr(1).png'), pygame.image.load('images/fons_pr/fon_pr(2).png'),
        pygame.image.load('images/fons_pr/fon_pr(3).png')]
prcar = [pygame.image.load('images/prcar(1).png'), pygame.image.load('images/prcar(2).png'),
         pygame.image.load('images/prcar(3).png'), pygame.image.load('images/prcar(4).png')]
x1 = 0
x2 = 800
x3 = 800
rx1 = 0
rx2 = 800
y = 450
c = 0
pygame.mixer.music.load('music/pr.mp3')
pygame.mixer.music.play(-1)
obj1 = object1()
create2 = False
obj2 = ''
create3 = False
obj3 = ''
create4 = False
create5 = False
obj4 = ''
obj5 = ''
stop = False
t = datetime.now()
skip = False
win_t = False
t2 = ''
skip_game = False
shot = pygame.mixer.Sound('music/pr/пиу.mp3')
hole = pygame.mixer.Sound('music/pr/дыра.mp3')
bread = pygame.mixer.Sound('music/pr/хлеб.mp3')
while flag:
    win.fill((135, 206, 235))
    keys = pygame.key.get_pressed()
    pygame.draw.rect(win, (128, 128, 128), (0, 120, 800, 130))
    if not stop:
        x1 -= 20
        x2 -= 20
        x3 -= 20
    win.blit(fons[0], (x1, 0))
    win.blit(fons[1], (x2, 0))
    win.blit(fons[2], (x3, 0))
    if x1 == -800:
        x1 = 800
    if x2 == -800:
        x2 = 800
    if x3 == -800:
        x3 = 800
    pygame.draw.rect(win, (255, 255, 255), (0, 250, 800, 350), 4)
    if not stop:
        rx1 -= 20
        rx2 -= 20
    win.blit(pygame.image.load('images/road.png'), (rx1, 250))
    win.blit(pygame.image.load('images/road.png'), (rx2, 250))
    if rx1 == -800:
        rx1 = 800
    if rx2 == -800:
        rx2 = 800
    if not stop:
        if keys[pygame.K_w]:
            if y + 100 - 7 >= 250:
                y -= 7
        if keys[pygame.K_s]:
            if y + 100 + 7 <= 600:
                y += 7
    if not skip_game and (not datetime.now() > t + timedelta(seconds=80) and not skip):
        obj1.draw()
        if datetime.now() > t + timedelta(seconds=10):
            if not create2:
                obj2 = object2()
                create2 = True
            obj2.draw()
        if datetime.now() > t + timedelta(seconds=40):
            if not create3:
                obj3 = object3()
                create3 = True
            obj3.draw()
    if not stop:
        win.blit(prcar[int(c)], (160, y))
    else:
        win.blit(pygame.image.load('images/prcarcrash.png'), (160, y))
    if not stop:
        if c + 0.5 < 4:
            c += 0.5
        else:
            c = 0
    if not skip_game and (datetime.now() > t + timedelta(seconds=80) or skip):
        if not create4:
            obj4 = object4()
            create4 = True
        if not create5:
            obj5 = object5()
            create5 = True
        obj4.draw()
        obj5.draw()
    if datetime.now() > t + timedelta(seconds=120) or skip_game:
        if not win_t:
            t2 = datetime.now()
            win_t = True
        win.blit(pygame.image.load('images/win_pr.png'), (0, 0))
        with open('PR.txt', mode='w', encoding='utf8') as f:
            print('rbnghjbrrghjrgrbngkrhjbgrejkbgeruigbrejghbnergjrehngreuhngujikregbnhrujikwaghliufhuiawhf', file=f)
            print('erhuighreguihreguhreuigherui9ghuirhg9uwhu9erhguigyes', file=f)
        if datetime.now() >= t2 + timedelta(seconds=5):
            flag = False
            runpy.run_module('main')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
            runpy.run_module('main')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                flag = False
                runpy.run_module('GAME2')
            elif event.key == pygame.K_t:
                skip = True
            elif event.key == pygame.K_m:
                skip_game = True
    win.blit(shrift.render('Управление: [W] и [S], чтобы двигаться. [R], чтобы начать сначала.', 1, (0, 0, 0)),
             (10, 550))
    pygame.display.update()
