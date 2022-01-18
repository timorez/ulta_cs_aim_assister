import pygame
import math
import random

# создаем окно для работы
pygame.init()
size = width, height = 1000, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('zastavka')
running = True

#создаем спрайты
sprite = pygame.sprite.Sprite()
all_sprites = pygame.sprite.Group()

clock = pygame.time.Clock()
FPS = 120

# отрисока начального руга
zapusk = None
pygame.draw.circle(screen, 'white', (width / 2, height / 2), height / 10, 1)
text = 'Start'
f = pygame.font.Font(None, 40)
text = f.render(text, True, 'white')
pos = text.get_rect(center=(width / 2, height / 2))
screen.blit(text, pos)


# класс шариков заставки
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


# класс стенок для взаимодействия с шариками
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


# настройки стенок и шариков
Border(5, 5, width - 5, 5)
Border(5, height - 5, width - 5, height - 5)
Border(5, 5, 5, height - 5)
Border(width - 5, 5, width - 5, height - 5)
for i in range(20):
    Ball(20, width / 2, height / 2, 0)


# основной игровой цикл
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
                # начало заставки
        if event.type == pygame.WINDOWMAXIMIZED:
            size = pygame.display.get_desktop_sizes()
            screen = pygame.display.set_mode(size[0])
    if zapusk == 1:
        # анимация заставки
        screen.fill('black')
        all_sprites.draw(screen)
        horizontal_borders.draw(screen)
        vertical_borders.draw(screen)
        all_sprites.update()
    pygame.display.flip()
    clock.tick(FPS)
