from dataclasses import dataclass
from functools import reduce

puzzle_input = "input15.txt"


def read_input(input_data) -> list[str]:
    with open(input_data, 'r') as file:
        for line in file:
            steps = line.split(",")
    return steps


def run_algorithm(step: str) -> int:
    current_value = 0
    for char in step:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def solve_part1(input_data) -> int:
    steps = read_input(input_data)
    total = []
    for step in steps:
        total.append(run_algorithm(step))
    return sum(total)

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
