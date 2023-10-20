"""
1부터 6까지 숫자가 적힌 주사위가 네 개 있습니다. 네 주사위를 굴렸을 때 나온 숫자에 따라 다음과 같은
점수를 얻습니다.

네 주사위에서 나온 숫자가 모두 p로 같다면 1111 × p점을 얻습니다.
- 세 주사위에서 나온 숫자가 p로 같고 나머지 다른 주사위에서 나온 숫자가 q(p ≠ q)라면 (10 × p + q)2 점
- 주사위가 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|점
- 어느 두 주사위에서 나온 숫자가 p로 같고 나머지 두 주사위에서 나온 숫자가 각각 p와 다른 q, r(q ≠ r)
  이라면 q × r점
- 네 주사위에 적힌 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자 만큼의 점수

네 주사위를 굴렸을 때 나온 숫자가 정수 매개변수 a, b, c, d로 주어질 때, 얻는 점수를 return 하는
solution 함수를 작성해 주세요.
"""
from utils import prvalue
from collections import Counter


@prvalue(print_result=False)
def solution(a, b, c, d):
    count_result = dict(Counter([a,b,c,d]))
    sorted_result = sorted(count_result.items(), key=lambda item: item[1], reverse=True)
    count1 = sorted_result[0][1]
    if count1 == 4:
        return 1111 * sorted_result[0][0]
    if count1 == 3:
        return pow(10 * sorted_result[0][0] + sorted_result[1][0], 2)
    count2 = sorted_result[1][1]
    if count1 == 2 and count2 == 2:
        x = sorted_result[0][0] + sorted_result[1][0]
        y = abs(sorted_result[0][0] - sorted_result[1][0])
        return x * y
    if count1 == 2 and count2 == 1:
        x, y = sorted_result[1][0], sorted_result[2][0]
        return x * y
    return sorted(count_result.items(), key=lambda item: item[0])[0][0]


if __name__ == '__main__':
    assert solution(2,2,2,2) == 2222
    assert solution(4,1,4,4) == 1681
    assert solution(6,3,3,6) == 27
    assert solution(2,5,2,6) == 30
    assert solution(6,4,2,5) == 2
