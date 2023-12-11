from collections import Counter
from dataclasses import dataclass
from enum import Enum
from operator import itemgetter

puzzle_input = "input7.txt"

CARD_ORDER = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8,
              "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

JOKER_ORDER = {"A": 13, "K": 12, "Q": 11, "T": 10, "9": 9, "8": 8,
               "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}


class Rank(Enum):
    FIVE_OF_A_KIND = 1
    FOUR_OF_A_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_A_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7


@dataclass(frozen=True)
class Hand:
    hand: str
    type: Rank


def get_hand_rank(hand_bit_pair: tuple[Hand, int]) -> int:
    hand, _ = hand_bit_pair
    return hand.type.value


def make_joker_combinations(hand: str) -> list[str]:
    unique_cards = set(hand) - {"J"}
    joker_combinations = [hand.replace("J", card) for card in unique_cards]
    if not joker_combinations:
        return ["AAAAA"]
    return joker_combinations


def joker_ranks(hand: str) -> Rank:
    joker_combinations = make_joker_combinations(hand)
    ranks = map(detect_rank, joker_combinations)
    return min(ranks, key=lambda rank: rank.value)


def read_input(input_data) -> dict[Hand, int]:
    all_games = {}
    with open(input_data) as file:
        for line in file:
            hand, bid = line.rstrip().split(" ")
            if "J" not in hand:
                rank = detect_rank(hand)
            else:
                rank = joker_ranks(hand)
            hand = Hand(hand=hand, type=rank)
            all_games[hand] = int(bid)
    return all_games


def detect_rank(hand: str) -> Rank:
    c = Counter(hand)
    most_common_cards = c.most_common(1)[0][1]
    if most_common_cards == 5:
        rank = Rank.FIVE_OF_A_KIND
    elif most_common_cards == 4:
        rank = Rank.FOUR_OF_A_KIND
    elif most_common_cards == 3:
        if c.most_common(2)[1][1] == 2:
            rank = Rank.FULL_HOUSE
        else:
            rank = Rank.THREE_OF_A_KIND
    elif most_common_cards == 2:
        if c.most_common(2)[1][1] == 2:
            rank = Rank.TWO_PAIR
        else:
            rank = Rank.ONE_PAIR
    else:
        rank = Rank.HIGH_CARD
    return rank


def make_value_tuple_of_hand(hand: Hand) -> tuple:
    number_hand = ()
    for letter in hand.hand:
        number_hand += (CARD_ORDER[letter],)
    return number_hand


def make_value_tuple_of_hand_joker(hand: Hand) -> tuple:
    number_hand = ()
    for letter in hand.hand:
        number_hand += (JOKER_ORDER[letter],)
    return number_hand


def sort_the_games(
        games: dict[Hand, int]) -> list[tuple, int]:

    games_sorted = sorted(games.items(), key=get_hand_rank)
    games_sorted.reverse()

    sections_per_type = [[] for _ in range(7)]

    for hand, bid in games_sorted:
        rank = hand.type.value
        number_hand = make_value_tuple_of_hand_joker(hand)
        if 1 <= rank <= 7:
            sections_per_type[rank-1].append((number_hand, bid))

    for section in sections_per_type:
        section.sort()
        section.reverse()

    ranked_games = sum(sections_per_type, [])  # flatten list
    ranked_games.reverse()
    return ranked_games


def make_ordered_bidlist(ranked_games: list[tuple]) -> list[int]:
    get_second_item = itemgetter(1)
    return [0] + list(map(get_second_item, ranked_games))


def calc_total_winnings(bids: list[int]) -> int:
    winnings = 0
    for i, bid in enumerate(bids):
        winnings += i * bid
    return winnings


def solve_part1(input_data):
    all_games = read_input(input_data)
    ranked = sort_the_games(all_games)
    bids = make_ordered_bidlist(ranked)
    return calc_total_winnings(bids)


def solve_part2(input_data) -> int:
    all_games = read_input(input_data)
    ranked = sort_the_games(all_games)
    bids = make_ordered_bidlist(ranked)
    return calc_total_winnings(bids)


def generate_solution(puzzle):
    # solution1 = solve_part1(puzzle)
    solution2 = solve_part2(puzzle)
    # print(f"\n\nsolution part 1 : {solution1}")
    print(f"\nsolution part 2 : {solution2}")


if __name__ == "__main__":
    _input = puzzle_input
    generate_solution(_input)
