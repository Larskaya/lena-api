import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


"""

Спрайт — это элемент компьютерной графики, представляющий объект на экране, который может двигаться.
Для загрузки и отрисовки спрайтов в случай этой игры их нужно добавить в разделы “Обновление” и 
“Визуализация” игрового цикла(группировка спрайтов). В Pygame все спрайты выступают объектами.

"""

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


"""
Дальше необходимо определить rect(rectangle) спрайта. Прямоугольники повсеместно используются в Pygame
для отслеживания координат объектов. Команда get_rect() высчитывает прямоугольник, способный окружить его.

"""




# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("evolution")
clock = pygame.time.Clock()

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
        
    # Рендеринг
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()

