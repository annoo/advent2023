from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np
from numpy import ndarray

puzzle_input = "input16.txt"


class Orientation(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Point:
    x: int
    y: int


class Beam_focus:
    from_: Orientation
    to_: Orientation
    coords: Point


def build_grid(input_data) -> list:
    grid = []
    with open(input_data) as file:
        grid = [line.strip() for line in file]
    return grid


def build_energy_grid(grid) -> ndarray:
    rows = len(grid)
    cols = len(grid[0])
    return np.zeros((rows, cols))


def solve_part1(input_data) -> int:
    pass


def solve_part2(input_data) -> int:
    pass


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    # solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    # print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
