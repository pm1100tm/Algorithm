"""가장 많이 받은 선물
https://school.programmers.co.kr/learn/courses/30/lessons/258712
"""
from collections import defaultdict
from utils import prvalue


@prvalue(print_result=True)
def solution(friends: list[str], gifts: list[str]) -> int:
    give_count = defaultdict(int)
    gave_count = defaultdict(int)
    exchange_count = defaultdict(lambda: defaultdict(int))
    gift_rate = defaultdict(int)

    for f in friends:
        exchange_count[f] = defaultdict(int)
        give_count[f] = 0
        gave_count[f] = 0

    for gift in gifts:
        give, gave = gift.split()
        give_count[give] += 1
        gave_count[gave] += 1
        exchange_count[give][gave] += 1

    for f in friends:
        gift_rate[f] = give_count[f] - gave_count[f]

    next_month_gifts = defaultdict(int)
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            give = friends[i]
            gave = friends[j]

            count_a = exchange_count.get(give).get(gave, 0)
            count_b = exchange_count.get(gave).get(give, 0)

            if (count_a == 0 and count_b == 0) or (count_a == count_b):
                if gift_rate[give] > gift_rate[gave]:
                    next_month_gifts[give] += 1
                elif gift_rate[give] < gift_rate[gave]:
                    next_month_gifts[gave] += 1
                else:
                    continue

            if count_a > count_b:
                next_month_gifts[give] += 1

            elif count_a < count_b:
                next_month_gifts[gave] += 1

    return max(next_month_gifts.values(), default=0)


if __name__ == '__main__':
    assert solution(
        ["muzi", "ryan", "frodo", "neo"],
        ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi",
         "frodo muzi", "frodo ryan", "neo muzi"],
    ) == 2
    assert solution(
        ["joy", "brad", "alessandro", "conan", "david"],
        ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro",
         "alessandro david"],
    ) == 4
    assert solution(
        ["a", "b", "c"],
        ["a b", "b a", "c a", "a c", "a c", "c a"],
    ) == 0
