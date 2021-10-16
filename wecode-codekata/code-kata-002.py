""" 문제
Q. reverse 함수에 정수인 숫자를 인자로 받습니다. 그 숫자를 뒤집어서 return 해주세요.

x: 숫자
return: 뒤집어진 숫자를 반환!

x: 1234
return: 4321

x: -1234
return: -4321

x: 1230
return: 321
"""
import unittest
from utils import CommonUtils


class Solution:
    
    @CommonUtils.logging_time
    def reverse(self, num: int) -> int:
        
        if num < 0:
            return int(str(num * -1)[::-1]) * -1
        
        return int(str(num)[::-1])


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_reverse_1(self):
        case_1 = 1234
        
        self.assertEqual(
            4321,
            self.solution.reverse(case_1)
        )
    
    def test_reverse_2(self):
        case_2 = -1234
        
        self.assertEqual(
            -4321,
            self.solution.reverse(case_2)
        )
    
    def test_reverse_3(self):
        case_3 = 1230
        
        self.assertEqual(
            321,
            self.solution.reverse(case_3)
        )
    

if __name__ == '__main__':
    unittest.main()
