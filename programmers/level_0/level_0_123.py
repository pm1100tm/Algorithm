"""
1로 만들기

정수가 있을 때, 짝수라면 반으로 나누고,
홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다.
예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.

10 / 2 = 5
(5 - 1) / 2 = 4
4 / 2 = 2
2 / 2 = 1
위와 같이 4번의 나누기 연산으로 1이 되었습니다.

정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서
필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.

3 ≤ num_list의 길이 ≤ 15
1 ≤ num_list의 원소 ≤ 30

[12, 4, 15, 1, 14]	11
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(num_list):
    op_count = 0

    for n in num_list:
        while n > 1:
            if n % 2 == 0:
                n = n // 2

            else:
                n = (n - 1) // 2

            op_count += 1

    return op_count


@prvalue(print_result=True)
def solution001(num_list):
    """
    O(nlogn)을 O(n)으로 줄일 수 있네요!

    예를 들어 i=12 일때, bin(i) 를 하면 '0b1100' 이 됩니다.
    여기서 우리는 마지막으로 남겨야 하는 1; 즉 2^0인 맨끝의 '0'과 과 이진수를 나타내는 앞의 '0b'
    총 길이 3을 제외한 나머지 숫자들인 "110" 을 없애는 것이 목표값이 되는데,
    이는 각 자리마다 2를 나누는 횟수기 때문에 "110"의 길이인 3이 됩니다.
    홀 수 일 때는 어차피 -1을 해서 짝수로 만들기 때문에 가능합니다.

    len(bin(i)) - 3을 통해 '0b'의 길이 2와 마지막 비트(1)의 길이 1을 뺍니다.
    이는 정수 i를 1로 만드는데 필요한 연산 횟수와 일치합니다.
    예를 들어, 10은 이진수로 1010이고, 3번의 연산이 필요합니다 (첫 번째 '1'은 무시됩니다).
    """
    return sum(len(bin(i)) - 3 for i in num_list)


def t():
    print(bin(1000))
    print(bin(1))


if __name__ == '__main__':
    solution([12, 4, 15, 1, 14])
    t()
