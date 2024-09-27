# Импортируем необходимые библиотеки
import pygame
import time
import random

# Инициализация всех модулей Pygame
pygame.init()

# Определяем цвета в формате RGB
WHITE = (255, 255, 255)  # Белый цвет
RED = (255, 0, 0)        # Красный цвет
BLACK = (0, 0, 0)        # Черный цвет
GREEN = (0, 255, 0)      # Зеленый цвет

# Размеры окна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Размер блока змейки
SNAKE_BLOCK_SIZE = 10

# Устанавливаем скорость змейки (количество кадров в секунду)
SNAKE_SPEED = 15

# Создаем окно игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка на Pygame")

# Настройка шрифтов для отображения текста
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Часы для контроля скорости обновления экрана
clock = pygame.time.Clock()

# Функция для отображения текущего счёта
def display_score(score):
    value = score_font.render(f"Ваш счёт: {score}", True, GREEN)
    screen.blit(value, [0, 0])

# Функция для отображения сообщений (например, проигрыш)
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])


