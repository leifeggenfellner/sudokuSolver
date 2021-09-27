board = [
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0]
]


def isLegal(board, row, col, num):
    for _col in range(9):
        if board[row][_col] == num:
            return False

    for _row in range(9):
        if board[_row][col] == num:
            return False

    startRow = row - row % 3
    startCol = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startCol] == num:
                return False
    return True


def solveBoard(board, row, col):
    if row == 8 and col == 9:
        return True

    if col == 9:
        row += 1
        col = 0

    if board[row][col] > 0:
        return solveBoard(board, row, col + 1)

    for num in range(1, 10):
        if isLegal(board, row, col, num):
            board[row][col] = num

            if solveBoard(board, row, col + 1):
                return True

        board[row][col] = 0

    return False


if __name__ == "__main__":
    if solveBoard(board, 0, 0):
        for i in range(9):
            for j in range(9):
                print(board[i][j], end=" ")
            print()
    else:
        print("No solution.")
