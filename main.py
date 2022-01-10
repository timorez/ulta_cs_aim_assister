import pygame
import math
import random


pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
pygame.display.set_caption('ultra_cs_aim_assister')
running = True

sprite = pygame.sprite.Sprite()
all_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()
FPS = 120

zapusk = None
pygame.draw.circle(screen, 'white', (width / 2, height / 2), height / 10, 1)
text = 'Start'
f = pygame.font.Font(None, 40)
text = f.render(text, True, 'white')
pos = text.get_rect(center=(width / 2, height / 2))
screen.blit(text, pos)


# menu ot timoshi
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
        print(self.board)

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        texts = ['start', 'settings', 'records', 'exit']
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
        if 200 <= mouse_pos[0] <= 350:
            if 100 < mouse_pos[1] < 250:
                pass
            elif 250 < mouse_pos[1] < 400:
                pass
            elif 400 < mouse_pos[1] < 550:
                pass
            elif 550 < mouse_pos[1] < 700:
                return 0


class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, x, y , colvo_stolknoveniy):
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



horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


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


Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
for i in range(20):
    Ball(20, width / 2, height / 2, 0)
menu = Menu(1, 4)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_coord = pygame.mouse.get_pos()[0]
            y_coord = pygame.mouse.get_pos()[1]
            sqx = (x_coord - (width / 2)) ** 2
            sqy = (y_coord - (height / 2)) ** 2
            if math.sqrt(sqx + sqy) < height / 10:
                zapusk = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu.click(pygame.mouse.get_pos()) == 0:
                running = False

    if zapusk == 1:
        screen.fill('black')
        all_sprites.draw(screen)
        horizontal_borders.draw(screen)
        vertical_borders.draw(screen)
        all_sprites.update()
        menu.render(screen)
    pygame.display.flip()
    clock.tick(FPS)
