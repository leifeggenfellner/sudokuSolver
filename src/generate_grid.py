from solve import solve_grid
import random


def get_filled_squares(grid):
    filled = []

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                filled.append([i, j])

    return filled


def remove_numbers(grid):
    count = solve_grid(grid, 0, 0, 0)

    filled_squares = get_filled_squares(grid)
    filled_squares_count = len(get_filled_squares(grid))

    rounds = 3

    while rounds > 0 and filled_squares_count >= 17:
        row, column = filled_squares.pop(
            random.randint(0, len(filled_squares) - 1))
        filled_squares_count -= 1

        removed_square = grid[row][column]
        grid[row][column] = 0

        grid_copy = [i[:] for i in grid]

        if solve_grid(grid_copy, 0, 0, count) != 1:
            grid[row][column] = removed_square
            filled_squares_count += 1
            rounds -= 1
    return


def generate():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    remove_numbers(grid)
    return grid
