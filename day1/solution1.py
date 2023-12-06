from collections import namedtuple

puzzle_input = "input1.txt"


# query from the left side: found something: remember + stop
# query from the' right side: found something: remember + stop
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


# find first in list/set of words, save index of first letter and the string
# same for digit
# compare & take the lowest index

# reverse: strings in reverse


def solve_part2(input_data):
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
    DigitInfo = namedtuple("DigitInfo", ["index", "value"])
    numbers_to_add = []

    with open(input_data, "r") as file:
        for line in file:
            # numeral
            front_index_numeral, front_digit_numeral = next(
                ((i, char) for i, char in enumerate(line) if char.isdigit()),
                (None, None),
            )
            # strings
            # find the index of the first sting
            indices = [line.find(d.name) for d in DIGITS if
                       line.find(d.name) != -1]
            front_index_string = min(indices) if indices else None

            # we need to take the one with the smallest index
            if front_index_string < front_index_numeral:
                digit1 = next((d.value for d in DIGITS
                               if line.find(d.name, front_index_string),
                              None)
            else:
                digit1 = front_digit_numeral

            numbers_to_add.append(int(digit1))

            back_candidates = []
            digit2 = next(
                (
                    (i, char)
                    for i, char in enumerate(reversed(line))
                    if char.isdigit()
                ),
                (None, None),
            )
            number_str = digit1 + digit2
            numbers_to_add.append(int(number_str))
        solution = sum(numbers_to_add)
    return solution


def generate_solution(puzzle):
    solution = solve_part1(puzzle)
    print(f"\n\n{solution=}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
