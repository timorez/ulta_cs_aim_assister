import pygame


pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
col_vo_balls = 30
radius = 35
default_color_screen = 'black'
color_screen = 'black'
fullness_ball = 0
color_ball = 'white'
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
        self.text_colors_sc = ['black', 'white', 'purple', 'grey', 'blue', 'red', 'yellow', 'green']
        self.text = 'screen color'
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 10 + self.width / 10 + self.width / 22 * 2,
                                           self.height / 20 * 9 + self.height / 40))
        screen.blit(self.t, self.pos)
        self.colors_sc_rgb = [(0, 0, 0), (255, 255, 255), (148, 0, 211), (190, 190, 190), (0, 121, 219),
                              (239, 48, 56), (253, 219, 109), (138, 255, 138)]


    def warning(self):
        self.text = "Warning! Don't use the same colors!"
        self.t = self.f.render(self.text, True, 'white')
        self.pos = self.t.get_rect(center=(self.width / 10 + self.width / 16 * 2, self.height / 1.5))
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




set = Settings(width, height, screen)
set.col_vo(col_vo_balls)
set.radius(radius)
set.color(color_ball)
set.color_sc(color_screen)
set.warning()
set.circle(radius, color_ball, fullness_ball)
running = True
set.fullness_ball(fullness_ball)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if set.rect_plus_col_vo.collidepoint(pygame.mouse.get_pos()):
                if col_vo_balls < 200:
                    col_vo_balls += 5
                    screen.fill(default_color_screen, (width / 20, height / 20, width / 10, height / 20))
                    set.draw(col_vo_balls, height / 20)
            if set.rect_minus_col_vo.collidepoint(pygame.mouse.get_pos()):
                if col_vo_balls > 5:
                    col_vo_balls -= 5
                    screen.fill(default_color_screen, (width / 20, height / 20, width / 10, height / 20))
                    set.draw(col_vo_balls, height / 20)
            if set.rect_plus_rad.collidepoint(pygame.mouse.get_pos()):
                if radius < 75:
                    radius += 5
                    screen.fill(default_color_screen, (width / 20, height / 20 * 3, width / 10, height / 20))
                    set.draw(radius, height / 20 * 3)
                    screen.fill(default_color_screen, (width / 2, 0, width / 2, height / 2))
                    set.circle(radius, color_ball, fullness_ball)
            if set.rect_minus_rad.collidepoint(pygame.mouse.get_pos()):
                if radius > 5:
                    radius -= 5
                    screen.fill(default_color_screen, (width / 20, height / 20 * 3, width / 10, height / 20))
                    set.draw(radius, height / 20 * 3)
                    screen.fill(default_color_screen, (width / 2, 0, width / 2, height / 2))
                    set.circle(radius, color_ball, fullness_ball)
            if set.rect_minus_f_b.collidepoint(pygame.mouse.get_pos()):
                if fullness_ball > 0:
                    fullness_ball -= 1
                    screen.fill(default_color_screen, (width / 20, height / 20 * 5, width / 10, height / 20))
                    set.draw(fullness_ball, height / 20 * 5)
                    screen.fill(default_color_screen, (width / 2, 0, width / 2, height / 2))
                    set.circle(radius, color_ball, fullness_ball)
            if set.rect_plus_f_b.collidepoint(pygame.mouse.get_pos()):
                if fullness_ball < 1:
                    fullness_ball += 1
                    screen.fill(default_color_screen, (width / 20, height / 20 * 5, width / 10, height / 20))
                    set.draw(fullness_ball, height / 20 * 5)
                    screen.fill(default_color_screen, (width / 2, 0, width / 2, height / 2))
                    set.circle(radius, color_ball, fullness_ball)
            if set.rect_minus_color.collidepoint(pygame.mouse.get_pos()):
                color_ball = set.text_colors[set.text_colors.index(color_ball) - 1]
                screen.fill(default_color_screen, (width / 20, height / 20 * 7, width / 10, height / 20))
                set.draw(color_ball, height / 20 * 7)
                screen.fill(default_color_screen, (width / 2, 0, width / 2, height / 2))
                set.circle(radius, color_ball, fullness_ball)
            if set.rect_plus_color.collidepoint(pygame.mouse.get_pos()):
                if set.text_colors.index(color_ball) < 9:
                    color_ball = set.text_colors[set.text_colors.index(color_ball) + 1]
                    screen.fill(default_color_screen, (width / 20, height / 20 * 7, width / 10, height / 20))
                    set.draw(color_ball, height / 20 * 7)
                    screen.fill(default_color_screen, (width / 2, 0, width / 2, height / 2))
                    set.circle(radius, color_ball, fullness_ball)
                else:
                    color_ball = 'white'
                    screen.fill(default_color_screen, (width / 20, height / 20 * 7, width / 10, height / 20))
                    set.draw(color_ball, height / 20 * 7)
                    screen.fill(default_color_screen, (width / 2, 0, width / 2, height / 2))
                    set.circle(radius, color_ball, fullness_ball)
            if set.rect_minus_color_sc.collidepoint(pygame.mouse.get_pos()):
                color_screen = set.text_colors_sc[set.text_colors_sc.index(color_screen) - 1]
                screen.fill(default_color_screen, (width / 20, height / 20 * 9, width / 10, height / 20))
                set.draw(color_screen, height / 20 * 9)
                color_screen_rgb = set.colors_sc_rgb[set.text_colors_sc.index(color_screen)]
                screen.fill(color_screen_rgb, (width / 2, height / 2, width / 2, height / 2))
            if set.rect_plus_color_sc.collidepoint(pygame.mouse.get_pos()):
                if set.text_colors_sc.index(color_screen) < 7:
                    color_screen = set.text_colors_sc[set.text_colors_sc.index(color_screen) + 1]
                    screen.fill(default_color_screen, (width / 20, height / 20 * 9, width / 10, height / 20))
                    set.draw(color_screen, height / 20 * 9)
                    color_screen_rgb = set.colors_sc_rgb[set.text_colors_sc.index(color_screen)]
                    screen.fill(color_screen_rgb, (width / 2, height / 2, width / 2, height / 2))
                else:
                    color_screen = 'black'
                    screen.fill(default_color_screen, (width / 20, height / 20 * 9, width / 10, height / 20))
                    set.draw(color_screen, height / 20 * 9)
                    color_screen_rgb = set.colors_sc_rgb[set.text_colors_sc.index(color_screen)]
                    screen.fill(color_screen_rgb, (width / 2, height / 2, width / 2, height / 2))
    pygame.display.flip()
