"""
메모리공간을 동적으로 사용하여 데이터 관리하기

프로그램 실행 순서
1. 입력할 정수의 개수를 사용자로부터 입력 받는다.
2 .입력받은 정수의 개수만큼 정수를 입력받는다.
3 .입력받은 정수의 합과 평균 값을 출력한다.
4 .할당된 메모리공간을 비운다.

메모리공간은 사용자의 입력 수의 따라 변동된다.
사용한 공간은 마지막에 비워야 한다.
배열을 사용하면 안된다.
"""


def get_sum_and_avg():
    """
    Generate a number of integer based on a number user input at first step
    :return: sum ->(int) sum of a number of integer, average ->(float) average of sum
    """
    try:
        number_of_int = int(input())
        aggregate, average = 0, 0
        for i in range(0, number_of_int):
            aggregate += int(input())

        average = aggregate / number_of_int
        print("입력 받은 정수의 총 합은:{agg}, 평균 값은:{avg} 입니다."
              .format(agg=aggregate, avg=average))
    except Exception as e:
        print("raised exception: ", end=" ")
        print(e)
    finally:
        del number_of_int, aggregate, average


get_sum_and_avg()