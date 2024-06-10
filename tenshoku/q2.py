from dataclasses import dataclass

from collections import Counter


@dataclass
class Results:
    set_name: str
    selected_cards: "array"


def solution(cards):
    # TODO: 미완성
    rank_map = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14,
    }
    suit_map = {
        'S': 1,
        'H': 2,
        'D': 3,
        'C': 4,
    }

    # 정렬 선행
    sorted_cards = sorted(
        cards,
        key=lambda x: (rank_map[x[:-1]], suit_map[x[-1]]),
        reverse=True,
    )

    rank_list = []
    suit_list = []
    for c in sorted_cards:
        rank_list.append(c[:-1])
        suit_list.append(c[-1])

    set_name = ''
    selected_cards = []

    consecutive_count = 0
    for i in range(len(set(rank_list)) - 5):
        for j in range(i + 1, len(rank_list)):
            if abs(rank_map[rank_list[i]] - rank_map[rank_list[j]]) == 1:
                consecutive_count += 1
                if consecutive_count == 5:
                    set_name = 'five in row'

    count_result = Counter(rank_list).most_common()
    print(count_result)
    if count_result[0][1] == 1:
        set_name = 'single card'
        selected_cards.append(sorted_cards[0])

    elif count_result[0][1] == 2:
        set_name = 'pair'
        selected_cards = [c for c in sorted_cards if c[:-1] == count_result[0][0]]

    elif count_result[0][1] >= 3 and count_result[1][1] < 2:
        set_name = 'triple'
        selected_cards = [c for c in sorted_cards if c[:-1] == count_result[0][0]][:3]

    return Results(set_name=set_name, selected_cards=selected_cards)


if __name__ == '__main__':
    # print(solution(['2H', '4H', '7C', '9D', '10D', 'KS']))
    # print(solution(['AS', '10H', '8H', '10S', '8D']))
    # print(solution(['AS', 'JS', 'AH', 'AD', '10D', 'AC']))
    print(solution(['6H', '7S', '8S', '9S', '10S', 'JD', 'JC', 'KC', 'AC']))
