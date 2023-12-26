puzzle_input = "input25.txt"
import networkx as nx

def read_input(input_data) -> :
    steps = []
    with open(input_data, "r") as file:

    return steps





def solve_part1(input_data) -> int:
    G = nx.Graph()



def solve_part2(input_data) -> int:
    pass


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    # solution2 = solve_part2(puzzle)
    print(f"\n\nsolution part 1 : {solution1}")
    # print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
