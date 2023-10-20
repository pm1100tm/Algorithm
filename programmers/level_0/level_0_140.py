"""
qr code

두 정수 q, r과 문자열 code가 주어질 때,
code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자를
앞에서부터 순서대로 이어 붙인 문자열을 return 하는 solution 함수를 작성해 주세요.

0 ≤ r < q ≤ 20
r < code의 길이 ≤ 1,000
code는 영소문자로만 이루어져 있습니다.

q	r	code	result
3	1	"qjnwezgrpirldywt"	"jerry"
1	0	"programmers"	"programmers"
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(q, r, code):
    the_first_index: int = 0
    for i, _ in enumerate(code):
        if i % q == r:
            the_first_index = i
            break

    answer = ""
    for i in range(the_first_index, len(code), q):
        answer += code[i]

    return answer


@prvalue(print_result=True)
def solution001(q, r, code):
    return code[r::q]


if __name__ == '__main__':
    assert solution(3,	1, "qjnwezgrpirldywt") == "jerry"
    assert solution(1,	0, "programmers") == "programmers"
    assert solution001(3, 1, "qjnwezgrpirldywt") == "jerry"
    assert solution001(1, 0, "programmers") == "programmers"
