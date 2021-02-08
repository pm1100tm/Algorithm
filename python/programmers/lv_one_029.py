import unittest
from typing import List

from python.utils import CommonUtils


class Solution:
    """ 자연수 뒤집어 배열로 만들기
    자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
    예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

    제한 조건
        n은 10,000,000,000이하인 자연수입니다.
    
    입출력 예
        n       return
        12345   [5,4,3,2,1]
    """
    
    def my_solution(self, n: int) -> List[int]:
        new_str = str(n)[::-1]
        return list(map(int, new_str))
    
    def best_solution_i_think(self, n: int) -> List[int]:
        return [int(char) for char in str(n)][::-1]
    
    def other_solution_one(self, n: int) -> List[int]:
        return list(map(int, reversed(str(n))))


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case = [
            12345,
            123456789
        ]
        
        self.result = [
            [5, 4, 3, 2, 1],
            [9, 8, 7, 6, 5, 4, 3, 2, 1]
        ]
    
    @CommonUtils.logging_time
    def test_best_solution_i_think(self):
        
        for index in range(len(self.case)):
            result = self.solution.best_solution_i_think(
                self.case[index]
            )
            
            self.assertEqual(
                self.result[index],
                result
            )
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        
        for index in range(len(self.case)):
            result = self.solution.my_solution(
                self.case[index]
            )
        
            self.assertEqual(
                self.result[index],
                result
            )


if __name__ == '__main__':
    unittest.main()
