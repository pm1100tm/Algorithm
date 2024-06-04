"""
PROGRAMMERS-962 행성에 불시착한 우주비행사 머쓱이는 외계행성의 언어를 공부하려고 합니다. 알파벳이 담긴
배열 spell과 외계어 사전 dic이 매개변수로 주어집니다. spell에 담긴 알파벳을 한번씩만 모두 사용한 단어가
dic에 존재한다면 1, 존재하지 않는다면 2를 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(spell, dic):
    def sorted_str(string):
        return ''.join(sorted(string))

    answer = 2
    sorted_spell = sorted_str(spell)
    for d in dic:
        if sorted_spell in sorted_str(d):
            answer = 1
            break

    return answer


def solution2(spell, dic):
    new_spell = set(spell)
    for s in dic:
        if not new_spell - set(s):
            return 1

    return 2


if __name__ == '__main__':
    solution2(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])
    solution2(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"])
    solution2(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"])
