#!/usr/bin/env python
def do_part_1(positions: list[int]) -> int:
    zeroes = [p for p in positions if p % 100 == 0]

    return len(zeroes)


def do_part_2(rotations: list[int], starting_postion) -> int:
    """
    Initial attempt to calculate number of zeroes for each rotation failed,
    so for now I'm stepping thought every click individually :(
    """
    total_clicks = 0
    position = starting_postion

    for rotation in rotations:
        for x in range(abs(rotation)):
            position += -1 if rotation < 0 else 1
            position %= 100
            if position == 0:
                total_clicks += 1

    return total_clicks


def parse_rotation(line: str) -> int:
    multiplier = -1 if line[0] == "L" else 1
    return multiplier * int(line[1:])


def parse_rotations(lines: list[str]) -> list[int]:
    return [parse_rotation(line) for line in lines]


def calc_positions(rotations: list[int], starting_position) -> list[int]:
    positions = [starting_position]
    for rotation in rotations:
        positions.append(positions[-1] + rotation)
    return positions


def main() -> None:
    starting_position = 50
    lines = read_input()
    rotations = parse_rotations(lines)
    positions = calc_positions(rotations, starting_position=starting_position)

    part_1 = do_part_1(positions)
    print(f"{part_1=}")

    part_2 = do_part_2(rotations, starting_postion=starting_position)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day01.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
