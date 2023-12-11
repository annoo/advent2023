import pytest
from solution5b import (
    solve_part1,
    solve_part2,
    sort_ranges,
    unpack_in_seed_tuples,
)


def test_number_of_seeds():
    seeds = [79, 14, 55, 13]
    expected_number_of_total_seeds = 27
    seeds_ranges = unpack_in_seed_tuples(seeds)
    number = sum(l for _, _, l in seeds_ranges)
    assert number == expected_number_of_total_seeds


expected_seeds = [79, 14, 55, 13]
expected_maps = {
    'seed_to_soil_map': [(50, 98, 2), (52, 50, 48)],
    'soil_to_fertilizer_map': [(0, 15, 37), (37, 52, 2), (39, 0, 15)],
    'fertilizer_to_water_map': [(49, 53, 8), (0, 11, 42), (42, 0, 7), (57, 7, 4)],
    'water_to_light_map': [(88, 18, 7), (18, 25, 70)],
    'light_to_temperature_map': [(45, 77, 23), (81, 45, 19), (68, 64, 13)],
    'temperature_to_humidity_map': [(0, 69, 1), (1, 0, 69)],
    'humidity_to_location_map': [(60, 56, 37), (56, 93, 4)]
}

@pytest.mark.parametrize("mapping, expected_sorted_mapping", [
    ([(50, 98, 2), (52, 50, 48)], [(52, 50, 48), (50, 98, 2)]),
    ([(0, 15, 37), (37, 52, 2), (39, 0, 15)], [(39, 0, 15), (0, 15, 37), (37, 52, 2)]),
])
def test_sort_ranges(mapping, expected_sorted_mapping):
    assert sort_ranges(mapping) == expected_sorted_mapping





@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        (1, "test_input5.txt", 35),
        # (1, "input5.txt", 0),
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
