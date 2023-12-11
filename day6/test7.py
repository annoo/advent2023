import pytest
from solution7 import solve_part1, solve_part2


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input7.txt", 6440),
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
