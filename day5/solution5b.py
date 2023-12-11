from operator import itemgetter

puzzle_input = "input5.txt"


# I realize fully well that there is a relationship between the numbers...

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
                seed_numbers = line.rstrip().removeprefix("seeds: ")

                seeds = [int(s) for s in seed_numbers.split(" ")]
                continue

            elif line.strip() == "":
                continue

            if "map" in line:
                map_to_set = next(map_iterator)
                continue

            map_to_set.append(tuple([int(n) for n in line.rstrip().split(" ")]))

    return maps, seeds


def unpack_in_seed_tuples(seeds: list[int]) -> tuple[int, int, int]:
    seed_tuples = []
    for start_seed, length in zip(seeds[::2], seeds[1::2]):
        seed_tuples.append((start_seed, 0, length))  # matrices : 0 or 1??
    return seed_tuples


def sort_ranges(mapping: list[tuple[int, int, int]]) -> list[tuple[int, int, int]]:
    return sorted(mapping, key=itemgetter(1))  # sort by source


def solve_part1(input_data) -> int:
    pass


def solve_part2(input_data):
    maps, seeds = divide_input_parts(input_data)
    for name in maps:
        maps[name] = sort_ranges(maps[name])
    seeds_ranges = unpack_in_seed_tuples(seeds)


def generate_solution(puzzle):
    # solution1 = solve_part1(puzzle)
    solution2 = solve_part2(puzzle)
    # print(f"\n\nsolution part 1 : {solution1}")
    print(f"\solution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
