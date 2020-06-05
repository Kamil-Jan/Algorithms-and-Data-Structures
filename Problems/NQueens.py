def is_safe(board, row, col):
    n = len(board)
    for i in range(n):
        # check column
        if board[i][col] == "Q":
            return False
        # check diagonals
        for j in range(n):
            if i + j == row + col or i - j == row - col:
                if board[i][j] == "Q":
                    return False
    return True

def find_solutions(board, row, queen_left, solution_count=0):
    if row == len(board):
        yield board
    else:
        n = len(board)
        for i in range(n):
            if is_safe(board, row, i):
                board[row][i] = "Q"
                yield from find_solutions(board, row + 1, queen_left - 1)
                board[row][i] = "."

if __name__ == "__main__":
    N = 8
    b = [["." for _ in range(N)] for _ in range(N)]
    start = time.time()
    for row in next(find_solutions(b, 0, len(b))):
        print(*row)

