grid = [
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


def is_legal(grid, row, column, num):
    for col in range(9):
        if grid[row][col] == num:
            return False

    for _row in range(9):
        if grid[_row][column] == num:
            return False

    startRow = row - row % 3
    startCol = column - column % 3

    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True


def solve_grid(grid, row, column, count):
    if row == 8 and column == 9:
        return 1 + count

    if column == 9:
        row += 1
        column = 0

    if grid[row][column] > 0:
        return solve_grid(grid, row, column + 1, count)

    for num in range(1, 10):
        if count >= 2:
            return count

        if is_legal(grid, row, column, num):
            grid[row][column] = num
            count = solve_grid(grid, row, column + 1, count)

            if solve_grid(grid, row, column + 1, count):
                return True

        grid[row][column] = 0

    return count
