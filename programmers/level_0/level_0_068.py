"""
할 일 목록

오늘 해야 할 일이 담긴 문자열 배열 todo_list와
각각의 일을 지금 마쳤는지를 나타내는 boolean 배열 finished가 매개변수로 주어질 때,
todo_list에서 아직 마치지 못한 일들을 순서대로 담은 문자열 배열을 return 하는 solution 함수를 작성해 주세요.

1 ≤ todo_list의 길이 1 ≤ 100
2 ≤ todo_list의 원소의 길이 ≤ 20
todo_list의 원소는 영소문자로만 이루어져 있습니다.
todo_list의 원소는 모두 서로 다릅니다.
finished[i]는 true 또는 false이고 true는 todo_list[i]를 마쳤음을, false는 아직 마치지 못했음을 나타냅니다.
아직 마치지 못한 일이 적어도 하나 있습니다.
"""
from utils import prvalue


@prvalue(print_time=True)
def solution(todo_list: list[str], finished: list[bool]) -> list[str]:
    return [x for x, y in zip(todo_list, finished) if not y]


@prvalue(print_time=True)
def solution001(todo_list: list[str], finished: list[bool]) -> list[str]:
    return [todo for index, todo in enumerate(todo_list) if not finished[index]]


if __name__ == '__main__':
    assert solution(
        ["problemsolving", "practiceguitar", "swim", "studygraph"]
        , [True, False, True, False]
    ) == ["practiceguitar", "studygraph"]

    assert solution001(
        ["problemsolving", "practiceguitar", "swim", "studygraph"]
        , [True, False, True, False]
    ) == ["practiceguitar", "studygraph"]
    # 편리한 것은 zip 함수, 빠르기는 리스트 컴프리헨션이 빠르다.
