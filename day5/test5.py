import pytest
from solution5 import solve_part1, solve_part2

input_data = "input5.txt"


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input5.txt", 35),
        # (2, "test_input4.txt", 30),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
