import pytest
from solution4 import solve_part1, solve_part2, total_number_of_initial_tickets

input_data = "input4.txt"


def test_number_of_initial_tickets_is_calculated_correctly():
    assert total_number_of_initial_tickets(input_data) == 208
    assert total_number_of_initial_tickets("test_input4.txt") == 6


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input4.txt", 13),
        (2, "test_input4.txt", 30),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
