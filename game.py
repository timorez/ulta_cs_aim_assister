import pygame
import random
import math

pygame.init()
default_color_ball = pygame.color.Color('white')
default_radius_ball = 35
default_width_ball = 1
default_fulness_ball = 0
default_col_vo = 50
default_color_screen = pygame.color.Color('black')

size = width, height = 1000, 500
screen = pygame.display.set_mode(size)

class Game():

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

    # в разработке
    def update2(self, radius_ball2):
        self.hsv = self.color_ball.hsva
        self.radius_ball2 = radius_ball2
        if self.radius_ball <= self.radius_ball2 * 1.2:
            self.screen.fill('black')
            self.radius_ball += 1
            self.color_ball.hsva = (self.hsv[0], self.hsv[1], self.hsv[2] - 9, self.hsv[3])
            pygame.draw.circle(self.screen, self.color_ball, (self.coord_x, self.coord_y),
                               self.radius_ball, self.width_ball)
        else:
            self.radius_ball = self.radius_ball / 1.2
            self.color_ball.hsva = (self.hsv[0], self.hsv[1], 100, self.hsv[3])
            self.screen.fill('black')


    def return_pos(self):
        return self.coord_x, self.coord_y


    def end(self, time):
        self.time = str(round(time, 3))
        self.f = pygame.font.Font(None, 50)
        self.text = 'Time - '+ self.time + ' sec'
        self.text = self.f.render(self.text, True, 'Green')
        self.pos = self.text.get_rect(center=(width / 2, height / 2))
        screen.blit(self.text, self.pos)


color_ball = default_color_ball
radius_ball = default_radius_ball
width_ball = default_width_ball
fulness_ball = default_fulness_ball
col_vo = default_col_vo
game = Game(color_ball, radius_ball, width_ball, fulness_ball, width, height, screen)
color_screen = default_color_screen

running = True
zapusk = None
click = 0
nachalo = None
FPS = 60
v = 1
time = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = game.return_pos()
            x_coord = pos[0]
            y_coord = pos[1]
            x_coord_mouse = pygame.mouse.get_pos()[0]
            y_coord_mouse = pygame.mouse.get_pos()[1]
            sqx = (x_coord_mouse - (x_coord)) ** 2
            sqy = (y_coord_mouse - (y_coord)) ** 2
            if math.sqrt(sqx + sqy) < radius_ball:
                zapusk = 1
                nachalo = 1
    if col_vo > 0:
        if nachalo == 1:
            time += v / 60
        if zapusk == 1:
            screen.fill(color_screen)
            game.update()
            pygame.display.flip()
            col_vo -= 1
            zapusk = 0
    if col_vo <= 0:
        screen.fill(color_screen)
        game.end(time)
    clock.tick(FPS)
    pygame.display.flip()
