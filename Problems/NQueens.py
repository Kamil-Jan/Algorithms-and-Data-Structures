def is_safe(board, row, col):
    n = len(board)
    for i in range(n):
        # check column
        if board[i][col] == 1:
            return False
        # check diagonals
        for j in range(n):
            if i + j == row + col or i - j == row - col:
                if board[i][j] == 1:
                    return False
    return True

def find_solution(board, row, queen_left):
    if queen_left == 0:
        return True
    n = len(board)
    for i in range(n):
        if is_safe(board, row, i):
            board[row][i] = 1
            if find_solution(board, row + 1, queen_left - 1):
                return True
            board[row][i] = "_"
    return False

if __name__ == "__main__":
    board = [["_" for _ in range(8)] for _ in range(8)]
    find_solution(board, 0, len(board))
    for row in board:
        print(*row)

