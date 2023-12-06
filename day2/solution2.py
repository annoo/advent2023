from functools import reduce

puzzle_input = "input2.txt"


def is_impossible(cube_set: str) -> bool:
    max_values = {"red": 12, "green": 13, "blue": 14}
    number, color = cube_set.split(" ")
    number = int(number)

    return number > max_values.get(color)


def check_max_amount_of_cubes(cubes: str) -> dict:
    amount_of_cubes = {"red": 0, "green": 0, "blue": 0}
    for cube_set in cubes.replace(";", ",").split(", "):
        number, color = cube_set.split(" ")
        number = int(number)
        if number > amount_of_cubes.get(color):
            amount_of_cubes[color] = number
    return amount_of_cubes


def calculate_cube_of_cubes(amount_of_cubes: dict) -> int:
    return reduce(lambda x, y: x * y, amount_of_cubes.values(), 1)


def solve_part1(input_data):
    numbers_to_add = []
    with open(input_data) as file:
        for line in file:
            game, cubes = line.rstrip().split(": ")
            _, game_ID = game.split(" ")
            line_impossible = False

            for cubeset in cubes.replace(";", ",").split(", "):
                if is_impossible(cubeset):
                    line_impossible = True
                    break
            if not line_impossible:
                numbers_to_add.append(int(game_ID))
        result = sum(number for number in numbers_to_add)
    return result


def solve_part2(input_data):
    numbers_to_add = []
    with open(input_data) as file:
        for line in file:
            _, cubes = line.rstrip().split(": ")
            amount_of_cubes = check_max_amount_of_cubes(cubes)
            cube = calculate_cube_of_cubes(amount_of_cubes=amount_of_cubes)
            numbers_to_add.append(cube)
        result = sum(number for number in numbers_to_add)
    return result


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
