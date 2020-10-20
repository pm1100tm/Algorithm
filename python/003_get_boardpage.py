"""
A씨는 게시판 프로그램을 작성하고 있다.
A씨는 게시물의 총 건수와 한 페이지에 보여줄 게시물수를 입력으로 주었을 때 총 페이지수를 리턴하는 프로그램이 필요하다고 한다.

입력 : 총건수(m), 한페이지에 보여줄 게시물수(n) (단 n은 1보다 크거나 같다. n >= 1)
출력 : 총페이지수
"""
import math


class PostNumException(Exception):
    def __init__(self):
        super().__init__("한 페이지에 보여줄 게시물의 수는 1 이상입니다.")


def get_page_num(m, n):
    """
    :param m: 총 건수(총 레코드 수)
    :param n: 한 페이지에 보여줄 레코드 수
    :return: 총 페이지 수
    """
    if n < 1:
        raise PostNumException()
    else:
        return math.ceil(m/n)


print(get_page_num(0, 1))
print(get_page_num(1, 1))
print(get_page_num(2, 1))
print(get_page_num(1, 10))
print(get_page_num(10, 10))
print(get_page_num(11, 10))
print(get_page_num(11, 0))