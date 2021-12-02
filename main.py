import pygame
from pygame.locals import *

pygame.init()

screen_width = 600
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic tac toe game')

line_width = 8
markers = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
clicked = False
pos = []
player = 1


def draw_grid():
    bg_color = (255, 255, 200)
    grid_color = (50, 50, 50)
    screen.fill(bg_color)
    for x in range(1, 3):
        pygame.draw.line(screen, grid_color, (0, x * 200), (screen_width, x * 200), line_width)
        pygame.draw.line(screen, grid_color, (x * 200, 0), (x * 200, screen_height), line_width)


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, (0, 255, 0), (x_pos * 200 + 15, y_pos * 200 + 15),
                                 (x_pos * 200 + 185, y_pos * 200 + 185), line_width)
                pygame.draw.line(screen, (0, 255, 0), (x_pos * 200 + 15, y_pos * 200 + 185),
                                 (x_pos * 200 + 185, y_pos * 200 + 15), line_width)
            if y == -1:
                pygame.draw.circle(screen, (255, 0, 0), (x_pos * 200 + 100, y_pos * 200 + 100), 80, line_width)
            y_pos += 1
        x_pos += 1


run = True
while run:

    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if markers[cell_x // 200][cell_y // 200] == 0:
                markers[cell_x // 200][cell_y // 200] = player
                player *= -1

    pygame.display.update()

pygame.quit()
