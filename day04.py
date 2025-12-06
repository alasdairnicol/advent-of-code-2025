#!/usr/bin/env python


def num_neighbours(point: tuple[int, int], grid: set[tuple[int, int]]) -> int:
    x, y = point
    deltas = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]
    return len([1 for dx, dy in deltas if (x + dx, y + dy) in grid])


def update_grid(grid: set[tuple[int, int]]) -> tuple[set[tuple[int, int]], int]:
    new_grid = {p for p in grid if num_neighbours(p, grid) >= 4}
    removed = len(grid) - len(new_grid)
    return new_grid, removed


def do_part_1(grid: set[tuple[int, int]]) -> int:
    _, removed = update_grid(grid)
    return removed


def do_part_2(grid: set[tuple[int, int]]) -> int:
    original_count = len(grid)

    while True:
        grid, removed = update_grid(grid)
        if removed == 0:
            break

    final_count = len(grid)

    return original_count - final_count


def main() -> None:
    lines = read_input()
    grid = {
        (i, j) for j, line in enumerate(lines) for i, x in enumerate(line) if x == "@"
    }

    part_1 = do_part_1(grid)
    print(f"{part_1=}")

    part_2 = do_part_2(grid)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day04.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
