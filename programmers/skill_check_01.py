""" 문제 설명

자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
    n은 10,000,000,000이하인 자연수입니다.

입출력 예
    n : 12345
    return : [5,4,3,2,1]
"""
from utils import CommonUtils


@CommonUtils.logging_time
def solution_quiz_one(n):
    answer = []
    
    for num in str(n)[::-1]:
        answer.append(int(num))
    
    return answer


""" 문제 설명

함수 solution은 정수 n을 매개변수로 입력받습니다.
n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

제한 조건
    n은 1이상 8000000000 이하인 자연수입니다.

입출력 예
    n
        118372
    return
        873211
"""
@CommonUtils.logging_time
def solution_quiz_two(n):
    answer = 0
    
    if n < 8000000000:
        answer = int(''.join(sorted(str(n), reverse=True)))
    
    return answer

r_two = solution_quiz_two(118372)
print(r_two)



