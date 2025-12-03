#!/usr/bin/env python
import itertools
from functools import cache


def do_part_1(lines: list[str]) -> int:
    return sum(
        max(int("".join(c)) for c in list(itertools.combinations(line.strip(), 2)))
        for line in lines
    )


@cache
def max_joltage(number, length):
    """
    Recursively find the max joltage
    """
    if length == 0:
        return ""
    if len(number) == length:
        return number

    n1 = number[0] + max_joltage(number[1:], length - 1)
    n2 = max_joltage(number[1:], length)
    return n1 if int(n1) > int(n2) else n2


def do_part_2(lines: list[str]) -> int:
    return sum(int(max_joltage(line, 12)) for line in lines)


def main() -> None:
    lines = read_input()
    lines = [line.strip() for line in lines]

    part_1 = do_part_1(lines)
    print(f"{part_1=}")

    part_2 = do_part_2(lines)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day03.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
