"""비밀지도
https://school.programmers.co.kr/learn/courses/30/lessons/17681
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(n: int, arr1: list[int], arr2: list[int]) -> list[str]:
    answer = []

    for i in range(len(arr1)):
        a1 = bin(arr1[i]).replace('0b', '').zfill(n)
        a2 = bin(arr2[i]).replace('0b', '').zfill(n)

        temp = ''
        for j in range(len(a1)):
            if a1[j] == '1' or a2[j] == '1':
                temp += '#'
            else:
                temp += ' '

        answer.append(temp)

    return answer


@prvalue(print_result=True)
def solution2(n: int, arr1: list[int], arr2: list[int]) -> list[str]:
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)

    return answer


if __name__ == '__main__':
    assert (
        solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
        == ['#####', '# # #', '### #', '#  ##', '#####']
    )
    assert (
        solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
        == ['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']
    )
    assert (
        solution2(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
        == ['#####', '# # #', '### #', '#  ##', '#####']
    )
    assert (
        solution2(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])
        == ['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']
    )
