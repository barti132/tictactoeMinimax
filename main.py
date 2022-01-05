import pygame
from pygame.locals import *

# ustawienie zmiennych gry
pygame.init()

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

player = 1
winner = 0
clicked = False
game_over = False

run = True

screen_width = 600
screen_height = 600

line_width = 8

again_rect = Rect(screen_width // 2 - 160, screen_height // 2 + 35, 350, 50)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic tac toe game')


def is_tie(board_game):
    for row in board_game:
        for i in row:
            if i == 0:
                return False
    return True


def check_winner(board_game):
    # wiersze i kolumny
    y_pos = 0
    for x in board_game:
        if sum(x) == 3 or (board_game[0][y_pos] + board_game[1][y_pos] + board_game[2][y_pos] == 3):
            return 1
        if sum(x) == -3 or (board_game[0][y_pos] + board_game[1][y_pos] + board_game[2][y_pos] == -3):
            return -1
        y_pos += 1

    # przekątne
    if board_game[0][0] + board_game[1][1] + board_game[2][2] == 3 or\
            board_game[2][0] + board_game[1][1] + board_game[0][2] == 3:
        return 1

    if board_game[0][0] + board_game[1][1] + board_game[2][2] == -3 or\
            board_game[0][0] + board_game[1][1] + board_game[2][2] == -3:
        return -1

    return 0


def minimax(depth, is_max):
    global board
    win = check_winner(board)

    if win == 1:
        return -10

    if win == -1:
        return 10

    if is_tie(board):
        return 0

    if is_max:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = max(best, minimax(depth + 1, not is_max))
                    board[i][j] = 0
        return best - depth

    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    best = min(best, minimax(depth + 1, not is_max))
                    board[i][j] = 0
        return best + depth


def ai_move():
    global player
    global board

    best_val = -1000
    best_pos = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = -1
                move_val = minimax(0, True)

                board[i][j] = 0
                if move_val > best_val:
                    best_pos = (i, j)
                    best_val = move_val

    print(best_val)
    board[best_pos[0]][best_pos[1]] = player
    player *= -1


def player_events(e):
    global run
    global clicked
    global player
    global winner
    global game_over
    global board

    if e.type == pygame.QUIT:
        run = False
    if game_over == 0:
        if e.type == pygame.MOUSEBUTTONDOWN and not clicked:
            clicked = True

        if e.type == pygame.MOUSEBUTTONUP and clicked:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            if board[cell_x // 200][cell_y // 200] == 0:
                board[cell_x // 200][cell_y // 200] = player
                player *= -1

                winner = check_winner(board)
                if winner != 0:
                    game_over = True
                    player = 1

                if not game_over and is_tie(board):
                    game_over = True
                    winner = 0
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
    for x in board:
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


def draw_winner():
    if winner != 0:
        end_text = "Gracz " + str(winner) + " wygrał!"
    else:
        end_text = "        Remis"

    end_img = pygame.font.SysFont(pygame.font.get_default_font(), 60).render(end_text, True, (0, 0, 255))
    pygame.draw.rect(screen, (0, 255, 0), (screen_width // 2 - 145, screen_height // 2 - 30, 320, 60))
    screen.blit(end_img, (screen_width // 2 - 140, screen_height // 2 - 20))

    again_text = 'Zagraj ponownie'
    again_img = pygame.font.SysFont(pygame.font.get_default_font(), 60).render(again_text, True, (0, 0, 255))
    pygame.draw.rect(screen, (0, 255, 0), again_rect)
    screen.blit(again_img, (screen_width // 2 - 150, screen_height // 2 + 40))


def show_game_over_screen():
    global clicked
    global board
    global winner
    global player
    global game_over

    draw_winner()
    if event.type == pygame.MOUSEBUTTONDOWN and not clicked:
        clicked = True
    if event.type == pygame.MOUSEBUTTONUP and clicked:
        clicked = False
        pos = pygame.mouse.get_pos()
        if again_rect.collidepoint(pos):
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            winner = 0
            player = 1
            game_over = False


# główna pętla gry
while run:
    draw_grid()
    draw_markers()

    if player == 1:
        for event in pygame.event.get():
            player_events(event)
    else:
        ai_move()
        winner = check_winner(board)
        if winner != 0:
            game_over = True
            player = 1

        if not game_over and is_tie(board):
            game_over = True
            winner = 0

    if game_over:
        show_game_over_screen()
    pygame.display.update()

pygame.quit()
