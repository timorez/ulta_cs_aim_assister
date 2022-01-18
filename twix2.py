import pygame


# создание окна для работы
pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)
default_color_screen = 'black'

# класс выхода из игры
class Exit:
    def __init__(self, width, height):
        self.width = width
        self.height = height

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


exit = Exit(width, height)
exit.click_exit()
running = True
# основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if exit.rect_dont_exit.collidepoint(pygame.mouse.get_pos()):
                pass
                #обратно в главное меню
            if exit.rect_exit.collidepoint(pygame.mouse.get_pos()):
                screen.fill(default_color_screen)
                f = 1
                exit.authors()
                # можно здесь таймерочек сделать
                running = False
    pygame.display.flip()
