import matplotlib.pyplot as plt
import pytest
from solution16 import build_energy_grid, build_grid, solve_part1, solve_part2

test_input = "test_input16.txt"


def test_show_beam():
    grid = build_grid(test_input)
    energy_grid = build_energy_grid(grid)
    plt.imshow(energy_grid, cmap="Greys")
    plt.colorbar()
    plt.title("Beam Path Visualization")
    plt.show()


@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        # (1, "test_input15.txt", 1320),
        (2, "test_input15.txt", 145),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
