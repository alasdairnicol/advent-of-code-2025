#!/usr/bin/env python


def in_range(ranges, ingredient):
    for lower, upper in ranges:
        if lower > ingredient:
            return False

        if upper < ingredient:
            continue

        return True

    return False


def merge_ranges(ranges):
    if not ranges:
        return []

    out = [ranges[0]]
    for r in ranges[1:]:
        current = out[-1]
        if current[1] + 1 >= r[0]:
            # Merge overlapping or adjacent ranges (e.g. (2,4), (5,6))
            out[-1] = (current[0], max(current[1], r[1]))
        else:
            # Add distinct range to end of output
            out.append(r)

    return out


def do_part_1(ranges: list[tuple[int, int]], ingredients: list[int]) -> int:
    return len([i for i in ingredients if in_range(ranges, i)])


def do_part_2(ranges: list[tuple[int, int]]) -> int:
    collapsed_ranges = merge_ranges(ranges)
    return sum(b - a + 1 for a, b in collapsed_ranges)


def main() -> None:
    input_str = read_input()
    ranges, ingredients = parse_input(input_str)

    part_1 = do_part_1(ranges, ingredients)
    print(f"{part_1=}")

    part_2 = do_part_2(ranges)
    print(f"{part_2=}")


def read_input() -> str:
    with open("day05.txt") as f:
        return f.read()


def parse_input(input_str: str) -> tuple[list[tuple[int, int]], list[int]]:
    ranges_str, ingredients_str = input_str.split("\n\n")
    ranges = sorted(
        (int(x), int(y))
        for x, y in [r.split("-") for r in ranges_str.strip().split("\n")]
    )
    ingredients = [int(i) for i in ingredients_str.strip().split("\n")]
    return ranges, ingredients


if __name__ == "__main__":
    main()
