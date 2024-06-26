"""하샤드 수
양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다.
자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution 을 완성해주세요.

입출력 예
 arr return
 10  true
 12  true
 11  false
 13  false
"""


def solution(x: int) -> bool:
    sum_of_x = sum([int(a) for a in str(x)])

    return (x % sum_of_x) == 0


if __name__ == '__main__':
    assert solution(10) is True
    assert solution(12) is True
    assert solution(11) is False
    assert solution(13) is False
