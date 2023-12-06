puzzle_input = "input4.txt"


def solve_part1(input_data):
    numbers_to_add = []
    with open(input_data) as file:
        for line in file:
            _, numbers = line.rstrip().split(": ")
            winning_numbers, my_numbers = numbers.replace("  ", " ").split(
                " | "
            )
            winning_set = set(winning_numbers.split(" "))
            my_set = set(my_numbers.split(" "))
            my_wins = winning_set.intersection(my_set)
            amount_of_wins = len(my_wins)
            if amount_of_wins == 0:
                numbers_to_add.append(0)
            else:
                numbers_to_add.append(2 ** (amount_of_wins - 1))
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
