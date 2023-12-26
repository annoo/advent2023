from itertools import combinations

import pytest
from solution11 import (
    Galaxy,
    Point,
    build_grid,
    calculate_shortest_path,
    detect_galaxies,
    solve_part1,
    solve_part2,
    space_expansion,
)

test_input = "test_input11.txt"


def test_expansion():
    expected_grid = [
                    "....#........",
                    ".........#...",
                    "#............",
                    ".............",
                    ".............",
                    "........#....",
                    ".#...........",
                    "............#",
                    ".............",
                    ".............",
                    ".........#...",
                    "#....#.......",
                    ]
    grid = build_grid(input_data=test_input)
    assert space_expansion(grid) == expected_grid


def test_detect_galaxies():
    expected_galaxies = [Galaxy(1, Point(3, 0)),
                         Galaxy(2, Point(7, 1)),
                         Galaxy(3, Point(0, 2))]
    mini_grid = ["...#......",
                 ".......#..",
                 "#........."]
    assert detect_galaxies(mini_grid) == expected_galaxies


@pytest.mark.parametrize("pair_of_galaxies, expected_distance", [
    ((Galaxy(5, Point(1, 6)), Galaxy(9, Point(5, 11))), 9),
    ((Galaxy(1, Point(4, 0)), Galaxy(7, Point(9, 10))), 15),
    ((Galaxy(3, Point(0, 2)), Galaxy(6, Point(12, 7))), 17),
    ((Galaxy(8, Point(0, 11)), Galaxy(9, Point(5, 11))), 5),

])
def test_shortest_path(pair_of_galaxies, expected_distance):
    assert calculate_shortest_path(pair_of_galaxies) == expected_distance


def test_to_see_output():
    grid = build_grid(test_input)
    galaxies = detect_galaxies(grid)
    pairs = combinations(galaxies, 2)
    shortest_paths = []
    for pair in pairs:
        shortest_paths.append(calculate_shortest_path(pair))
    return galaxies, shortest_paths

@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input11.txt", 374),
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
