counter = 0

def check_grid(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False
    return True

def solve_grid_generate(grid):  
    global counter
    
    for i in range(81):
        row = i // 9
        col = i % 9

        if grid[row][col] == 0:
            for value in range(1, 10):
                if not(value in grid[row]):
                    if not value in (grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]):
                        square = []
                        if row<3:
                            if col<3:
                                square=[grid[i][0:3] for i in range(0,3)]
                            elif col<6:
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
                            if check_grid(grid):
                                counter += 1
                                break
                            else:
                                if solve_grid_generate(grid):
                                    return True
            break
    grid[row][col]=0  

def find_next_cell_to_fill(grid, row, column):
    for _row in range(row, 9):
        for _column in range(column, 9):
            if grid[_row][_column] == 0:
                return _row, _column
    
    for _row in range(9):
        for _column in range(9):
            if grid[_row][_column] == 0:
                return _row, _column
    
    return -1, -1


def is_valid(grid, row, column, number):
    row_valid = all([number != grid[row][_column] for _column in range(9)])
    
    if row_valid:
        column_valid = all([number != grid[_row][column] for _row in range(9)])

        if column_valid:
            secTopRow, secTopColumn = 3 * (row // 3), 3 * (column // 3)
            for _row in range(secTopRow, secTopRow + 3):
                for _column in range(secTopColumn, secTopColumn + 3):
                    if grid[_row][_column] == number:
                        return False
            return True
    return False


def solve_grid(grid, row=0, column=0):    
    row, column = find_next_cell_to_fill(grid, row, column)

    if row == -1:
        return True
    for number in range(1, 10):
        if is_valid(grid, row, column, number):
            grid[row][column] = number
            if solve_grid(grid, row, column):
                return True
            grid[row][column] = 0
    return False