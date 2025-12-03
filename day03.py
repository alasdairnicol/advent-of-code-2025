#!/usr/bin/env python
import itertools


def do_part_1(lines: list[str]) -> int:
    return sum(
        max(int("".join(c)) for c in list(itertools.combinations(line.strip(), 2)))
        for line in lines
    )


def max_joltage(number: str, length: int):
    result = ""
    start = 0

    for end in range(len(number) - length, len(number)):
        # end is the final index that can be selected while
        # still leaving enough digits afterwards

        # find the index containing the max digit in s[start : end+1]
        best_idx = max(range(start, end + 1), key=lambda i: number[i])

        result += number[best_idx]
        start = best_idx + 1

    return int(result)


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
