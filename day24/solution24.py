from shapely import LineString, Point

puzzle_input = "input24.txt"


MIN = 7
MAX = 27


def get_hailstones(input_file) -> list[Point]:
    flying_stones = []
    with open (input_file, "r") as file:
        for line in file:
            point_str, velocity_str = line.rstrip().split(" @ ")
            point_a = [int(val) for val in point_str.split(",")]
            velocity = [int(val) for val in velocity_str.split(",")]
            point_b = [p + v for p, v in zip(point_a, velocity)]
            hailstone_point_a = Point(*point_a)
            hailstone_point_b = Point(*point_b)
            flying_hailstone = LineString([hailstone_point_a, hailstone_point_b])
            flying_stones.append(flying_hailstone)
    return flying_stones


def solve_part1(input_data) -> int:
    pass


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
