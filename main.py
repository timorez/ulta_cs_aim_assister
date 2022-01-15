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

default_color_ball = pygame.color.Color('white')
default_radius_ball = 35
default_width_ball = 1
default_fulness_ball = 0
default_col_vo = 4
default_color_screen = pygame.color.Color('black')
color_screen = default_color_screen

color_ball = default_color_ball
radius_ball = default_radius_ball
width_ball = default_width_ball
fulness_ball = default_fulness_ball

click = 0
start_timer = None
rectangle_menu = pygame.Rect(width - width / 5, height - height / 10,
                             width / 5, height / 10)
v = 1
time = 0

zapusk = None
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
                        y_coord - game.coord_y) ** 2 < default_radius_ball ** 2:
                    clicked = 1
                if width - width / 5 <= x_coord <= (width - width / 5) + (width / 5)\
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
                    elif menu.click([x_coord, y_coord]) == 2:
                        to_menu = 0
                        to_settings = 1
                        to_intro = 0
                    elif menu.click([x_coord, y_coord]) == 3:
                        to_menu = 0
                        to_records = 1
                        to_intro = 0
                    elif menu.click([x_coord, y_coord]) == 4:
                        running = False
                        break
                if to_records == 1:
                    if 800 < x_coord < 950 and 690 < y_coord < 740:
                        to_records = 0
                        to_menu = 1
        screen.fill((0, 0, 0))
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
                    if rec[1] < time / default_col_vo:
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
        if to_records == 1:
            records.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
