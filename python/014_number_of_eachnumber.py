"""
1~1000에서 각 숫자의 개수 구하기
10 = 1, 0
11 = 1, 1
12 = 1, 2
13 = 1, 3
14 = 1, 4
15 = 1, 5

그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개
"""

""" #1 """
dic = dict.fromkeys([i for i in range(10)], 0)

for i in range(1, 1001):
    for j in range(10):
        if str(i).find(str(j)) != -1:
            dic[j] += str(i).count(str(j))

for keys, values in dic.items():
    print("{0}은 {1}개" .format(keys, values), end=" ")
    print()

# 0은 192개
# 1은 301개
# 2은 300개
# 3은 300개
# 4은 300개
# 5은 300개
# 6은 300개
# 7은 300개
# 8은 300개
# 9은 300개


""" #2 """
dic = dict.fromkeys([i for i in range(10)], 0)

for i in range(1, 1001):
    for j in str(i):
        dic[int(j)] += 1

for keys, values in dic.items():
    print("{0}은 {1}개" .format(keys, values), end=" ")
    print()