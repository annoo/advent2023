import pytest
from solution15 import (
    Lens,
    Operation,
    recognize_lens,
    run_algorithm,
    solve_part1,
    solve_part2,
)

test_input = "test_input15.txt"


def test_HASH_is_52():
    assert run_algorithm("HASH") == 52


@pytest.mark.parametrize("hash, expected_tuple", [
    ("rn=1", Lens("rn", 0, Operation.INSERT, 1)),
    ("cm-", Lens("cm", 0, Operation.REMOVE, None)),
    ("qp=3", Lens("qp", 1, Operation.INSERT, 3)),
])
def test_from_hash_to_tuple(hash, expected_tuple):
    assert recognize_lens(hash) == expected_tuple


# def test_initialization_pattern():
#     expected_box_numbers = [30, 253, 97, 47, 14, 180, 9, 197, 48, 214, 231]
#     boxes = initialization_sequence(test_input)
#     assert all(boxes[n][0].initial_box == n for n in expected_box_numbers



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
