import generate_grid
import draw_grid
# import solve


def main():
    grid = [[0 for _ in range(9)] for _ in range(9)]

    grid = generate_grid.generate(grid)
    draw_grid.draw(grid)


if __name__ == "__main__":
    main()
