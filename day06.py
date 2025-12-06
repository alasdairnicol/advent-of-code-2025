#!/usr/bin/env python
import functools
import itertools
import operator
from typing import Callable, Iterable

# Type aliases
Column = Iterable[int]
IntOperator = Callable[[int, int], int]
ColumnExtractor = Callable[[list[str]], Iterable[Column]]


operators = {
    "+": operator.add,
    "*": operator.mul,
}


def digits_to_num(digits: Iterable[int]) -> int:
    return functools.reduce(lambda x, y: 10 * x + y, digits, 0)


def calc_column(op: IntOperator, column: Column) -> int:
    return functools.reduce(op, column)


def calc_columns(ops: list[IntOperator], columns: Iterable[Column]) -> int:
    return sum(calc_column(op, column) for op, column in zip(ops, columns))


def extract_columns_part_1(row_strings: list[str]) -> Iterable[Column]:
    """
    Split rows on whitespace then transpose to get columns
    """
    rows = [[int(x) for x in row.split()] for row in row_strings]
    return zip(*rows)


def extract_columns_part_2(row_strings: list[str]) -> Iterable[Column]:
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
    ops: list[IntOperator],
    extract_columns_function: Callable[[list[str]], Iterable[Column]],
) -> int:
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
