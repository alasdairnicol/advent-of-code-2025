#!/usr/bin/env python
import operator
from typing import Callable, Any
import functools

operators = {
    "+": operator.add,
    "*": operator.mul,
}


def digits_to_num(digits):
    return functools.reduce(lambda x, y: 10 * x + y, digits, 0)


def calc_column(op, column):
    return functools.reduce(op, column)


def calc_columns(ops, columns):
    return sum(calc_column(op, column) for op, column in zip(ops, columns))


def do_part_1(row_strings: list[str], ops: list[Callable[[Any, Any], Any]]) -> int:
    rows = [[int(x) for x in row.split()] for row in row_strings]
    columns = zip(*rows)
    return calc_columns(ops, columns)


def do_part_2(row_strings: list[str], ops: list[Callable[[Any, Any], Any]]) -> int:
    new_columns = list(
        digits_to_num([int(x) for x in l if x.strip()]) for l in zip(*row_strings)
    )
    batched_columns = []
    batch = []
    for column in new_columns:
        if column == 0:
            batched_columns.append(batch)
            batch = []
        else:
            batch.append(column)
    return calc_columns(ops, batched_columns)


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
