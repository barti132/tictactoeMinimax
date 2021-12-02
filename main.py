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
winner = 0
game_over = False
again_rect = Rect(screen_width // 2 - 160, screen_height // 2 + 35, 350, 50)


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


def check_winner():
    global winner
    global game_over

    y_pos = 0
    for x in markers:
        if sum(x) == 3 or (markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3):
            winner = 1
            game_over = True
        if sum(x) == -3 or (markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3):
            winner = 2
            game_over = True
        y_pos += 1

    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True

    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[0][0] + markers[1][1] + markers[2][2] == -3:
        winner = 2
        game_over = True

    if not game_over:
        tie = True
        for row in markers:
            for i in row:
                if i == 0:
                    tie = False
        if tie:
            game_over = True
            winner = 0


def draw_winner():
    if winner != 0:
        end_text = "Gracz " + str(winner) + " wygrał!"
    else:
        end_text = "        Remis"

    end_img = pygame.font.SysFont(None, 60).render(end_text, True, (0, 0, 255))
    pygame.draw.rect(screen, (0, 255, 0), (screen_width // 2 - 145, screen_height // 2 - 30, 320, 60))
    screen.blit(end_img, (screen_width // 2 - 140, screen_height // 2 - 20))

    again_text = 'Zagraj ponownie'
    again_img = pygame.font.SysFont(None, 60).render(again_text, True, (0, 0, 255))
    pygame.draw.rect(screen, (0, 255, 0), again_rect)
    screen.blit(again_img, (screen_width // 2 - 150, screen_height // 2 + 40))


run = True
while run:

    draw_grid()
    draw_markers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == 0:
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
                    check_winner()

    if game_over:
        draw_winner()
        if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
                winner = 0
                player = 1
                game_over = False

    pygame.display.update()

pygame.quit()
