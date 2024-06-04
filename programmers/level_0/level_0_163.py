"""
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 다항식을 계산할 때는 동류항끼리 계산해
정리합니다. 덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 동류항끼리 더한 결괏값을
문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

제한사항
- 0 < polynomial에 있는 수 < 100
- polynomial에 변수는 'x'만 존재합니다.
- polynomial은 양의 정수, 공백, ‘x’, ‘+'로 이루어져 있습니다.
- 항과 연산기호 사이에는 항상 공백이 존재합니다.
- 공백은 연속되지 않으며 시작이나 끝에는 공백이 없습니다.
- 하나의 항에서 변수가 숫자 앞에 오는 경우는 없습니다.
- " + 3xx + + x7 + "와 같은 잘못된 입력은 주어지지 않습니다.
- 0으로 시작하는 수는 없습니다.
- 결괏값에 상수항은 마지막에 둡니다.
"""
from utils import prvalue


@prvalue(print_result=False)
def solution(polynomial):
    x_ele, n_ele = 0, 0
    for ele in polynomial.split(' '):
        if ele.endswith('x'):
            value = ele[:-1]
            x_ele += int(value) if len(value) else 1
        else:
            if ele.isdigit():
                n_ele += int(ele)

    if x_ele and not n_ele:
        return f"{'' if x_ele == 1 else x_ele}x"
    if not x_ele and n_ele:
        return f"{n_ele}"

    return f"{'' if x_ele == 1 else x_ele}x + {n_ele}"


def solution2(polynomial: str):
    x_total, const_total = 0, 0
    for term in polynomial.split(' + '):
        if term.isdigit():
            const_total += int(term)
        else:
            x_total += 1 if term == 'x' else int(term[:-1])

    result = []
    if x_total:
        result.append(f"{'' if x_total == 1 else x_total}x")
    if const_total:
        result.append(f"{const_total}")

    return ' + '.join(result)


if __name__ == '__main__':
    assert solution2("3x + 7 + x") == "4x + 7"
    assert solution2("x + x + x") == '3x'
    assert solution2("1 + 3 + 4") == '8'
    assert solution2("11x + 22x + 33x") == "66x"
    assert solution2("x + 1") == "x + 1"
