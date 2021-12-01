import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic tac toe game')

line_width = 8
markers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def draw_grid():
    bg_color = (255, 255, 200)
    grid_color = (50, 50, 50)
    screen.fill(bg_color)
    for x in range(1, 3):
        pygame.draw.line(screen, grid_color, (0, x * 200), (screen_width, x * 200), line_width)
        pygame.draw.line(screen, grid_color, (x * 200, 0), (x * 200, screen_height), line_width)


run = True
while run:

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
