import pygame


pygame.init()
size = width, height = 1024, 768
screen = pygame.display.set_mode(size)


class Menu:
    def __init__(self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.rectangles = []

    def otrisovka(self):
        self.width_rect = self.width / 4
        self.height_rect = self.height / 10
        self.y_rect = self.height / 10
        self.x_rect = self.width / 2 - self.width / 8
        self.text_y = self.height / 10
        self.rectangles = []
        self.texts = ['play', 'settings', 'records', 'exit']
        for i in range(4):
            pygame.draw.rect(screen, 'white', (self.x_rect, self.y_rect, self.width_rect, self.height_rect), 1)
            self.rect = pygame.Rect(self.x_rect, self.y_rect, self.width_rect, self.height_rect)
            self.rectangles.append(self.rect)
            self.y_rect += self.width_rect / 2
            self.f = pygame.font.Font(None, 50)
            self.text = self.f.render(self.texts[i], True, 'white')
            self.pos = self.text.get_rect(center=(self.x_rect + self.width_rect / 2,
                                                  self.text_y + self.height_rect / 2))
            screen.blit(self.text, self.pos)
            self.text_y += self.width_rect / 2

    def click(self):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rectangles[0].collidepoint(pygame.mouse.get_pos()):
                print(1)
            if self.rectangles[1].collidepoint(pygame.mouse.get_pos()):
                print(2)
            if self.rectangles[2].collidepoint(pygame.mouse.get_pos()):
                print(3)
            if self.rectangles[3].collidepoint(pygame.mouse.get_pos()):
                print(0)

running = True
menu = Menu(width, height, screen)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    menu.otrisovka()
    menu.click()
    pygame.display.flip()

