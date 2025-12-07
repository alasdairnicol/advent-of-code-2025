#!/usr/bin/env python

# Type aliases
Grid = dict[tuple[int, int], str | int]


def get_val(grid: Grid, i: int, j: int) -> str | int | None:
    current = grid.get((i, j))
    if current == "^":
        return current
    val: int = 0
    left = grid.get((i - 1, j))
    above_left = grid.get((i - 1, j - 1))
    above = grid.get((i, j - 1))
    right = grid.get((i + 1, j))
    above_right = grid.get((i + 1, j - 1))
    if above not in {"^", None}:
        val = above if above != "|" and isinstance(above, int) else 1
    if left == "^" and above_left and isinstance(above_left, int):
        val += above_left
    if right == "^" and above_right and isinstance(above_right, int):
        val += above_right

    return val


def do_part_1(grid: Grid, width: int, height: int) -> int:
    count = 0
    for j in range(1, height):
        for i in range(width):
            if (
                (grid.get((i, j - 1)) == "|" and grid.get((i, j)) != "^")
                or (grid.get((i - 1, j)) == "^" and grid.get((i - 1, j - 1)) == "|")
                or (grid.get((i + 1, j)) == "^" and grid.get((i + 1, j - 1)) == "|")
            ):
                grid[i, j] = "|"

            if grid.get((i, j - 1)) == "|" and grid.get((i, j)) == "^":
                count += 1
    return count


def do_part_2(grid: Grid, width: int, height: int) -> int:
    for j in range(1, height):
        for i in range(width):
            val = get_val(grid, i, j)
            if val is not None:
                grid[i, j] = val
    return sum(int(grid.get((i, height - 1), 0)) for i in range(width))


def main() -> None:
    lines = read_input()
    grid = parse_grid(lines)
    width = len(lines[0].strip())
    height = len(lines)

    part_1 = do_part_1(grid, width, height)
    print(f"{part_1=}")

    # grid has been modified by part 1 but it seems to work ok because
    # we'll overwrite the new "|"s on our second pass.
    part_2 = do_part_2(grid, width, height)
    print(f"{part_2=}")


def parse_grid(lines: list[str]) -> Grid:
    return {
        (i, j): "|" if val == "S" else val
        for j, line in enumerate(lines)
        for i, val in enumerate(line)
        if val not in {".", "\n"}
    }


def read_input() -> list[str]:
    with open("day07.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
