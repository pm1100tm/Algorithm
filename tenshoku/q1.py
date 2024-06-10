def solution(A, B):
    def count_pieces(length, stick1, stick2):
        return (stick1 // length) + (stick2 // length)

    def can_form_square(length, stick1, stick2):
        return count_pieces(length, stick1, stick2) >= 4

    for length in range(max(A, B), 0, -1): # min을 max로 바꿔야 한다.
        if can_form_square(length, A, B):
            return length
    return 0


if __name__ == '__main__':
    case1 = [10, 21]
    case2 = [13, 11]
    case3 = [10, 30]
    case4 = [1, 1]
    case5 = [1, 8]

    ret = solution(case1[0], case1[1])
    print(ret)
    ret = solution(case2[0], case2[1])
    print(ret)
    ret = solution(case3[0], case3[1])
    print(ret)
    ret = solution(case4[0], case4[1])
    print(ret)
    ret = solution(case5[0], case5[1])
    print(ret)
