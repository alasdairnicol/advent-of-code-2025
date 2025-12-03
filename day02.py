#!/usr/bin/env python
import math


def has_single_repeat(x):
    s = str(x)
    half = s[: len(s) // 2]
    return s == half + half


def calc_repeats(ranges: list[tuple[int, int]]) -> set[int]:
    max_value = int(max(max(x) for x in ranges))
    max_length = math.ceil(math.log(max_value, 10))
    repeats = set()
    for i in range(
        10 ** (max_length // 2)
    ):  # if max value is abcdef, then longest repeat will be abc
        for n in range(2, max_length):
            x = int(str(i) * n)
            if x > max_value:
                break
            repeats.add(x)
    return repeats


def do_part_1(ranges: list[tuple[int, int]]) -> int:
    return sum([n for x, y in ranges for n in range(x, y + 1) if has_single_repeat(n)])


def do_part_2(ranges: list[tuple[int, int]]) -> int:
    repeats = calc_repeats(ranges)
    return sum([n for x, y in ranges for n in range(x, y + 1) if n in repeats])


def parse_ranges(input_string: str) -> list[tuple[int, int]]:
    ranges = [
        (int(x), int(y))
        for x, y in (range.split("-") for range in input_string.split(","))
    ]
    return sorted(ranges)


def main() -> None:
    input_string = read_input()
    ranges = parse_ranges(input_string)

    part_1 = do_part_1(ranges)
    print(f"{part_1=}")

    part_2 = do_part_2(ranges)
    print(f"{part_2=}")


def read_input() -> str:
    with open("day02.txt") as f:
        return f.read()


if __name__ == "__main__":
    main()
