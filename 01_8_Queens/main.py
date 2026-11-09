N = 8
PRINT_ALL_SOLUTIONS = False

def is_safe(board, row, col):
    for r in range(row):
        if board[r] == col:
            return False
        if abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(board, row, solutions):
    if row == N:
        solutions.append(board[:])
        if PRINT_ALL_SOLUTIONS or len(solutions) == 1:
            for r in range(N):
                print(" ".join("Q" if board[r] == c else "." for c in range(N)))
            print()
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1, solutions)
            board[row] = -1

def main():
    solutions = []
    solve([-1] * N, 0, solutions)
    print("Total solutions found:", len(solutions))

if __name__ == "__main__":
    main()
