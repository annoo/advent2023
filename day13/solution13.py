import numpy as np
from numpy.typing import NDArray

puzzle_input = "input13.txt"


def split_input_to_maps(filename) -> list[str]:
    with open(filename, 'r') as file:
        content = file.read()
    maps = content.split('\n\n')
    return maps


def transform_map_to_array_grid(mini_map: str) -> NDArray:
    grid_str = mini_map.replace("#", "1").replace(".", "0").splitlines()
    grid = [[int(char) for char in line] for line in grid_str]
    grid = np.array(grid)
    return grid


def detect_vertical_mirror(map: NDArray) -> int:
    # left side_compare
    # from big to small
    n_of_cols = map.shape[1]  # 2nd dimension of matix, 0-based

    for cut_off_line in range(n_of_cols, 1, -1):
        part_of_map = map[:, :cut_off_line]
        if np.array_equal(part_of_map, np.fliplr(part_of_map)):
            return cut_off_line // 2
    # right side_compare
    # from big to small
    for cut_off_line in range(n_of_cols - 1):
        part_of_map = map[:, cut_off_line:]
        if np.array_equal(part_of_map, np.fliplr(part_of_map)):
            return (n_of_cols // 2) + 1

    return 0


def detect_horizontal_mirror(map: NDArray) -> int:
    n_of_rows = map.shape[0]

    for cut_off_column in range(n_of_rows, 1, -1):
        part_of_map = map[:cut_off_column]
        if np.array_equal(part_of_map, np.flipud(part_of_map)):
            return cut_off_column // 2
    for cut_off_column in range(n_of_rows - 1):
        part_of_map = map[cut_off_column:]
        if np.array_equal(part_of_map, np.flipud(part_of_map)):
            return (n_of_rows // 2) + 1

    return 0


def solve_part1(input_data) -> int:
    maps = split_input_to_maps(input_data)
    vertical_mirrors = []
    horizontal_mirrors = []
    for map in maps:
        grid = transform_map_to_array_grid(map)
        vertical_mirrors.append(detect_vertical_mirror(grid))
        horizontal_mirrors.append(detect_horizontal_mirror(grid))

    return (sum(vertical_mirrors) +
            sum([x * 100 for x in horizontal_mirrors]))


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
