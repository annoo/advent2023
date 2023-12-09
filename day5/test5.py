import pytest
from solution5 import (
    Map,
    decypher_map,
    read_range,
    solve_part1,
    solve_part2,
    unpack_in_seed_ranges,
)


def test_number_of_seeds():
    seeds = [79, 14, 55, 13]
    expected_number_of_total_seeds = 27
    seeds_ranges = unpack_in_seed_ranges(seeds)
    number = sum(len(range) for range in seeds_ranges)
    assert number == expected_number_of_total_seeds


@pytest.mark.parametrize(
    ["scrambled_part", "expected_source_range", "expected_destination_range"],
[
    ([50, 98, 2], range(98, 98+2), range(50, 50+2)),
    ([52, 50, 48], range(50, 50+48), range(52, 52+48))
])
def test_decypher_part_of_map(scrambled_part, expected_source_range,
                              expected_destination_range):
    decyphered_source, decyphered_destination= read_range(scrambled_part)
    assert decyphered_source == expected_source_range
    assert decyphered_destination == expected_destination_range


@pytest.mark.parametrize(
    ["scrambled_map", "expected_mapping"],
[
    (
            [[50, 98, 2], [52, 50, 48]],
            {src: dest for src_rng, dest_rng
             in zip([range(98, 98+2), range(50, 50+48)],
                    [range(50, 50+2), range(52, 52+48)])
                       for src, dest in zip(src_rng, dest_rng)}
    )
])
def test_decypher_whole_map(scrambled_map, expected_mapping):
    decyphered_map = decypher_map(scrambled_map)
    assert decyphered_map.mapping == expected_mapping


test_map = Map(source=[range(98, 98+2), range(50, 50+48)],
               destination=[range(50, 50+2), range(52, 52+48)])

@pytest.mark.parametrize(
    ["source_number", "expected_destination_number"],
[
    (79, 81),
    (14, 14),
    (55, 57),
    (13, 13),

])
def test_map_returns_correct_mapping_for_number(source_number,
                                                expected_destination_number):
    destination_number = test_map.map_number_to_destination(source_number)
    assert destination_number == expected_destination_number



@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input5.txt", 35),
        (1, "input5.txt", 0),
        (2, "test_input5.txt", 46),
        # (2, "input5.txt", 0),
    ],
)
def test_solve(part, input_data, expected_output):

    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
