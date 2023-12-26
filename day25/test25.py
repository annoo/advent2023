import networkx as nx
import pytest
from solution25 import create_graph_from_input, solve_part1, solve_part2

test_input = "test_input25.txt"


def test_creating_graph():
    g = create_graph_from_input(test_input)
    assert g.number_of_nodes() == 22


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, test_input, 54),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
