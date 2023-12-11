from dataclasses import dataclass
from functools import reduce

puzzle_input = "input6.txt"

@dataclass
class Race:
    time: int
    distance: int


def read_input(input_data) -> list[tuple[int]]:
    with open(input_data) as file:
        for line in file:
            if "Time" in line:
                times = [int(n) for n in line.removeprefix("Time:").strip().split()]
            if "Distance" in line:
                distances = [int(n) for n in line.removeprefix("Distance:").strip().split()]
        return list(zip(times, distances))


def calc_distance(time:int, push_time: int) -> int:
    race_time = time - push_time
    speed = push_time
    race_distance = race_time * speed
    return race_distance


def is_win(winning_distance: int, race_distance: int) -> bool:
    return True if race_distance > winning_distance else False


def solve_part1(input_data):
    wins = []
    races = read_input(input_data)
    for time, distance in races:
        win_options = 0
        for n in range(time + 1):
            if is_win(winning_distance=distance,
                      race_distance=calc_distance(time=time, push_time=n)):
                win_options += 1
        wins.append(win_options)
    result = reduce(lambda x, y: x * y,  wins)
    return result


race = (58819676, 434104122191218)


def solve_part2(race: tuple[int, int]) -> int:
    time, distance = race
    win_options = 0
    for n in range(time + 1):
        if is_win(winning_distance=distance,
                  race_distance=calc_distance(time=time, push_time=n)):
            win_options += 1
    return win_options


def generate_solution(puzzle):
    solution1 = solve_part1(puzzle)
    solution2 = solve_part2(race)
    print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
