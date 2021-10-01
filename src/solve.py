counter = 0

def check_grid(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False
    return True

def solve_grid(grid):  
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
                                if solve_grid(grid):
                                    return True
            break
    grid[row][col]=0  