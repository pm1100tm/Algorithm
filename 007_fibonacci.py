"""
피보나치 수열 구하기
피보나치 수열이란, 첫 번째 항의 값이 0이고 두 번째 항의 값이 1일 때,
이후의 항들은 이전의 두 항을 더한 값으로 이루어지는 수열을 말한다.
예) 0, 1, 1, 2, 3, 5, 8, 13
인풋을 정수 n으로 받았을때, n 이하까지의 피보나치 수열을 출력하는 프로그램을 작성하세요
"""

n = 100 # 입력 받은 정수의 값
def fibo(n):
    fibo_list = [0, 1]
    index = 0
    while fibo_list[index] + fibo_list[index + 1] < n:
        fibo_list.append(fibo_list[index] + fibo_list[index + 1])
        index += 1
    print(", ".join(list(map(str, fibo_list))))

fibo(n) # 입력 값 100에 대한 결과 값: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89


# 재귀 함수
a = 100 # 입력 받은 정수의 값
def fibo(a):
    if a <= 0:
        return 0
    if a <= 1:
        return 1
    return fibo(a-2) + fibo(a-1)

for i in range(a):
    r = fibo(i)
    if r > a:
        break
    print(str(fibo(i)), end=", ")