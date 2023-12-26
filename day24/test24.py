import pytest
from solution24 import solve_part1, solve_part2

test_input = "test_input24.txt"


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, test_input, 2),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
