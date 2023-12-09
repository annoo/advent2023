import pytest
from solution6 import (
    calc_distance,
    is_win,
    read_input,
    solve_part1,
    solve_part2,
)


def test_read_input_returns_races():
    expected_races = [(7, 9), (15, 40), (30, 200)]
    assert read_input("test_input6.txt") == expected_races

@pytest.mark.parametrize(
    "push_length, expected_distance",
    [
        (0, 0),
        (1, 6),
        (2, 10),
        (3, 12),
        (4, 12),
        (5, 10),
        (6, 6),
        (7, 0)
    ])
def test_calculate_race_result(push_length, expected_distance):
    time, winning_distance = (7, 9)
    assert calc_distance(time, push_length) == expected_distance


@pytest.mark.parametrize(
    "race_distance, expected_win",
    [
        (0, False),
        (6, False),
        (10, True),
        (12, True),
        (12, True),
        (10, True),
        (6, False),
        (0, False),
    ])
def test_is_win(race_distance, expected_win):
    time, winning_distance = (7, 9)
    assert is_win(winning_distance, race_distance) == expected_win


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input6.txt", 288),
        (2, (71530, 940200), 71503),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
