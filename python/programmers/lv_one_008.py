import unittest
import math

from typing       import final
from python.utils import CommonUtils


class Solution:
    """ 수박수박수박수박수박수?
    길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요.
    예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.
    
    제한 조건
        n은 길이 10,000이하인 자연수입니다.
    
    입출력 예
        n   return
        3   수박수
        4   수박수박
    """
    
    def my_solution(self, n: int) -> str:
        if not n:
            return ''
        
        STR_CONST: final = '수박'
        
        return STR_CONST * int(n / 2) if n % 2 == 0 else (STR_CONST * math.ceil(n / 2))[:-1]
    
    def solution_one(self, n: int) -> str:
        return ('수박' * n)[0:n]
    
    def solution_two(self, n: int) -> str:
        return "수박" * (n // 2) + "수" * (n % 2)


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_1 = 0
        self.case_2 = 1
        self.case_3 = 2
        self.case_4 = 8
        self.case_5 = 9

    @CommonUtils.logging_time
    def test_my_solution(self):
        
        self.assertEqual(
            '',
            self.solution.my_solution(self.case_1)
        )
        
        self.assertEqual(
            '수',
            self.solution.my_solution(self.case_2)
        )
        
        self.assertEqual(
            '수박',
            self.solution.my_solution(self.case_3)
        )
        
        self.assertEqual(
            '수박수박수박수박',
            self.solution.my_solution(self.case_4)
        )
        
        self.assertEqual(
            '수박수박수박수박수',
            self.solution.my_solution(self.case_5)
    
        )
    
    @CommonUtils.logging_time
    def test_solution_one(self):
        self.assertEqual(
            '',
            self.solution.solution_one(self.case_1)
        )
    
        self.assertEqual(
            '수',
            self.solution.solution_one(self.case_2)
        )
    
        self.assertEqual(
            '수박',
            self.solution.solution_one(self.case_3)
        )
    
        self.assertEqual(
            '수박수박수박수박',
            self.solution.solution_one(self.case_4)
        )
    
        self.assertEqual(
            '수박수박수박수박수',
            self.solution.solution_one(self.case_5)
        )


if __name__ == '__main__':
    unittest.main()