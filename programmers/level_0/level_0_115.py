"""
날짜 비교하기

정수 배열 date1과 date2가 주어집니다.
두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다.
각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.
만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.
"""
import datetime as dt
from utils import prvalue


@prvalue(print_result=True)
def solution(date1, date2):
    dtm1 = dt.datetime(date1[0], date1[1], date1[2])
    dtm2 = dt.datetime(date2[0], date2[1], date2[2])
    return int(dtm1 < dtm2)


if __name__ == '__main__':
    assert solution([2021, 12, 28], [2021, 12, 29]) == 1
    assert solution([1024, 10, 24], [1024, 10, 24]) == 0
