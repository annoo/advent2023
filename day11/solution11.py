from dataclasses import dataclass
from itertools import combinations

puzzle_input = "input11.txt"


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Galaxy:
    name: int
    coords: Point


def build_grid(input_data) -> list:
    grid = []
    with open(input_data) as file:
        grid = [line.strip() for line in file]
    return grid


def space_expansion(grid: list[str]) -> list[str]:
    row_expanded_grid = []
    for line in grid:
        row_expanded_grid.append(line)
        if "#" not in line:
            row_expanded_grid.append(line)

    cols_expanded_grid = []
    for line in row_expanded_grid:
        new_line = ''
        for x in range(len(line)):
            if not any(grid[y][x] == "#" for y in range(len(grid))):
                new_line += line[x] * 2
            else:
                new_line += line[x]
        cols_expanded_grid.append(new_line)
    return cols_expanded_grid


def detect_galaxies(grid: list[str]) -> list[Galaxy]:
    galaxies = []
    name = 0
    for y, line in enumerate(grid):
        x = 0

        while x < len(line):
            char = line[x]
            if char == "#":
                coords = Point(x, y)
                name += 1
                galaxy = Galaxy(name, coords)
                galaxies.append(galaxy)

            x += 1
    return galaxies


def calculate_shortest_path(pair_of_galaxies: tuple[Galaxy, Galaxy]) -> int:
    a, b = pair_of_galaxies
    return abs(a.coords.x - b.coords.x) + abs(a.coords.y - b.coords.y)


def solve_part1(input_data) -> int:
    grid = build_grid(input_data)
    grid = space_expansion(grid)
    galaxies = detect_galaxies(grid)
    pairs = combinations(galaxies, 2)
    shortest_paths = []
    for pair in pairs:
        shortest_paths.append(calculate_shortest_path(pair))
    return sum(shortest_paths)


def solve_part2(input_data) -> int:
    pass
    return 1


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    # solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    # print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
