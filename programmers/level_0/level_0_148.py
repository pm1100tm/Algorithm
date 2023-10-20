"""
덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다.
수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(quiz):
    answer = []
    for expression in quiz:
        expression: str
        v = expression.replace(' ', '').split('=')
        if str(eval(v[0])) == v[1]:
            answer.append('O')
        else:
            answer.append('X')

    return answer


if __name__ == '__main__':
    assert solution(["3 - 4 = -3", "5 + 6 = 11"]) == ['X', 'O']
    assert (
        solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"])
        == ['O', 'O', 'X', 'O']
    )

