PLAYER_X = 1
PLAYER_O = -1
EMPTY = 0

def evaluate(board):
    lines = board + list(map(list, zip(*board)))
    lines += [
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    for line in lines:
        if line[0] == line[1] == line[2] != EMPTY:
            return line[0]
    return 0

def moves_left(board):
    return any(cell == EMPTY for row in board for cell in row)

def minimax(board, is_max):
    score = evaluate(board)
    if score != 0:
        return score
    if not moves_left(board):
        return 0

    if is_max:
        best = float("-inf")
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = PLAYER_X
                    best = max(best, minimax(board, False))
                    board[r][c] = EMPTY
        return best
    else:
        best = float("inf")
        for r in range(3):
            for c in range(3):
                if board[r][c] == EMPTY:
                    board[r][c] = PLAYER_O
                    best = min(best, minimax(board, True))
                    board[r][c] = EMPTY
        return best

def find_best_move(board):
    if evaluate(board) != 0 or not moves_left(board):
        return None
    best_value, best_move = float("-inf"), None
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                board[r][c] = PLAYER_X
                value = minimax(board, False)
                board[r][c] = EMPTY
                if value > best_value:
                    best_value, best_move = value, (r, c)
    return best_move

def print_board(board):
    symbols = {PLAYER_X: "X", PLAYER_O: "O", EMPTY: "."}
    for row in board:
        print(" ".join(symbols[x] for x in row))

if __name__ == "__main__":
    board = [
        [PLAYER_X, PLAYER_O, PLAYER_X],
        [PLAYER_O, PLAYER_X, EMPTY],
        [EMPTY, PLAYER_O, PLAYER_X]
    ]
    print("Current Board:")
    print_board(board)
    move = find_best_move(board)
    if move is None:
        print("The game is already over.")
    else:
        print("Best Move:", move)
        board[move[0]][move[1]] = PLAYER_X
        print("\nBoard after best move:")
        print_board(board)
