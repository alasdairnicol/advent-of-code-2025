#!/usr/bin/env python
import functools
import itertools
import operator
from typing import Any, Callable, Iterable

operators = {
    "+": operator.add,
    "*": operator.mul,
}


def digits_to_num(digits: list[int]) -> int:
    return functools.reduce(lambda x, y: 10 * x + y, digits, 0)


def calc_column(op: Callable[[Any, Any], Any], column: Iterable[int]):
    return functools.reduce(op, column)


def calc_columns(
    ops: list[Callable[[Any, Any], Any]], columns: Iterable[Iterable[int]]
):
    return sum(calc_column(op, column) for op, column in zip(ops, columns))


def extract_columns_part_1(row_strings: list[str]) -> Iterable[Iterable[int]]:
    """
    Split rows on whitespace then transpose to get columns
    """
    rows = [[int(x) for x in row.split()] for row in row_strings]
    return zip(*rows)


def extract_columns_part_2(row_strings: list[str]) -> Iterable[Iterable[int]]:
    """
    Concat digits vertically. Groups are separated by a column of whitespace.
    """
    columns = list(
        digits_to_num([int(c) for c in col if c.strip()]) for col in zip(*row_strings)
    )
    grouped_columns = [
        list(group)
        for value, group in itertools.groupby(columns, key=lambda x: x != 0)
        if value  # keep only the non-zero groups
    ]
    return grouped_columns


def solve(
    row_strings: list[str],
    ops: list[Callable[[Any, Any], Any]],
    extract_columns_function: Callable[[list[str]], Iterable[Iterable[int]]],
):
    columns = extract_columns_function(row_strings)
    return calc_columns(ops, columns)


def main() -> None:
    lines = read_input()
    *row_strings, operators_string = lines
    ops = [operators[o] for o in operators_string.split()]

    part_1 = solve(row_strings, ops, extract_columns_part_1)
    print(f"{part_1=}")

    part_2 = solve(row_strings, ops, extract_columns_part_2)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day06.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
