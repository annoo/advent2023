from dataclasses import dataclass
from functools import reduce
from typing import Iterator

puzzle_input = "input5.txt"


# I realize fully well that there is a relationship between the numbers...

@dataclass
class Map:
    mapping: dict[int, int]

    def __init__(self, source: list[range], destination: list[range]) -> None:
        self.mapping = self._build_mapping(source, destination)

    def _build_mapping(self, source: list[range], destination: list[range]) -> \
    dict[int, int]:
        mapping = {}
        for src_range, destination_range in zip(source, destination):
            for src_value, destination_value in zip(src_range,
                                                    destination_range):
                mapping[src_value] = destination_value
        return mapping

    def map_number_to_destination(self, number: int) -> int:
        return self.mapping.get(number, number) # else: return self


def divide_input_parts(input_data) -> tuple[dict, list]:
    # name with .removesuffix(" map") vs pre-built list
    # work with iterators and takewhile
    maps = {
        name: []
        for name in [
            "seed_to_soil_map",
            "soil_to_fertilizer_map",
            "fertilizer_to_water_map",
            "water_to_light_map",
            "light_to_temperature_map",
            "temperature_to_humidity_map",
            "humidity_to_location_map",
        ]
    }
    seeds = []

    with open(input_data) as file:
        map_iterator = iter(maps.values())

        for line in file:
            if line.startswith("seeds"):
                _, seed_numbers = line.rstrip().split(": ")

                seeds = [int(s) for s in seed_numbers.split(" ")]
                continue

            elif line.strip() == "":
                continue

            if "map" in line:
                map_to_set = next(map_iterator)
                continue

            map_to_set.append([int(n) for n in line.rstrip().split(" ")])

    return maps, seeds


def unpack_in_seed_ranges(seeds: list[int]) -> Iterator[range]:
    for start_seed, length in zip(seeds[::2], seeds[1::2]):
        yield range(start_seed, start_seed+length)


def read_range(range_: list) -> tuple[range, range]:
    destination_range_start, source_range_start, length = range_
    return (range(source_range_start, source_range_start + length),
            range(destination_range_start, destination_range_start + length))


def decypher_map(scrambled_map: list[list[int]]) -> Map:
    # cleanup
    source_points = []
    destination_points = []
    for part in scrambled_map:
        decyphered_source, decyphered_destination = read_range(part)
        source_points.append(decyphered_source)
        destination_points.append(decyphered_destination)
    return Map(source_points, destination_points)


def process_seed_through_maps(seed: int, maps: list[Map]) -> int:
    return reduce(lambda number, map: map.map_number_to_destination(number)
                                      or number,
                  maps,
                  seed)


def solve_part1(input_data) -> int:
    maps, seeds = divide_input_parts(input_data)
    maps = [decypher_map(m) for m in maps.values()]

    return min([process_seed_through_maps(seed, maps) for seed in seeds])


def solve_part2(input_data):
    maps, seeds = divide_input_parts(input_data)
    maps = [decypher_map(m) for m in maps.values()]
    seed_ranges = unpack_in_seed_ranges(seeds)
    processed_seeds = [process_seed_through_maps(seed, maps)
                       for seed_range in seed_ranges
                       for seed in seed_range]
    return min(processed_seeds)


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    # solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    # print(f"\solution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
