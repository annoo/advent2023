import re
from dataclasses import asdict, dataclass
from enum import Enum
from typing import Optional

puzzle_input = "input15.txt"


class Operation(Enum):
    REMOVE = "-"
    INSERT = "="


@dataclass
class Lens:
    label: str
    initial_box: int
    operation: Operation
    focal_length: Optional[int] = None


# @dataclass
# class Box:
#     number: int
#     slots: list[Lens]


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


# def detect_label(step: str) -> str:
#     select_letters = re.compile('[a-z]+')
#     return select_letters.match(step).group()
#
#
# def detect_focal_length(step:str) -> int | None:
#     select_digit = re.compile('[0-9]')
#     return int(select_digit.match(step).group())


def recognize_lens(step: str) -> Lens:
    split_pattern = re.compile(r'([a-z]+)([=-])(\d)?')
    label, operation, focus_length = split_pattern.match(step).groups()
    initial_box = run_algorithm(label)
    operation = Operation(value=operation)
    focus_length = int(focus_length) if focus_length else None
    return Lens(label, initial_box, operation, focus_length)


# def initialization_sequence(input_data) -> dict:
#     steps = read_input(input_data)
#     boxes = {n: [] for n in range(256)}
#     for step in steps:
#         lens = recognize_lens(step)
#         boxes[lens.initial_box].append(lens)
#     return boxes


def solve_part1(input_data) -> int:
    steps = read_input(input_data)
    total = []
    for step in steps:
        total.append(run_algorithm(step))
    return sum(total)


def calc_focus_power_per_lens(boxes: dict) -> list[int]:
    focussing_power_per_lens = []
    for box_number, lenses in boxes.items():
        for i, lens in enumerate(lenses):
            focus_power = (box_number + 1) * (i + 1) * lens.focal_length
            focussing_power_per_lens.append(focus_power)
    return focussing_power_per_lens


def solve_part2(input_data) -> int:
    boxes = {n: [] for n in range(256)}
    steps = read_input(input_data)
    for step in steps:
        new_lens = recognize_lens(step)
        lens_slots = boxes[new_lens.initial_box]
        if new_lens.operation == Operation.REMOVE:
            boxes[new_lens.initial_box] = [lens for lens in lens_slots if lens.label != new_lens.label]
        if new_lens.operation == Operation.INSERT:
            if new_lens.label in [lens.label for lens in lens_slots]:
                boxes[new_lens.initial_box] = [
                    new_lens if lens.label == new_lens.label else lens
                    for lens in lens_slots]
            else:
                lens_slots.append(new_lens)

    focussing_power_per_lens = calc_focus_power_per_lens(boxes)
    return sum(focussing_power_per_lens)


def generate_solution(puzzle):
    # solution1 = solve_part1(puzzle)
    solution2 = solve_part2(puzzle)
    # print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
