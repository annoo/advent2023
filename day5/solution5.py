puzzle_input = "input5.txt"

maps = {
    name: []
    for name in [
        "seeds",
        "seed_to_soil_map",
        "fertilizer_to_water_map",
        "water_to_light_map",
        "light_to_temperature_map",
        "temperature_to_humidity_map",
        "humidity_to_location_map",
    ]
}


def divide_input_parts(input_data):
    with open(input_data) as file:
        for line in file:
            map_iterator = iter(maps.values())
            map_to_set = next(map_iterator, None)
            if line.startswith("seeds"):
                _, seed_numbers = line.rstrip().split(": ")
                map_to_set.append(seed_numbers)
            elif line.strip() == "":
                map_to_set = None
                continue

            if map_to_set is None:
                map_to_set = next(map_iterator, None)
                continue

            map_to_set.append(line.rstrip().split(" "))


def solve_part1(input_data):
    numbers_to_add = []
    divide_input_parts(input_data)
    result = sum(n for n in numbers_to_add)
    return result


def total_number_of_initial_tickets(input_data):
    with open(input_data) as file:
        total = sum(1 for line in file)
    return total


def solve_part2(input_data):
    total_initial_tickets = total_number_of_initial_tickets(input_data)
    numbers_to_add = []

    result = sum(n for n in numbers_to_add)
    return result


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
