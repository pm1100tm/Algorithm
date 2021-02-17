import unittest
from typing import List

from python.utils import CommonUtils


class Solution:
    """ 실패율
    슈퍼 게임 개발자 오렐리는 큰 고민에 빠졌다. 그녀가 만든 프랜즈 오천성이 대성공을 거뒀지만,
    요즘 신규 사용자의 수가 급감한 것이다.
    원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다.
    이 문제를 어떻게 할까 고민 한 그녀는 동적으로 게임 시간을 늘려서 난이도를 조절하기로 했다.
    역시 슈퍼 개발자라 대부분의 로직은 쉽게 구현했지만, 실패율을 구하는 부분에서 위기에 빠지고 말았다.
    오렐리를 위해 실패율을 구하는 코드를 완성하라.
    
    실패율은 다음과 같이 정의한다.
        스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
        전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages 가 매개변수로 주어질 때,
        실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
    
    제한사항
        스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
        stages 의 길이는 1 이상 200,000 이하이다.
        stages 에는 1 이상 N + 1 이하의 자연수가 담겨있다.
        각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
        단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
        만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
        스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
    
    입출력 예
        N   stages                      result
        5   [2, 1, 2, 6, 2, 4, 3, 3]    [3,4,2,1,5]
        4   [4,4,4,4,4]                 [4,1,2,3]
        
        1 번 스테이지 실패율 : 1/8
        2 번 스테이지 실패율 : 3/7
        3 번 스테이지 실패율 : 2/4
        4 번 스테이지 실패율 : 1/2
        5 번 스테이지 실패율 : 0/1
    """
    
    def my_solution(self, N: int, stages: List[int]) -> List[int]:
        """
        통과는 되지만 효율성 테스트에서 문제가 있음
        """
        
        stage_len = len(stages)
        failure_data = {}
        
        for i in range(N):
            users_num = stages.count(i+1)
            
            if not users_num:
                failure_data[i + 1] = 0
            else:
                failure_data[i + 1] = users_num / stage_len
            
            stage_len -= users_num
        
        sorted_data = sorted(failure_data.items(), key=lambda kv: kv[1], reverse=True)
        
        return [data[0] for data in sorted_data]

    def other_solution_one(self, N: int, stages: List[int]) -> List[int]:
        fail = {}
        
        for i in range(1, N + 1):
            try:
                fail_ = len([a for a in stages if a == i]) / len([a for a in stages if a >= i])
            
            except Exception as e:
                fail_ = 0
            
            fail[i] = fail_
        
        return sorted(fail, key=fail.get, reverse=True)


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one = [5, [2, 1, 2, 6, 2, 4, 3, 3]]
        self.case_two = [4, [4, 4, 4, 4, 4]]
        
        self.result_one = [3, 4, 2, 1, 5]
        self.result_two = [4, 1, 2, 3]
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        result_one = self.solution.my_solution(self.case_one[0], self.case_one[1])
        
        self.assertEqual(
            self.result_one,
            result_one
        )

        result_two = self.solution.my_solution(self.case_two[0], self.case_two[1])
        
        self.assertEqual(
            self.result_two,
            result_two
        )

    @CommonUtils.logging_time
    def test_other_solution_one(self):
        result_one = self.solution.other_solution_one(self.case_one[0], self.case_one[1])
        
        self.assertEqual(
            self.result_one,
            result_one
        )
        
        result_two = self.solution.other_solution_one(self.case_two[0], self.case_two[1])

        self.assertEqual(
            self.result_two,
            result_two
        )


if __name__ == '__main__':
    unittest.main()
