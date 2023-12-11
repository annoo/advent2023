from dataclasses import dataclass
from functools import reduce

puzzle_input = "input11.txt"


def read_input(input_data) -> list[tuple[int]]:
    with open(input_data) as file:
        for line in file:
            if "Time" in line:
                times = [int(n) for n in line.removeprefix("Time:").strip().split()]
            if "Distance" in line:
                distances = [int(n) for n in line.removeprefix("Distance:").strip().split()]
        return list(zip(times, distances))





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
