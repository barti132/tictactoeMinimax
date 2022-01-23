def is_tie(board_game):
    """
    OPIS:
        Funkcja sprawdza warunki remisu dla gry kółko i krzyżyk

    PARAMETRY:
        board_game - plansza gry

    ZWRACA:
        True jeżeli jest remis,
        False jeżeli nie ma remisu
    """

    for row in board_game:
        for i in row:
            if i == 0:
                return False
    return True


def check_rows_cols(player, board):
    """
    OPIS:
        Funckja sprawdza zwycięstwa dla podanego gracza w wierszach i kolumnach

    PARAMETRY:
        player - dla jakiego gracza sprawdzamy warunki
        board - plansza gry

    ZWRACA:
        True jeżeli gracz wygrał
        False jeżeli warunek zwycięstwa nie jest spełniony
    """
    y = 0
    for x in board:
        if sum(x) == 3 * player or (board[0][y] + board[1][y] + board[2][y] == 3 * player):
            return True
        y += 1
    return False


def check_diagonal(player, board):
    """
    OPIS:
        Funckja sprawdza zwycięstwa dla podanego gracza w przekątnych

    PARAMETRY:
        player - dla jakiego gracza sprawdzamy warunki
        board - plansza gry

    ZWRACA:
        True jeżeli gracz wygrał
        False jeżeli warunek zwycięstwa nie jest spełniony
    """

    if board[0][0] + board[1][1] + board[2][2] == 3 * player or \
            board[2][0] + board[1][1] + board[0][2] == 3 * player:
        return True
    return False


def check_winner(board_game):
    """
    OPIS:
        Funkcja sprawdza warunki zwycięstwa dla gry kółko i krzyżyk

    PARAMETRY:
        board_game - plansza gry

    ZWRACA:
        1 jeżeli wygrał gracz X,
        -1 jeżeli wygral gracz O,
        0 jeżeli nie ma wygranej
    """

    if check_rows_cols(-1) or check_diagonal(-1):
        return -1

    if check_rows_cols(1) or check_diagonal(1):
        return 1

    return 0
