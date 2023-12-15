import pytest
from solution15 import run_algorithm, solve_part1, solve_part2


def test_HASH_is_52():
    assert run_algorithm("HASH") == 52
    

@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input15.txt", 1320),
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
