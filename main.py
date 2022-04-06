import pygame
import random
import math
import sqlite3

con = sqlite3.connect('records.sqlite')
cur = con.cursor()
pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ultra cs aim assister')
sprite = pygame.sprite.Sprite()
all_sprites = pygame.sprite.Group()
col_vo_balls = 30
radius = 35
default_color_screen = 'black'
color_screen = 'black'
fullness_ball = 0
color_ball = 'white'

default_color_ball = pygame.color.Color('white')
default_radius_ball = 35
default_width_ball = 1
default_fulness_ball = 0
default_col_vo = 30
radius_ball = default_radius_ball
width_ball = default_width_ball
fulness_ball = default_fulness_ball

rectangle_menu = pygame.Rect(width - width / 5, height - height / 10,
                             width / 5, height / 10)
v = 1
time = 0
start = pygame.time.get_ticks()

pygame.draw.circle(screen, 'white', (width / 2, height / 2), height / 10, 1)
text = 'Start'
f = pygame.font.Font(None, 40)
text = f.render(text, True, 'white')
pos = text.get_rect(center=(width / 2, height / 2))
screen.blit(text, pos)
col_vo = default_col_vo

horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()

begin = 1
to_menu = 0
to_settings = 0
to_records = 0
to_intro = 0
to_gameplay = 0
to_results = 0
clicked = 0
end_click = 0
to_exit = 0

running = True
clock = pygame.time.Clock()
FPS = 120


class Menu:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 200
        self.top = 100
        self.cell_size = 150
        self.text_x = 200
        self.text_y = 150

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        texts = ['play', 'settings', 'records', 'exit']
        text_x = self.text_x
        text_y = self.text_y
        cur_left = self.left
        cur_top = self.top
        for i in self.board:
            for x in i:
                pygame.draw.rect(screen, (255, 255, 255), (cur_left, cur_top, self.cell_size, self.cell_size), 1)
                cur_left += self.cell_size
            cur_top += self.cell_size
            cur_left = self.left
        for _ in texts:
            font = pygame.font.Font(None, 50)
            text = font.render(_, True, (255, 255, 255))
            screen.blit(text, (text_x, text_y))
            text_y += 150

    def click(self, mouse_pos):
        ret = 0
        if 200 <= mouse_pos[0] <= 350:
            if 100 < mouse_pos[1] < 250:
                ret = 1
            elif 250 < mouse_pos[1] < 400:
                ret = 2
            elif 400 < mouse_pos[1] < 550:
                ret = 3
            elif 550 < mouse_pos[1] < 700:
                ret = 4
        return ret


class Game:
    def __init__(self, color_ball, radius_ball, width_ball, fulness_ball, width, height, screen):
        self.color_ball = color_ball
        self.radius_ball = radius_ball
        self.width_ball = width_ball
        self.fulness_ball = fulness_ball
        self.width = width
        self.height = height
        self.coord_x = width / 2
        self.coord_y = height / 2
        self.width_right = self.width - self.radius_ball
        self.width_left = self.radius_ball
        self.height_top = self.radius_ball
        self.height_bottom = self.height - self.radius_ball
        self.screen = screen

    def render(self):
        if self.fulness_ball == 0:
            pygame.draw.circle(self.screen, self.color_ball, (self.width / 2, self.height / 2),
                               self.radius_ball, self.width_ball)
        elif self.fulness_ball == 1:
            self.width_ball = 0
            pygame.draw.circle(self.screen, self.color_ball, (self.width / 2, self.height / 2),
                               self.radius_ball, self.width_ball)

    def update(self):
        self.coord_x = random.randint(self.width_left, self.width_right)
        self.coord_y = random.randrange(self.height_top, self.height_bottom)
        pygame.draw.circle(self.screen, self.color_ball, (self.coord_x, self.coord_y),
                           self.radius_ball, self.width_ball)

    def return_pos(self):
        return self.coord_x, self.coord_y

    def end(self, time, rectangle):
        self.time = str(round(time, 3))
        self.f = pygame.font.Font(None, 50)
        self.text = 'Time - ' + self.time + ' sec'
        self.text = self.f.render(self.text, True, 'Green')
        self.pos = self.text.get_rect(center=(width / 2, height / 2))
        screen.blit(self.text, self.pos)
        self.f = pygame.font.Font(None, 25)
        self.text = 'Back to menu'
        self.text = self.f.render(self.text, True, 'Green')
        self.rectangle = rectangle
        self.pos = self.text.get_rect(center=(self.width - self.width / 10, self.height - self.height / 20))
        pygame.draw.rect(self.screen, 'green', self.rectangle, 1)
        screen.blit(self.text, self.pos)


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y, colvo_stolknoveniy):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color('white'),
                           (radius, radius), radius, 1)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = random.randint(-10, 10)
        if self.vx == 0:
            self.vx = random.randint(-10, 10)
        self.vy = random.randrange(-10, 10)
        if self.vy == 0:
            self.vy = random.randint(-10, 10)
        self.colvo_stolknoveniy = colvo_stolknoveniy

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)
        if pygame.sprite.spritecollideany(self, horizontal_borders):
            self.vy = -self.vy
            self.colvo_stolknoveniy += 1
        if pygame.sprite.spritecollideany(self, vertical_borders):
            self.vx = -self.vx
            self.colvo_stolknoveniy += 1
        if self.colvo_stolknoveniy == 2:
            self.kill()


class Border(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)


class Records:
    def __init__(self):
        self.y = 100

    def render(self, screen):
        data = list(cur.execute("""SELECT * FROM records"""))
        f = pygame.font.Font(None, 40)
        title_text = f.render('Records', True, 'white')
        tps_text = f.render('targets per second', True, 'white')
        time_text = f.render('time', True, 'white')
        button_text = f.render('go to menu', True, 'white')
        screen.blit(title_text, (450, 20))
        screen.blit(time_text, (400, 50))
        screen.blit(tps_text, (500, 50))
        times = []
        tpss = []
        for _ in data:
            time = f.render(str(_[0]), True, 'white')
            tps = f.render(str(_[1]), True, 'white')
            times.append(time)
            tpss.append(tps)
        screen.blit(times[0], (400, self.y))
        screen.blit(tpss[0], (550, self.y))
        screen.blit(times[1], (400, self.y + 50))
        screen.blit(tpss[1], (550, self.y + 50))
        screen.blit(times[2], (400, self.y + 100))
        screen.blit(tpss[2], (550, self.y + 100))
        screen.blit(button_text, (800, 700))
        pygame.draw.rect(screen, 'white', (800, 690, 150, 50), 1)


class Settings:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen

    def draw(self, text, y):
        self.y = y
        self.text = text
        self.rect = pygame.Rect(self.width / 20, self.y, self.width / 10, self.height / 20)
        self.rect_minus = pygame.Rect(1, self.y, self.width / 20, self.height / 20)
        self.rect_plus = pygame.Rect(self.width / 20 + self.width / 10, self.y,
                                     self.width / 20, self.height / 20)
        self.f = pygame.font.Font(None, 40)
        self.text_m = '--'
        self.t = self.f.render(self.text_m, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 40 + 1, self.y + self.height / 40))
        pygame.draw.rect(self.screen, 'white', self.rect_minus, 1)
        screen.blit(self.t, self.pos)
        self.text_p = '+'
        self.t = self.f.render(self.text_p, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 20 + self.width / 10 + self.width / 40,
                                           self.y + self.height / 40))
        pygame.draw.rect(self.screen, 'white', self.rect_plus, 1)
        screen.blit(self.t, self.pos)
        self.text = str(self.text)
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 20 + self.width / 20, self.y + self.height / 40))
        pygame.draw.rect(self.screen, 'white', self.rect, 1)
        screen.blit(self.t, self.pos)

    def col_vo(self, col_vo_balls):
        self.col_vo_balls = col_vo_balls
        self.rect_minus_col_vo = pygame.Rect(1, self.height / 20, self.width / 20, self.height / 20)
        self.rect_plus_col_vo = pygame.Rect(self.width / 20 + self.width / 10, self.height / 20,
                                            self.width / 20, self.height / 20)
        Settings.draw(self, self.col_vo_balls, self.height / 20)
        self.text = 'targets'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 10 + self.width / 10 + self.width / 20,
                                           self.height / 20 + self.height / 40))
        screen.blit(self.t, self.pos)

    def radius(self, rad):
        self.rad = str(rad)
        self.rect_minus_rad = pygame.Rect(1, self.height / 20 * 3, self.width / 20, self.height / 20)
        self.rect_plus_rad = pygame.Rect(self.width / 20 + self.width / 10, self.height / 20 * 3,
                                         self.width / 20, self.height / 20)
        Settings.draw(self, self.rad, self.height / 20 * 3)
        self.text = 'radius'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 10 + self.width / 10 + self.width / 20,
                                           self.height / 20 * 3 + self.height / 40))
        screen.blit(self.t, self.pos)

    def fullness_ball(self, fullness_ball):
        self.fullness_ball = fullness_ball
        self.rect_minus_f_b = pygame.Rect(1, self.height / 20 * 5, self.width / 20, self.height / 20)
        self.rect_plus_f_b = pygame.Rect(self.width / 20 + self.width / 10, self.height / 20 * 5,
                                         self.width / 20, self.height / 20)
        Settings.draw(self, self.fullness_ball, self.height / 20 * 5)
        self.text = 'fullness of target'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 10 + self.width / 10 + self.width / 17 * 2,
                                           self.height / 20 * 5 + self.height / 40))
        screen.blit(self.t, self.pos)

    def color(self, color_ball):
        self.color_ball = str(color_ball)
        self.rect_minus_color = pygame.Rect(1, self.height / 20 * 7, self.width / 20, self.height / 20)
        self.rect_plus_color = pygame.Rect(self.width / 20 + self.width / 10, self.height / 20 * 7,
                                           self.width / 20, self.height / 20)
        self.text_colors = ['white', 'red', 'yellow', 'blue', 'green', 'orange', 'purple', 'pink', 'black', 'brown']
        Settings.draw(self, self.color_ball, self.height / 20 * 7)
        self.text = 'target color'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 10 + self.width / 10 + self.width / 25 * 2,
                                           self.height / 20 * 7 + self.height / 40))
        screen.blit(self.t, self.pos)

    def color_sc(self, color_screen):
        self.color_screen = str(color_screen)
        self.rect_minus_color_sc = pygame.Rect(1, self.height / 20 * 9, self.width / 20, self.height / 20)
        self.rect_plus_color_sc = pygame.Rect(self.width / 20 + self.width / 10, self.height / 20 * 9,
                                              self.width / 20, self.height / 20)
        Settings.draw(self, self.color_screen, self.height / 20 * 9)
        self.text_colors_sc = ['black', 'purple', 'grey', 'blue', 'red', 'yellow', 'green']
        self.text = 'screen color'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 10 + self.width / 10 + self.width / 22 * 2,
                                           self.height / 20 * 9 + self.height / 40))
        screen.blit(self.t, self.pos)
        self.colors_sc_rgb = [(0, 0, 0), (148, 0, 211), (190, 190, 190), (0, 121, 219),
                              (239, 48, 56), (253, 219, 109), (138, 255, 138)]

    def warning(self):
        self.text = "Warning! Don't use the same colors!"
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 10 + self.width / 14 * 2, self.height / 1.5))
        screen.blit(self.t, self.pos)

    def circle(self, radius, color, fulness_ball):
        self.fulness_ball = fulness_ball
        self.radius = radius
        self.color = color
        if self.fulness_ball == 0:
            self.fulness_ball = 1
        else:
            self.fulness_ball = 0
        pygame.draw.circle(screen, self.color, (width / 2 + width / 4, height / 4), self.radius, self.fulness_ball)

    def authors(self):
        self.text = ['Authors:', 'https://github.com/timorez', 'github.com/evdakim1234']
        self.y_text = self.height / 1.2
        for i in self.text:
            self.f = pygame.font.Font(None, 30)
            self.t = self.f.render(i, True, 'green')
            self.pos = self.t.get_rect(center=(self.width / 5, self.y_text))
            screen.blit(self.t, self.pos)
            self.y_text += self.height / 40


class Exit:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.rect_dont_exit = pygame.Rect(self.width / 2 - self.width / 4.5, self.height / 2 - self.height / 24,
                                           self.width / 6, self.height / 16)
        self.rect_exit = pygame.Rect(self.width / 2 + self.width / 18, self.height / 2 - self.height / 24,
                                     self.width / 6, self.height / 16)

    def click_exit(self):
        # функция подтверждения\отмены выхода
        pygame.draw.rect(screen, 'white', (self.width / 2 - self.width / 4, self.height / 2 - self.height / 8,
                         self.width / 2, self.height / 5), 1)
        self.rect_dont_exit = pygame.Rect(self.width / 2 - self.width / 4.5, self.height / 2 - self.height / 24,
                                           self.width / 6, self.height / 16)
        pygame.draw.rect(screen, 'white', (self.rect_dont_exit), 1)
        self.rect_exit = pygame.Rect(self.width / 2 + self.width / 18, self.height / 2 - self.height / 24,
                                           self.width / 6, self.height / 16)
        pygame.draw.rect(screen, 'white', self.rect_exit, 1)
        self.f = pygame.font.Font(None, 40)
        self.text = 'Do you want to quit the game?'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 2, self.height / 2.5))
        screen.blit(self.t, self.pos)
        self.f = pygame.font.Font(None, 40)
        self.text = 'NO'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 2 - self.width / 4.5 + self.width / 12,
                                           self.height / 2 - self.height / 24 + self.height / 32))
        screen.blit(self.t, self.pos)
        self.f = pygame.font.Font(None, 40)
        self.text = 'YES'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 2 + self.width / 18 + self.width / 12,
                                           self.height / 2 - self.height / 24 + self.height / 32))
        screen.blit(self.t, self.pos)

    def authors(self):
        # ссылка на авторов в конце
        self.text = ['Authors:', 'https://github.com/timorez', 'https://github.com/evdakim1234']
        self.y_text = self.height / 2 - self.height / 40
        for i in self.text:
            self.f = pygame.font.Font(None, 30)
            self.t = self.f.render(i, True, 'green')
            self.pos = self.t.get_rect(center=(self.width / 2, self.y_text))
            screen.blit(self.t, self.pos)
            self.y_text += self.height / 40
        self.text = 'Thanks for playing!'
        self.f = pygame.font.Font(None, 50)
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 2, self.height / 1.5))
        screen.blit(self.t, self.pos)


settings = Settings(width, height, screen)
settings.col_vo(col_vo_balls)
settings.radius(radius)
settings.color(color_ball)
settings.color_sc(color_screen)
settings.warning()
settings.authors()
settings.circle(radius, color_ball, fullness_ball)
settings.fullness_ball(fullness_ball)
colors_sc_rgb = [(0, 0, 0), (255, 255, 255), (148, 0, 211), (190, 190, 190), (0, 121, 219),
                 (239, 48, 56), (253, 219, 109), (138, 255, 138)]

exit_menu = Exit(width, height)
records = Records()
menu = Menu(1, 4)
game = Game(color_ball, radius_ball, width_ball, fulness_ball, width, height, screen)

Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
for i in range(20):
    Ball(20, width / 2, height / 2, 0)

if __name__ == '__main__':
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x_coord = pygame.mouse.get_pos()[0]
                y_coord = pygame.mouse.get_pos()[1]
                sqx = (x_coord - (width / 2)) ** 2
                sqy = (y_coord - (height / 2)) ** 2
                if (x_coord - game.coord_x) ** 2 + (
                        y_coord - game.coord_y) ** 2 < game.radius_ball ** 2:
                    clicked = 1
                if width - width / 5 <= x_coord <= (width - width / 5) + (width / 5) \
                        and height - height / 10 <= y_coord <= (height - height / 10) + (height / 10) and col_vo == 0:
                    end_click = 1
                if math.sqrt(sqx + sqy) < height / 10 and begin == 1:
                    begin = 0
                    to_intro = 1
                    to_menu = 1
                if to_menu == 1:
                    if menu.click([x_coord, y_coord]) == 1:
                        to_gameplay = 1
                        to_menu = 0
                        to_intro = 0
                        col_vo = default_col_vo
                    elif menu.click([x_coord, y_coord]) == 2:
                        to_menu = 0
                        to_settings = 1
                        to_intro = 0
                    elif menu.click([x_coord, y_coord]) == 3:
                        to_menu = 0
                        to_records = 1
                        to_intro = 0
                    elif menu.click([x_coord, y_coord]) == 4:
                        to_menu = 0
                        to_exit = 1
                if 352 < y_coord < 400 and to_exit == 1:
                    if 284.4444 < x_coord < 455 and to_exit == 1:
                        to_exit = 0
                        to_menu = 1
                        # обратно в главное меню
                    if 568 < x_coord < 740:
                        screen.fill(default_color_screen)
                        f = 1
                        to_exit = 0
                if to_records == 1:
                    if 800 < x_coord < 950 and 690 < y_coord < 740:
                        to_records = 0
                        to_menu = 1
                if to_settings:
                    if 100 < x_coord < 250 and 690 < y_coord < 940:
                        to_settings = 0
                        to_menu = 1
                    if settings.rect_plus_col_vo.collidepoint(pygame.mouse.get_pos()):
                        if col_vo_balls < 200:
                            col_vo_balls += 5
                            default_col_vo += 5
                    if settings.rect_minus_col_vo.collidepoint(pygame.mouse.get_pos()):
                        if col_vo_balls > 5:
                            col_vo_balls -= 5
                            default_col_vo -= 5
                    if settings.rect_plus_rad.collidepoint(pygame.mouse.get_pos()):
                        if radius < 75:
                            radius += 5
                            game.radius_ball += 5
                    if settings.rect_minus_rad.collidepoint(pygame.mouse.get_pos()):
                        if radius > 5:
                            radius -= 5
                            game.radius_ball -= 5
                    if settings.rect_minus_f_b.collidepoint(pygame.mouse.get_pos()):
                        if fullness_ball > 0:
                            fullness_ball -= 1
                            game.width_ball += 1
                    if settings.rect_plus_f_b.collidepoint(pygame.mouse.get_pos()):
                        if fullness_ball < 1:
                            fullness_ball += 1
                            game.width_ball -= 1
                    if settings.rect_minus_color.collidepoint(pygame.mouse.get_pos()):
                        color_ball = settings.text_colors[settings.text_colors.index(color_ball) - 1]
                        game.color_ball = color_ball
                    if settings.rect_plus_color.collidepoint(pygame.mouse.get_pos()):
                        if settings.text_colors.index(color_ball) < 9:
                            color_ball = settings.text_colors[settings.text_colors.index(color_ball) + 1]
                            game.color_ball = color_ball
                        else:
                            color_ball = 'white'
                            game.color_ball = color_ball
                    if settings.rect_minus_color_sc.collidepoint(pygame.mouse.get_pos()):
                        color_screen = settings.text_colors_sc[settings.text_colors_sc.index(color_screen) - 1]
                        default_color_screen = settings.colors_sc_rgb[settings.text_colors_sc.index(color_screen)]
                    if settings.rect_plus_color_sc.collidepoint(pygame.mouse.get_pos()):
                        if settings.text_colors_sc.index(color_screen) < 6:
                            color_screen = settings.text_colors_sc[
                                settings.text_colors_sc.index(color_screen) + 1]
                            default_color_screen = settings.colors_sc_rgb[settings.text_colors_sc.index(color_screen)]
                        else:
                            color_screen = 'black'
                            default_color_screen = 'black'

        screen.fill(default_color_screen)
        if begin == 1:
            pygame.draw.circle(screen, 'white', (width / 2, height / 2), height / 10, 1)
            text = 'Start'
            f = pygame.font.Font(None, 40)
            text = f.render(text, True, 'white')
            pos = text.get_rect(center=(width / 2, height / 2))
            screen.blit(text, pos)
        if to_intro == 1:
            all_sprites.draw(screen)
            horizontal_borders.draw(screen)
            vertical_borders.draw(screen)
            all_sprites.update()
        if to_menu == 1:
            menu.render(screen)
        if to_gameplay == 1:
            time += v / 60
            if clicked == 1:
                col_vo -= 1
                clicked = 0
                game.update()
            else:
                pygame.draw.circle(game.screen, game.color_ball, (game.coord_x, game.coord_y),
                                   game.radius_ball, game.width_ball)
            if col_vo == 0:
                game.end(time, rectangle_menu)
                to_gameplay = 0
                to_results = 1
        if to_results == 1:
            game.end(time, rectangle_menu)
            if end_click == 1:
                prev_rec = list(cur.execute("""SELECT * FROM records"""))
                for rec in prev_rec:
                    if rec[1] > time / default_col_vo or rec[1] == 0:
                        cur.execute("""UPDATE records
                                       SET (time, targets_per_second) = (?, ?)
                                       WHERE id = ?""",
                                    (round(time, 3), round(time / default_col_vo, 3), rec[2]))
                        con.commit()
                        break
                begin = 0
                to_menu = 1
                to_settings = 0
                to_records = 0
                to_intro = 0
                to_gameplay = 0
                to_results = 0
                clicked = 0
                end_click = 0
                col_vo = default_col_vo
                time = 0
                to_exit = 0
        if to_records == 1:
            records.render(screen)
        if to_settings == 1:
            f = pygame.font.Font(None, 40)
            button_text = f.render('go to menu', True, 'white')
            targets = f.render('targets', True, 'white')
            size = f.render('size', True, 'white')
            ful = f.render('fullness of ball', True, 'white')
            ball_color = f.render('ball color', True, 'white')
            screen_color = f.render('screen color', True, 'white')
            screen.blit(targets, (230, 40))
            screen.blit(size, (230, 120))
            screen.blit(ful, (230, 200))
            screen.blit(ball_color, (230, 280))
            screen.blit(screen_color, (230, 360))
            screen.blit(button_text, (100, 700))
            pygame.draw.rect(screen, 'white', (100, 690, 150, 50), 1)
            settings.authors()
            settings.warning()
            screen.fill(default_color_screen, (width / 20, height / 20, width / 10, height / 20))
            settings.draw(col_vo_balls, height / 20)
            settings.draw(radius, height / 20 * 3)
            settings.draw(fullness_ball, height / 20 * 5)
            settings.draw(color_ball, height / 20 * 7)
            settings.draw(color_screen, height / 20 * 9)
            screen.fill(default_color_screen, (width / 2, 0, width / 2, height / 2))
            settings.circle(radius, color_ball, fullness_ball)
        if to_exit == 1:
            exit_menu.click_exit()
        if f == 1:
            exit_menu.authors()
            seconds = (pygame.time.get_ticks() - start) / 1000
            if seconds > 17:
                running = False
        pygame.display.flip()
        clock.tick(FPS)
