from dataclasses import dataclass
from functools import reduce

puzzle_input = "input5.txt"


# I realize fully well that there is a relationship between the numbers...

@dataclass
class Map:
    source: list[range]
    destination: list[range]

    def _find_source_range(self, number: int) -> int | None:
        for i, rng in enumerate(self.source):
            if number in rng:
                return i
        return None

    def _find_index(self, which_range: int, number: int) -> int | None:
        for j, value in enumerate(self.source[which_range]):
            if number == value:
                return j
        return None

    def _find_destination_value(self, which_range: int, index: int) -> int | None:
        if which_range is not None and index is not None:
            return self.destination[which_range][index]
        return None

    def map_number_to_destination(self, number: int) -> int:
        which_range = self._find_source_range(number)
        if which_range is not None:
            index = self._find_index(which_range, number)
            return self._find_destination_value(which_range, index)
        else:
            return number


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


def read_range(range_: list) -> tuple[range, range]:
    # cleanup
    source_range_start = range_[1]
    destination_range_start = range_[0]
    length = range_[2]
    source_range_stop = source_range_start + length
    destination_range_stop = destination_range_start + length
    decyphered_source = range(source_range_start, source_range_stop)
    decyphered_destination = range(destination_range_start,
                                   destination_range_stop)
    return decyphered_source, decyphered_destination


def decypher_map(scrambled_map: list[list[int]]) -> Map:
    # cleanup
    source_points = []
    destination_points = []
    for part in scrambled_map:
        decyphered_source, decyphered_destination = read_range(part)
        source_points.append(decyphered_source)
        destination_points.append(decyphered_destination)
    return Map(source=source_points, destination=destination_points)


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
    pass


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    # solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    # print(f"\solution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
