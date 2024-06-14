"""2016년
2016년 1월 1일은 금요일입니다.
2016년 a월 b일은 무슨 요일일까요?
두 수 a,b 를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.

제한 조건
- 2016년은 윤년입니다.
- 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
"""
import datetime as dt


def solution(a: int, b: int):
    days = {
        0: 'MON',
        1: 'TUE',
        2: 'WED',
        3: 'THU',
        4: 'FRI',
        5: 'SAT',
        6: 'SUN'
    }

    dtm = dt.datetime(year=2016, month=a, day=b)

    return days.get(dtm.weekday())


if __name__ == '__main__':
    assert solution(1, 1) == 'FRI'
    assert solution(5, 24) == 'TUE'
    assert solution(2, 29) == 'MON'
