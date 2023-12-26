import networkx as nx

puzzle_input = "input25.txt"


def create_graph_from_input(input_data) -> nx.Graph:
    graph = nx.Graph()
    with open(input_data, "r") as file:
        for line in file:
            start, ends = line.rstrip().split(": ")
            ends = ends.split(" ")
            for end in ends:
                graph.add_edge(start, end)
    return graph




def solve_part1(input_data) -> int:
    graph = create_graph_from_input(input_data)
    cut_value, partition = nx.stoer_wagner(graph)
    if cut_value == 3:
        return len(partition[0]) * len(partition[1])
    else:
        return 1  # apply additional reasoning if NOK

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
