"""
Tytuł: Kółko i krzyżyk (Tic tac toe)
Autor: Bartosz Średziński
Opis: Gra kółko i krzyżyk, napisana z biblioteką pygame. Umożliwia
granie w grę przeciwko komputerowi. Przeciwnik komputerowy używa algorytmu min max.
"""

import pygame
from pygame.locals import *

import game_rules
import minimax

# ustawienie zmiennych gry
pygame.init()

board_tictactoe = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

player_current = 1
winner = 0
clicked = False
clicked_new_game = 0
game_over = False

run = True

screen_width = 600
screen_height = 600

line_width = 8

again_rect = Rect(screen_width // 2 - 160, screen_height // 2 + 35, 350, 50)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic tac toe game')


def make_best_move_enemy(player, board):
    """
    OPIS:
        Funkcja wykonuje ruch gracza komputerowego. Wykonuje wszystkie możliwe ruchy i oblicza dla nich wartości poprzez
        algorytm minmax. Na koniec wybiera najlepszy ruch i go wykonuje.

    PARAMETRY:
        board - plansza gry
        player - zmienna odpowiedzialna za kolejność graczy

    ZWRACA:
        player - aktualny stan
        board - stan po ruchu komputera
    """

    best_val = -1000
    best_pos = (-1, -1)

    # Wykonanie wszystkich ruchów, a następnie wybranie najlepszego
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:

                board[i][j] = -1
                move_val = minimax.minimax(5, True, board)
                board[i][j] = 0

                if move_val > best_val:
                    best_pos = (i, j)
                    best_val = move_val

    board[best_pos[0]][best_pos[1]] = player
    player *= -1
    return player, board


def draw_grid():
    """
    OPIS:
        Funkcja rysuje na ekranie plansze gry
    """
    bg_color = (255, 255, 200)
    grid_color = (50, 50, 50)
    screen.fill(bg_color)
    for x in range(1, 3):
        pygame.draw.line(screen, grid_color, (0, x * 200),
                         (screen_width, x * 200), line_width)
        pygame.draw.line(screen, grid_color, (x * 200, 0), (x * 200,
                                                            screen_height), line_width)


def draw_markers(board):
    """
    OPIS:
        Funkcja rysuje na ekranie X i O

    PARAMETRY:
        board - plansza gry
    """
    x_pos = 0
    for x in board:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, (0, 255, 0), (y_pos * 200 +
                                                       15, x_pos * 200 + 15),
                                 (y_pos * 200 + 185, x_pos * 200 +
                                  185), line_width)
                pygame.draw.line(screen, (0, 255, 0), (y_pos * 200 +
                                                       15, x_pos * 200 + 185),
                                 (y_pos * 200 + 185, x_pos * 200 + 15),
                                 line_width)
            if y == -1:
                pygame.draw.circle(screen, (255, 0, 0), (y_pos * 200 +
                                                         100, x_pos * 200 + 100), 80, line_width)
            y_pos += 1
        x_pos += 1


# Wyświetlenie komunikatu o wygranej
def draw_winner():
    """
    OPIS:
        Funkcja wyświetla komunikat o zakończeniu gry(wygrana, remis) oraz komunikat "zagraj ponownie".
    """
    if winner != 0:
        end_text = "Gracz " + str(winner) + " wygrał!"
    else:
        end_text = "        Remis"

    end_img = pygame.font.SysFont(pygame.font.get_default_font(),
                                  60).render(end_text, True, (0, 0, 255))
    pygame.draw.rect(screen, (0, 255, 0), (screen_width // 2 - 145,
                                           screen_height // 2 - 30, 320, 60))
    screen.blit(end_img, (screen_width // 2 - 140, screen_height // 2 - 20))

    again_text = 'Zagraj ponownie'
    again_img = pygame.font.SysFont(pygame.font.get_default_font(),
                                    60).render(again_text, True, (0, 0, 255))
    pygame.draw.rect(screen, (0, 255, 0), again_rect)
    screen.blit(again_img, (screen_width // 2 - 150, screen_height // 2 + 40))


def show_game_over_screen(clicked_new_game):
    """
    OPIS:
        Funkcja wyświetla komunikat o zakończeniu gry i umożliwia zagranie od nowa

    PARAMETRY:
        clicked_new_game - stan myszy

    ZWRACA:
        0 - przycisk nie wciśnięty
        1 - przycisk wciśnięty
        2 - klinięto w "zagraj ponownie"
    """

    draw_winner()
    if event.type == pygame.MOUSEBUTTONDOWN and not clicked_new_game:
        return 1
    if event.type == pygame.MOUSEBUTTONUP and clicked_new_game:
        if again_rect.collidepoint(pygame.mouse.get_pos()):
            return 2
        return 0


# główna pętla gry
while run:
    # rysowanie planszy
    draw_grid()
    draw_markers(board_tictactoe)

    # ruch gracza
    if player_current == 1:
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
                    if board_tictactoe[cell_y // 200][cell_x // 200] == 0:
                        board_tictactoe[cell_y // 200][cell_x // 200] = player_current
                        player_current *= -1

    # ruch przeciwnika
    else:
        player_current, board_tictactoe = make_best_move_enemy(player_current, board_tictactoe)

    # sprawdzenie warunków zwycięstwa
    winner = game_rules.check_winner(board_tictactoe)
    if winner != 0:
        game_over = True
        player_current = 1

    if not game_over and game_rules.is_tie(board_tictactoe):
        game_over = True
        winner = 0
        player_current = 1

    if game_over:
        clicked_new_game = show_game_over_screen(clicked_new_game)
        if clicked_new_game == 2:
            board_tictactoe = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            winner = 0
            player_current = 1
            game_over = False
            clicked_new_game = 0

    pygame.display.update()

pygame.quit()
