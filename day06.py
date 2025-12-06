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


def do_part_1(row_strings: list[str], ops: list[Callable[[Any, Any], Any]]) -> int:
    rows = [[int(x) for x in row.split()] for row in row_strings]
    columns = zip(*rows)
    return calc_columns(ops, columns)


def do_part_2(row_strings: list[str], ops: list[Callable[[Any, Any], Any]]) -> int:
    columns = list(
        digits_to_num([int(c) for c in col if c.strip()]) for col in zip(*row_strings)
    )
    grouped_columns = [
        list(group)
        for value, group in itertools.groupby(columns, key=lambda x: x != 0)
        if value  # keep only the non-zero groups
    ]
    return calc_columns(ops, grouped_columns)


def main() -> None:
    lines = read_input()
    *row_strings, operators_string = lines
    ops = [operators[o] for o in operators_string.split()]

    part_1 = do_part_1(row_strings, ops)
    print(f"{part_1=}")

    part_2 = do_part_2(row_strings, ops)
    print(f"{part_2=}")


def read_input() -> list[str]:
    with open("day06.txt") as f:
        return f.readlines()


if __name__ == "__main__":
    main()
