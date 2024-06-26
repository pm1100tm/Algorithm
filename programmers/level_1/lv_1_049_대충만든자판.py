"""대충만든자판
https://school.programmers.co.kr/learn/courses/30/lessons/160586

알고리즘, 자료구조: hash, iterate

각 문자를 눌러야 하는 최소 카운트를 캐시에 저장한다.
최소 값을 찾지 못했다면 -1를 결과에 저장하고, 찾았다면 최소 카운트 수를 저장한다.
"""


def solution(keymap: list[str], targets: list[str]) -> list[int]:
    answer = []
    cache = {}

    for target in targets:
        i = 0
        count = 0
        not_found = False

        while i < len(target):
            char = target[i]
            cache_count = cache.get(char)
            if cache_count:
                count += cache_count
                i += 1
                continue

            index_map = [keys.find(char) for keys in keymap if keys.find(char) != -1]
            if not index_map:
                not_found = True
                break

            min_click_count = min(index_map) + 1
            cache[char] = min_click_count
            count += min_click_count
            i += 1

        if not_found:
            answer.append(-1)
        else:
            answer.append(count)

    return answer


def solution2(keymap: list[str], targets: list[str]) -> list[int]:
    char_to_press = {}
    for keys in keymap:
        for i, char in enumerate(keys, 1):
            if char not in char_to_press:
                char_to_press[char] = i
            else:
                char_to_press[char] = min(char_to_press[char], i)

    answer = []
    for target in targets:
        total_press_count = 0
        for char in target:
            if char not in char_to_press:
                total_press_count = -1
                break

            total_press_count += char_to_press[char]

        answer.append(total_press_count)

    return answer


if __name__ == '__main__':
    assert solution(["ABACD", "BCEFD"], ["ABCD","AABB"]) == [9, 4]
    assert solution(["AA"], ['B']) == [-1]
    assert solution(["AGZ", "BSSS"], ["ASA","BGZ"]) == [4, 6]
    assert solution(["ABACD", "BCEFD"],  ["ABCD", "DG", "AABB"]) == [9, -1, 4]

    assert solution2(["ABACD", "BCEFD"], ["ABCD","AABB"]) == [9, 4]
    assert solution2(["AA"], ['B']) == [-1]
    assert solution2(["AGZ", "BSSS"], ["ASA","BGZ"]) == [4, 6]
    assert solution2(["ABACD", "BCEFD"],  ["ABCD", "DG", "AABB"]) == [9, -1, 4]
