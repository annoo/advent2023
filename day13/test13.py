import pytest

from solution13 import solve_part1, solve_part2

puzzle_input = "input13.txt"


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, puzzle_input, 405),
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
