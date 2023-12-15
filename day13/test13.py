import numpy as np
import pytest

from solution13 import (
    detect_horizontal_mirror,
    detect_vertical_mirror,
    solve_part1,
    solve_part2,
    split_input_to_maps,
    transform_map_to_array_grid,
)

puzzle_input = "input13.txt"
test_input = "test_input13.txt"


def test_split_maps_into_list_of_minimaps():
    maps = split_input_to_maps(test_input)
    expected_first_map = ("#.##..##.\n"
                          "..#.##.#.\n"
                          "##......#\n"
                          "##......#\n"
                          "..#.##.#.\n"
                          "..##..##.\n"
                          "#.#.##.#.")
    assert maps[0] == expected_first_map


def test_transform_str_to_number_grid():
    expected_line1 = np.array([1, 0, 1, 1, 0, 0, 1, 1, 0])
    expected_line7 = np.array([1, 0, 1, 0, 1, 1, 0, 1, 0])

    maps = split_input_to_maps(test_input)

    grid = transform_map_to_array_grid(maps[0])
    assert np.array_equal(grid[0], expected_line1)
    assert np.array_equal(grid[6], expected_line7)


@pytest.mark.parametrize("simple_line, expected_mirror", [
    [np.array([[1, 1, 0, 0, 1, 1]]), 3],
    [np.array([[1, 0, 0, 1, 1]]), 2],
    [np.array([[2, 1, 0, 0, 1]]), 3],
    [np.array([[0, 0, 1]]), 1],
    [np.array([[0, 3, 4, 2]]), 0],  # representation of != columns
    [np.array([[0, 1, 0, 1]]), 0]
])
def test_detect_vertical_mirror_simple(simple_line, expected_mirror):
    assert detect_vertical_mirror(simple_line) == expected_mirror


maps = split_input_to_maps(test_input)
grid1 = transform_map_to_array_grid(maps[0])
grid2 = transform_map_to_array_grid(maps[1])


def test_detect_vertical_mirror_grid1():
    expected_mirror_line_map1 = 5
    assert detect_vertical_mirror(grid1) == expected_mirror_line_map1


def test_detect_vertical_mirror_grid2():
    expected_mirror_line_map2 = 0
    assert detect_vertical_mirror(grid2) == expected_mirror_line_map2


@pytest.mark.parametrize("simple_column, expected_mirror", [
    [np.array([[1], [1], [0], [0], [1], [1]]), 3],
    [np.array([[1], [0], [0], [1], [1]]), 2],
    [np.array([[2], [1], [0], [0], [1]]), 3],  # to avoid 2 mirrors
    [np.array([[0], [0], [1]]), 1],
    [np.array([[0], [2], [1], [4]]), 0],
    [np.array([[0], [1], [0], [1]]), 0]
])
def test_detect_horizontal_mirror_simple(simple_column, expected_mirror):
    assert detect_horizontal_mirror(simple_column) == expected_mirror


def test_detect_horizontal_mirror_grid1():
    expected_mirror_line_map1 = 0
    assert detect_horizontal_mirror(grid1) == expected_mirror_line_map1


def test_detect_horizontal_mirror_grid2():
    expected_mirror_line_map2 = 4
    assert detect_horizontal_mirror(grid2) == expected_mirror_line_map2

@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, test_input, 405),
        # (2, "test_input7.txt", 0),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
