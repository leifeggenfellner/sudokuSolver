from random import randint, shuffle
import solve

number_list = [i for i in range(1, 10)]

def fill_grid(grid):

    for i in range(81):
        row = i // 9
        col = i % 9

        if grid[row][col]==0:
            shuffle(number_list)      
            for value in number_list:
                if not(value in grid[row]):
                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                        square=[]
                        if row < 3:
                            if col < 3:
                                square=[grid[i][0:3] for i in range(0,3)]
                            elif col < 6:
                                square=[grid[i][3:6] for i in range(0,3)]
                            else:  
                                square=[grid[i][6:9] for i in range(0,3)]
                        elif row<6:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3,6)]
                            else:  
                                square=[grid[i][6:9] for i in range(3,6)]
                        else:
                            if col<3:
                                square=[grid[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(6,9)]
                            else:  
                                square=[grid[i][6:9] for i in range(6,9)]
                        if not value in (square[0] + square[1] + square[2]):
                            grid[row][col]=value
                            if solve.check_grid(grid):
                                return True
                            else:
                                if fill_grid(grid):
                                    return True
            break
    grid[row][col]=0

def generate(grid):
    fill_grid(grid)

    attempts = 5

    while attempts > 0:
        row = randint(0, 8)
        col = randint(0, 8)

        while grid[row][col] == 0:
            row = randint(0, 8)
            col = randint(0, 8)

        backup = grid[row][col]
        grid[row][col] = 0

        copy_grid = [row[:] for row in grid]

        solve.counter = 0
        solve.solve_grid_generate(copy_grid)

        if solve.counter != 1:
            grid[row][col] = backup
            attempts -= 1
    
    return grid
    
