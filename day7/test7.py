import pytest
from solution7 import (
    Hand,
    Rank,
    calc_total_winnings,
    detect_rank,
    make_joker_combinations,
    make_ordered_bidlist,
    make_value_tuple_of_hand,
    read_input,
    solve_part1,
    solve_part2,
    sort_the_games,
)

# def test_reads_input():
#     expected_games = {
#     Hand(hand="32T3K"): 765,
#     Hand(hand="T55J5"): 684,
#     Hand(hand="KK677"): 28,
#     Hand(hand="KTJJT"): 220,
#     Hand(hand="QQQJA"): 483
#     }
#
#     assert read_input("test_input7.txt") == expected_games


# def test_reads_input_part1():
#     expected_games = {
#     Hand(hand="32T3K", type=Rank.ONE_PAIR): 765,
#     Hand(hand="T55J5", type=Rank.THREE_OF_A_KIND): 684,
#     Hand(hand="KK677", type=Rank.TWO_PAIR): 28,
#     Hand(hand="KTJJT", type=Rank.TWO_PAIR): 220,
#     Hand(hand="QQQJA", type=Rank.THREE_OF_A_KIND): 483
#     }
#
#     assert read_input("test_input7.txt") == expected_games


def test_reads_input_joker():
    expected_games = {
    Hand(hand="32T3K", type=Rank.ONE_PAIR): 765,
    Hand(hand="T55J5", type=Rank.FOUR_OF_A_KIND): 684,
    Hand(hand="KK677", type=Rank.TWO_PAIR): 28,
    Hand(hand="KTJJT", type=Rank.FOUR_OF_A_KIND): 220,
    Hand(hand="QQQJA", type=Rank.FOUR_OF_A_KIND): 483
    }

    assert read_input("test_input7.txt") == expected_games

@pytest.mark.parametrize(
    "hand, expected_tuple",
    [
        (Hand(hand="32T3K", type=Rank.ONE_PAIR), (3, 2, 10, 3, 13)),
        (Hand(hand="T55J5", type=Rank.THREE_OF_A_KIND), (10, 5, 5, 11, 5)),
    ])
def test_hand_string_transforms_to_tuple_in_dict_item(hand, expected_tuple):
    assert make_value_tuple_of_hand(hand) == expected_tuple


def test_sort_games():
    unordered_games = {
    Hand(hand="32T3K", type=Rank.ONE_PAIR): 765,
    Hand(hand="T55J5", type=Rank.THREE_OF_A_KIND): 684,
    Hand(hand="KK677", type=Rank.TWO_PAIR): 28,
    Hand(hand="KTJJT", type=Rank.TWO_PAIR): 220,
    Hand(hand="QQQJA", type=Rank.THREE_OF_A_KIND): 483
    }
    expected_flat = [((3, 2, 10, 3, 13), 765),
                     ((13, 10, 11, 11, 10), 220),
                     ((13, 13, 6, 7, 7), 28),
                     ((10, 5, 5, 11, 5), 684),
                     ((12, 12, 12, 11, 14), 483)]

    assert sort_the_games(unordered_games) == expected_flat


def test_list_of_bids_in_order():
    init_list = [((3, 2, 10, 3, 13), 765),
                 ((13, 10, 11, 11, 10), 220),
                 ((13, 13, 6, 7, 7), 28),
                 ((10, 5, 5, 11, 5), 684),
                 ((12, 12, 12, 11, 14), 483)]
    expected_bids_list = [0, 765, 220, 28, 684, 483]
    assert make_ordered_bidlist(init_list) == expected_bids_list


def test_calculate_winnings():
    bids = [0, 765, 220, 28, 684, 483]
    expected_winnings = 6440
    assert calc_total_winnings(bids) == expected_winnings


@pytest.mark.parametrize(
    "hand_str, expected_type",
    [
        ("32T3K", Rank.ONE_PAIR),
        ("T55J5", Rank.THREE_OF_A_KIND),
        ("KK677", Rank.TWO_PAIR),
        ("KTJJT", Rank.TWO_PAIR),
        ("QQQJA", Rank.THREE_OF_A_KIND),
    ],
)
def test_recognize_type_of_hands(hand_str, expected_type):
    assert detect_rank(hand_str) == expected_type


def test_joker_combinations():
    hand = "JKA23"
    expected_combinations = {"KKA23", "AKA23", "2KA23", "3KA23"}
    actual_combinations = set(make_joker_combinations(hand))
    assert actual_combinations == expected_combinations

@pytest.mark.parametrize(
    "part, input_data, expected_output",
    [
        # (1, "test_input7.txt", 6440),
        (2, "test_input7.txt", 5905),
    ],
)
def test_solve(part, input_data, expected_output):
    if part == 1:
        result = solve_part1(input_data)
    else:
        result = solve_part2(input_data)
    print(f"\n\n{result=}")
    assert result == expected_output
