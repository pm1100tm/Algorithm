import unittest
import math
from typing import List


class Solution:
    """ 평균 구하기
    정수를 담고 있는 배열 arr 의 평균값을 return 하는 함수, solution 을 완성해보세요.
    
    제한사항
        arr 은 길이 1 이상, 100 이하인 배열입니다.
        arr 의 원소는 -10,000 이상 10,000 이하인 정수입니다.
    
    입출력 예
        arr	        return
        [1,2,3,4]   2.5
        [5,5]       5
    """
    
    def my_solution(self, arr: List[int]) -> float:
        return sum(arr) / len(arr)


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one = [1, 2, 3, 4]
        self.case_two = [5, 5]
        
        self.result_one = 2.5
        self.result_two = 5
    
    def test_my_solution(self):
        result_one = self.solution.my_solution(self.case_one)
        
        self.assertEqual(
            self.result_one,
            result_one
        )

        result_two = self.solution.my_solution(self.case_two)

        self.assertEqual(
            self.result_two,
            result_two
        )


if __name__ == '__main__':
    unittest.main()
