import unittest
from typing import List


class Solution:
    """ x만큼 간격이 있는 n개의 숫자
    함수 solution 은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
    다음 제한 조건을 보고, 조건을 만족하는 함수, solution 을 완성해주세요.

    제한 조건
        x는 -10000000 이상, 10000000 이하인 정수입니다.
        n은 1000 이하인 자연수입니다.
    
    입출력 예
        x   n   answer
        2   5   [2,4,6,8,10]
        4   3   [4,8,12]
        -4  2   [-4, -8]
    """
    
    def my_solution(self, x: int, n: int) -> List[int]:
        temp = x
        answer = [x]
        
        for i in range(n-1):
            x += temp
            answer.append(x)
        
        return answer
    
    def best_solution_i_thin(self, x: int, n: int) -> List[int]:
        return [i * x + x for i in range(n)]
    

class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case = {
            'case_1': [2, 5],
            'case_2': [4, 3],
            'case_3': [-4, 2]
        }
        
        self.result = {
            'result_1': [2, 4, 6, 8, 10],
            'result_2': [4, 8, 12],
            'result_3': [-4, -8]
        }
    
    def test_my_solution(self):
        
        r1 = self.solution.my_solution(
            self.case['case_1'][0],
            self.case['case_1'][1]
        )
        
        self.assertEqual(
            self.result['result_1'],
            r1
        )

        r2 = self.solution.my_solution(
            self.case['case_2'][0],
            self.case['case_2'][1]
        )

        self.assertEqual(
            self.result['result_2'],
            r2
        )

        r3 = self.solution.my_solution(
            self.case['case_3'][0],
            self.case['case_3'][1]
        )

        self.assertEqual(
            self.result['result_3'],
            r3
        )


if __name__ == '__main__':
    unittest.main()
