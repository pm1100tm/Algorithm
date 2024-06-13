"""3진법 뒤집기
자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를
return 하도록 solution 함수를 완성해주세요.

제한 사항
- n은 1 이상 100,000,000 이하인 자연수입니다.

n (10진법)   n (3진법)    앞뒤 반전(3진법)  10진법으로 표현
45          1200        0021            7
125         11122       22111           229
"""


def solution(n: int) -> int:
    ternary = ''
    number = n
    while number:
        n, r = divmod(number, 3)
        ternary += str(r)
        number = n

    result = int(ternary, 3)

    return result


def solution2(n: int) -> int:
    ternary = ''
    number = n
    while number > 0:
        quoitent, reminder = divmod(number, 3)
        ternary += str(reminder)
        number = quoitent

    result = 0
    for i, num_str in enumerate(ternary[::-1]):
        result += int(num_str) * (3 ** i)

    return result


if __name__ == '__main__':
    assert solution(45) == 7
    assert solution(125) == 229
    assert solution2(45) == 7
    assert solution2(125) == 229
