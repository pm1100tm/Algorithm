"""영어 끝말잇기
https://school.programmers.co.kr/learn/courses/30/lessons/12981
- idea
defaultdict, hash
"""
from utils import prvalue

from collections import defaultdict


@prvalue(print_result=True)
def solution(n: int, words: list[str]) -> list[int]:
    answer = [0, 0]
    participants, words_comes_out = defaultdict(int), defaultdict(int)
    prev_word = ''

    for i in range(1, n + 1):
        participants[i] = 0

    for i, next_word in enumerate(words):
        participants_num = (i % n) + 1
        participants[participants_num] += 1

        if not prev_word:
            prev_word = next_word
            words_comes_out[next_word] += 1
            continue

        if (
            len(next_word) < 2
            or prev_word[-1] != next_word[0]
            or words_comes_out[next_word] > 0
        ):
            answer[0] = participants_num
            answer[1] = participants[participants_num]
            break

        words_comes_out[next_word] += 1
        prev_word = next_word

    return answer


if __name__ == '__main__':
    assert (
        solution(
            3,
            ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot",
             "tank"],
        ) == [3, 3]
    ), 'fail'
    assert (
        solution(
            5,
            [
                "hello", "observe", "effect", "take", "either", "recognize", "encourage",
                "ensure", "establish", "hang", "gather", "refer", "reference", "estimate",
                "executive",
            ]
        )
        == [3, 3]
    ), 'fail'
    assert (
        solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])
        == [3, 3]
    ), 'fail'
