import unittest
from typing import List

from python.utils import CommonUtils


class Solution:
    """ 같은 숫자는 싫어
    배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
    이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
    단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
    
    예를 들면,
        arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
        arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
    
    배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
    
    제한사항
        배열 arr의 크기 : 1,000,000 이하의 자연수
        배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
    """
    
    def my_solution(self, arr: List[int]) -> List[int]:
        answer = [arr[0]]
        
        for i in range(1, len(arr)):
            if answer[-1] != arr[i]:
                answer.append(arr[i])
                
        return answer
    
    def best_solution_i_think(self, arr: List[int]) -> List[int]:
        answer = []
        
        for a in arr:
            if answer[-1:] == [a]:
                continue
            
            answer.append(a)
        
        return answer


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()

        self.case_one        = [1, 1, 3, 3, 0, 1, 1]
        self.case_two        = [4, 4, 4, 3, 3]
        
        self.case_one_result = [1, 3, 0, 1]
        self.case_two_result = [4, 3]
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        result_case_one = self.solution.my_solution(self.case_one)
        result_case_two = self.solution.my_solution(self.case_two)
        
        self.assertEqual(
            self.case_one_result,
            result_case_one
        )

        self.assertEqual(
            self.case_two_result,
            result_case_two
        )
    
    @CommonUtils.logging_time
    def test_best_solution_i_think(self):
        result_case_one = self.solution.best_solution_i_think(self.case_one)
        result_case_two = self.solution.best_solution_i_think(self.case_two)
        
        self.assertEqual(
            self.case_one_result,
            result_case_one
        )
        
        self.assertEqual(
            self.case_two_result,
            result_case_two
        )


if __name__ == '__main__':
    unittest.main()
