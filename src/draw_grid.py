import pygame

WIDTH = 550
HEIGHT = 600
background_color = (255, 255, 255)
original_grid_element_color = (0, 0, 0)
_buffer = 5


def insert(window, position, grid):
    myfont = pygame.font.SysFont("Comic Sans MS", 35)

    i, j = position[1] - 1, position[0] - 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if grid[i][j] != 0:
                    return
                if event.key == 48 or event.key == 8:
                    if event.key == 48:
                        grid[i][j] = event.key - 48
                    else:
                        grid[i][j] = event.key - 8
                    pygame.draw.rect(window, background_color,
                                     (position[0] * 50 + _buffer, position[1] * 50 + _buffer, 50 - 2 * _buffer, 50 - 2 * _buffer))
                    pygame.display.update()
                if 0 < event.key - 48 < 10:
                    pygame.draw.rect(window, background_color,
                                     (position[0] * 50 + _buffer, position[1] * 50 + _buffer, 50 - 2 * _buffer, 50 - 2 * _buffer))
                    value = myfont.render(
                        str(event.key - 48), True, original_grid_element_color)
                    window.blit(
                        value, (position[0] * 50 + 15, position[1] * 50))
                    grid[i][j]
                    pygame.display.update()
                return


def draw(grid):
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    window.fill(background_color)
    myfont = pygame.font.SysFont("Comic Sans MS", 35)

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(window, (0, 0, 0), (50 + 50 *
                             i, 50), (50 + 50 * i, 500), 3)
            pygame.draw.line(window, (0, 0, 0), (50, 50 +
                             50 * i), (500, 50 + 50 * i), 3)
        else:
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50),
                             (50 + 50*i, 500), 2)
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i),
                             (500, 50 + 50 * i), 2)

    for i in range(len(grid[0])):
        for j in range(len(grid[0])):
            if 0 < grid[i][j] < 10:
                value = myfont.render(
                    str(grid[i][j]), True, original_grid_element_color)
                window.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                position = pygame.mouse.get_pos()
                insert(window, (position[0] // 50, position[1] // 50), grid)

            if event.type == pygame.QUIT:
                return
