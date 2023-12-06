import pytest
from shapely import LineString, Point
from solution import (
    NumberLine,
    Star,
    Symbol,
    analyze_grid_for_numbers_and_stars,
    analyze_grid_for_numbers_and_symbols,
    build_grid,
    calculate_gear_ratio,
    is_number_adjacent_to_symbol,
    list_gears,
    list_part_numbers,
    solve_part1,
    solve_part2,
)

simple_input = ["1..", "..$", ".12"]


@pytest.mark.parametrize(
    "filename, expected_output",
    [
        (
            "test_input_a.txt",
            [
                "467..114..",
                "...*......",
                "..35..633.",
                "......#...",
                "617*......",
                ".....+.58.",
                "..592.....",
                "......755.",
                "...$.*....",
                ".664.598..",
            ],
        )
    ],
)
def test_correct_grid_gets_built(filename, expected_output):
    assert build_grid(filename) == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            simple_input,
            (
                [
                    NumberLine("1", LineString([(0, 0), (0, 0)])),
                    NumberLine("12", LineString([(1, 2), (2, 2)])),
                ],
                [Symbol("$", Point(2, 1))],
            ),
        )
    ],
)
def test_get_numbers_and_symbols_from_grid(input_data, expected_output):
    assert analyze_grid_for_numbers_and_symbols(input_data) == expected_output


@pytest.mark.parametrize(
    "number, symbols, expected_output",
    [
        (
            NumberLine("1", LineString([(0, 0), (0, 0)])),
            [Symbol("$", Point(2, 1))],
            False,
        ),
        (
            NumberLine("12", LineString([(1, 2), (2, 2)])),
            [Symbol("$", Point(2, 1))],
            True,
        ),
    ],
)
def test_numbers_have_symbol_adjacent(number, symbols, expected_output):
    assert is_number_adjacent_to_symbol(number, symbols) == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (
            simple_input,
            [
                NumberLine("1", LineString([(0, 0), (0, 0)])),
                NumberLine("12", LineString([(1, 2), (2, 2)])),
            ],
        )
    ],
)
def test_get_numbers_from_grid(input_data, expected_output):
    numbers, _ = analyze_grid_for_numbers_and_symbols(input_data)
    assert numbers == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (["*..", ".1.", "..."], True),
        ([".*.", ".1.", "..."], True),
        (["..*", ".1.", "..."], True),
        (["...", "*1.", "..."], True),
        (["...", ".1*", "..."], True),
        (["...", ".1.", "*.."], True),
        (["...", ".1.", ".*."], True),
        (["...", ".1.", "..*"], True),
        ([".....", ".1...", "...*."], False),
    ],
)
def test_number_touching_a_symbol_is_detected_correctly(
    input_data, expected_output
):
    number, symbols = analyze_grid_for_numbers_and_symbols(input_data)
    assert is_number_adjacent_to_symbol(number[0], symbols) == expected_output


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        (simple_input, [12]),
        ("test_input_a.txt", [467, 35, 633, 617, 592, 755, 664, 598]),
    ],
)
def test_get_part_numbers_and_symbols_from_grid(input_data, expected_output):
    if input_data == "test_input_a.txt":
        grid = build_grid(input_data)
    else:
        grid = input_data
    numbers, symbols = analyze_grid_for_numbers_and_symbols(grid)
    part_numbers = list_part_numbers(numbers=numbers, symbols=symbols)
    assert part_numbers == expected_output


def test_detects_correct_amount_of_stars():
    grid = build_grid("test_input_a.txt")
    _, stars = analyze_grid_for_numbers_and_stars(grid)
    assert len(stars) == 3


def test_detects_correct_amount_of_gears():
    grid = build_grid("test_input_a.txt")
    numbers, stars = analyze_grid_for_numbers_and_stars(grid)
    gears = list_gears(stars, numbers)
    assert len(gears) == 2


@pytest.mark.parametrize(
    ["gear", "expected_gear_ratio"],
    [(Star("*", Point(3, 1)), 16345), (Star("*", Point(5, 8)), 451490)],
)
def test_gear_ratio_is_correct(gear, expected_gear_ratio):
    grid = build_grid("test_input_a.txt")
    numbers, stars = analyze_grid_for_numbers_and_stars(grid)
    assert gear in stars

    gear_ratio = calculate_gear_ratio(gear, numbers)
    assert gear_ratio == expected_gear_ratio


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input_a.txt", 4361),
        (2, "test_input_a.txt", 467835),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
