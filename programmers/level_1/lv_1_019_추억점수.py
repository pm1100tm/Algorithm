"""추억점수
사진별로 추억 점수를 매길려고 합니다. 사진 속에 나오는 인물의 그리움 점수를 모두 합산한 값이 해당 사진의
추억 점수가 됩니다. 예를 들어 사진 속 인물의 이름이 ["may", "kein", "kain"]이고 각 인물의 그리움
점수가 [5점, 10점, 1점]일 때 해당 사진의 추억 점수는 16(5 + 10 + 1)점이 됩니다.
그리워하는 사람의 이름을 담은 문자열 배열 name,
각 사람별 그리움 점수를 담은 정수 배열 yearning,
각 사진에 찍힌 인물의 이름을 담은 이차원 문자열 배열 photo가 매개변수로 주어질 때,
사진들의 추억 점수를 photo에 주어진 순서대로 배열에 담아 return하는 solution 함수를 완성해주세요.

제한사항
- 그리움 점수가 없는 경우도 있다.
- 3 ≤ name의 길이 = yearning의 길이≤ 100
- name에는 중복된 값이 들어가지 않습니다.
- yearning[i]는 i번째 사람의 그리움 점수입니다.
"""


def total_yearning_score(name_list: list[str], score_map: dict[str, int]) -> int:
    return sum([score_map.get(name, 0) for name in name_list])


def solution(name: list[str], yearning: list[int], photo: list[list[str]]) -> list[int]:
    score_map = {k:v for k, v in zip(name, yearning)}

    answer = []
    for name_list in photo:
        answer.append(total_yearning_score(name_list, score_map))

    return answer


if __name__ == '__main__':
    assert solution(
        ["may", "kein", "kain", "radi"],
        [5, 10, 1, 3],
        [
            ["may", "kein", "kain", "radi"],
            ["may", "kein", "brin", "deny"],
            ["kon", "kain", "may", "coni"],
        ],
    ) == [19, 15, 6]
    assert solution(
        ["kali", "mari", "don"],
        [11, 1, 55],
        [
            ["kali", "mari", "don"],
            ["pony", "tom", "teddy"],
            ["con", "mona", "don"],
        ],
    ) == [67, 0, 55]
    assert solution(
        ["may", "kein", "kain", "radi"],
        [5, 10, 1, 3],
        [
            ["may"],
            ["kein", "deny", "may"],
            ["kon", "coni"],
        ]
    ) == [5, 15, 0]
