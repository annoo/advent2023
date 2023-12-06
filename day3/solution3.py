from dataclasses import dataclass
from functools import reduce

from shapely import LineString, Point

puzzle_input = "input3.txt"


@dataclass
class NumberLine:
    name: str
    coords: LineString


@dataclass
class Symbol:
    name: str
    coords: Point


@dataclass
class Star:
    name: str
    coords: Point


def build_grid(input_data) -> list:
    grid = []
    with open(input_data) as file:
        grid = [line.strip() for line in file]
    return grid


def analyze_grid_for_numbers_and_symbols(
    grid: list[str],
) -> tuple[list[NumberLine], list[Symbol]]:
    numbers: list[NumberLine] = []
    symbols: list[Symbol] = []

    for y, line in enumerate(grid):
        x = 0
        while x < len(line):
            char = line[x]

            if char.isdigit():
                number_str = ""
                start_x = x
                while x < len(line) and line[x].isdigit():
                    number_str += line[x]
                    x += 1
                end_x = x - 1  # the last coordinate is still ON the digit

                coords = LineString([(start_x, y), (end_x, y)])
                number_line = NumberLine(number_str, coords)
                numbers.append(number_line)
                continue

            elif char not in {"."}:
                coords = Point(x, y)
                name = line[x]
                symbol = Symbol(name, coords)
                symbols.append(symbol)

            x += 1
    return numbers, symbols


def analyze_grid_for_numbers_and_stars(
    grid: list[str],
) -> tuple[list[NumberLine], list[Star]]:
    numbers: list[NumberLine] = []
    stars: list[Star] = []

    for y, line in enumerate(grid):
        x = 0
        while x < len(line):
            char = line[x]

            if char.isdigit():
                number_str = ""
                start_x = x
                while x < len(line) and line[x].isdigit():
                    number_str += line[x]
                    x += 1
                end_x = x - 1  # the last coordinate is still ON the digit

                coords = LineString([(start_x, y), (end_x, y)])
                number_line = NumberLine(number_str, coords)
                numbers.append(number_line)
                continue

            elif char == "*":
                coords = Point(x, y)
                name = line[x]
                potential_gear = Star(name, coords)
                stars.append(potential_gear)

            x += 1
    return numbers, stars


def is_star_a_gear(star: Star, numbers: list[NumberLine]) -> bool:
    touch_two = 0
    for number in numbers:
        if star.coords.distance(number.coords) < 2:
            touch_two += 1
    if touch_two == 2:
        return True
    return False


def list_gears(stars: list[Star], numbers: list[NumberLine]) -> list[Star]:
    gears = []
    for star in stars:
        if is_star_a_gear(star, numbers):
            gears.append(star)
    return gears


def calculate_gear_ratio(gear: Star, numbers: list[NumberLine]) -> int:
    ratios = []
    for number in numbers:
        if gear.coords.distance(number.coords) < 2:
            ratios.append(int(number.name))
    return reduce(lambda x, y: x * y, ratios)


def is_number_adjacent_to_symbol(
    number: NumberLine, symbols: list[Symbol]
) -> bool:
    for symbol in symbols:
        if number.coords.distance(symbol.coords) < 2:
            return True
    return False


def list_part_numbers(
    numbers: list[NumberLine], symbols: list[Symbol]
) -> list[int]:
    part_numbers = []
    for number in numbers:
        if is_number_adjacent_to_symbol(number, symbols=symbols):
            part_numbers.append(int(number.name))
    return part_numbers


def solve_part1(input_data):
    grid = build_grid(input_data)
    numbers, symbols = analyze_grid_for_numbers_and_symbols(grid)
    part_numbers = list_part_numbers(numbers=numbers, symbols=symbols)
    result = sum(n for n in part_numbers)
    return result


def solve_part2(input_data):
    total_gear_ratio = []
    grid = build_grid(input_data)
    numbers, stars = analyze_grid_for_numbers_and_stars(grid)
    gears = list_gears(stars, numbers)
    for gear in gears:
        ratio = calculate_gear_ratio(gear, numbers)
        total_gear_ratio.append(ratio)
    result = sum(n for n in total_gear_ratio)
    return result


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
