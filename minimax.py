import game_rules


# algorytm minimax
def minimax(depth, is_max, board):
    """
    OPIS:
        Implementacja algorytmu min-max

    PARAMETRY:
        board - plansza gry
        is_max - maksymalizacja czy minimalizacja
        depth - głębokość drzewa

    ZWRACA:
        wartość gałęzi
    """
    win = game_rules.check_winner(board)

    if win == 1:
        return -10

    if win == -1:
        return 10

    if game_rules.is_tie(board) or depth == 0:
        return 0

    # maksymalizowanie wyniku
    if is_max:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 1
                    best = min(best, minimax(depth - 1, not is_max, board))
                    board[i][j] = 0
        return best - depth

    # minimalizowanie wyniku
    else:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -1
                    best = max(best, minimax(depth - 1, not is_max, board))
                    board[i][j] = 0
        return best + depth
