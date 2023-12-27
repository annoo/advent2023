from collections import namedtuple

puzzle_input = "input1.txt"


Stringified = namedtuple("StringDigit", ["name", "value"])
DIGITS = [
    Stringified("one", 1),
    Stringified("two", 2),
    Stringified("three", 3),
    Stringified("four", 4),
    Stringified("five", 5),
    Stringified("six", 6),
    Stringified("seven", 7),
    Stringified("eight", 8),
    Stringified("nine", 9)
]


def find_first_number(string: str, digits: list) -> int:
    lowest_index = float("inf")
    found_digit = None

    digit1 = next((char for char in string if char.isdigit()), None)
    if digit1:
        lowest_index = string.index(digit1)
        found_digit = int(digit1)

    for digit in digits:
        if digit.name in string:
            index_of_str_digit1 = string.index(digit.name)
            if index_of_str_digit1 < lowest_index:
                lowest_index = index_of_str_digit1
                found_digit = digit.value

    return found_digit


def find_last_number(string: str, digits: list) -> int:
    string_reversed = string[::-1]
    digits_reversed = [Stringified(digit.name[::-1], digit.value) for digit in digits]
    digit2 = find_first_number(string_reversed, digits_reversed)
    return digit2


def solve_part1(input_data):
    numbers_to_add = []
    with open(input_data, "r") as file:
        for line in file:
            digit1 = next((char for char in line if char.isdigit()), None)
            digit2 = next(
                (char for char in reversed(line) if char.isdigit()), None
            )
            number_str = digit1 + digit2
            numbers_to_add.append(int(number_str))
        solution = sum(numbers_to_add)
    return solution


def solve_part2(input_data):
    numbers_to_add = []

    with open(input_data, "r") as file:
        for line in file:
            digit1 = find_first_number(line.rstrip(), DIGITS)
            digit2 = find_last_number(line.strip(), DIGITS)
            number = digit1 * 10 + digit2
            numbers_to_add.append(number)
    return sum(numbers_to_add)


def generate_solution(puzzle):
    solution = solve_part2(puzzle)
    print(f"\n\n{solution=}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
