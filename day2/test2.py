import pytest
from solution import (
    calculate_cube_of_cubes,
    check_max_amount_of_cubes,
    solve_part1,
    solve_part2,
)


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ({"red": 4, "green": 2, "blue": 6}, 48),
        ({"red": 1, "green": 3, "blue": 4}, 12),
    ],
)
def test_cubing(input_data, expected_output):
    assert calculate_cube_of_cubes(input_data) == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            {"red": 4, "green": 2, "blue": 6},
        ),
        (
            "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            {"red": 1, "green": 3, "blue": 4},
        ),
    ],
)
def test_check_max_amount_of_cubes(input_data, expected_output):
    assert check_max_amount_of_cubes(input_data) == expected_output


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input_a.txt", 8),
        (2, "test_input_a.txt", 2286),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
