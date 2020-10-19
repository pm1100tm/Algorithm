"""
10~1000까지 각 숫자 분해하여 곱하기의 전체 합 구하기

예로, 10~15까지의 각 숫자 분해하여 곱하기의 전체 합은 다음과 같다.
10 = 1 * 0 = 0
11 = 1 * 1 = 1
12 = 1 * 2 = 2
13 = 1 * 3 = 3
14 = 1 * 4 = 4
15 = 1 * 5 = 5
그러므로, 이 경우의 답은 0+1+2+3+4+5 = 15
"""
import functools

total = 0
count = 0
for i in range(10, 1001):
    if str(i).find("0") == -1:
        count += 1
        total += functools.reduce(lambda x, y: x * y, [int(i) for i in str(i)])

print(total) # 93150
print(count)

# 숫자를 문자열로 바꿔 0이 포함되어있나 체크한 후, reduce 메서드를 활용하여 각 자릿수의 곱하기 총합을 계산.
# if 문을 넣었을 경우 count 820, 넣었을 경우 991 이다.