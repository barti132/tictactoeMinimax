# sprawdzenie remisu
def is_tie(board_game):
    for row in board_game:
        for i in row:
            if i == 0:
                return False
    return True


# sprawdzenie warunków zwycięstwa
def check_winner(board_game):
    # wiersze i kolumny
    y_pos = 0
    for x in board_game:
        # dla X
        if sum(x) == 3 or (board_game[0][y_pos] + board_game[1][y_pos]
                           + board_game[2][y_pos] == 3):
            return 1
        # dla O
        if sum(x) == -3 or (board_game[0][y_pos] + board_game[1][y_pos]
                            + board_game[2][y_pos] == -3):
            return -1
        y_pos += 1

    # przekątne
    # dla X
    if board_game[0][0] + board_game[1][1] + board_game[2][2] == 3 or \
            board_game[2][0] + board_game[1][1] + board_game[0][2] == 3:
        return 1

    # dla O
    if board_game[0][0] + board_game[1][1] + board_game[2][2] == -3 or \
            board_game[2][0] + board_game[1][1] + board_game[0][2] == -3:
        return -1

    return 0