import pytest
from solution18 import read_input, solve_part1, solve_part2

test_input = "test_input18.txt"


def test_read_input():
    read_input(test_input)


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        # (1, "test_input15.txt", 1320),
        (2, "test_input18.txt", 62),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
