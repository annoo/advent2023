from dataclasses import dataclass
from enum import Enum
from typing import Optional

import numpy as np
from numpy import ndarray

puzzle_input = "input18.txt"


@dataclass
class Point:
    x: int
    y: int


class Orientation(Enum):
    NORTH = "U"
    EAST = "R"
    SOUTH = "D"
    WEST = "L"

class Direction(Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"


@dataclass
class DigStep:
    # from_: Direction
    to_: Direction
    distance: int
    color: int


# def read_input(input_data) -> list:
#     steps = []
#     with open(input_data, "r") as file:
#         from_= Direction.UP
#         for y, line in enumerate(file):
#             direction, distance, color = line.rstrip().split(" ")
#             dig = DigStep(from_=from_, to_=direction, distance=distance, color=color)
#             steps.append(dig)
#             from_ = direction
#     return steps


def read_input(input_data) -> list:
    steps = []
    with open(input_data, "r") as file:
        for y, line in enumerate(file):
            direction, distance, color = line.rstrip().split(" ")
            direction = Direction(direction)
            dig = DigStep(to_=direction, distance=distance, color=color)
            steps.append(dig)
    return steps

def build_grid(steps: list) -> list:
    grid = []
    origin = Point(0,0)
    for step in steps:
        pass



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
