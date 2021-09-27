import generate_grid
import draw_grid
import solve


def main():
    grid = generate_grid.generate()
    grid_copy = [row[:] for row in grid]
    solve.solve_grid(grid, 0, 0, 0)

    draw_grid.draw(grid_copy)


if __name__ == "__main__":
    main()
