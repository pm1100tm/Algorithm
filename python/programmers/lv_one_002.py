""" 문자열 내 p와 y의 개수

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해
같으면 True, 다르면 False를 return 하는 solution를 완성하세요.

'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

제한사항
    문자열 s의 길이 : 50 이하의 자연수
    문자열 s는 알파벳으로만 이루어져 있습니다.
"""
import unittest
from python.utils import CommonUtils
from collections  import Counter


class Solution:
    
    @CommonUtils.logging_time
    def solution_one(self, s):
        
        char_map = {
            'p': 0,
            'y': 0
        }
        
        for char in s.lower():
            
            if char in char_map:
                char_map[char] += 1
        
        return char_map['p'] == char_map['y']
    
    @CommonUtils.logging_time
    def solution_two(self, s):
        return s.lower().count('p') == s.lower().count('y')
    
    @CommonUtils.logging_time
    def solution_three(self, s):
        c = Counter(s.lower())
        return c['y'] == c['p']
    

class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        self.case_1 = 'pPooooooooooyY'
        self.case_2 = 'Pyyyyyyyyyyyy'
    
    def test_solution_one(self):
        self.assertEqual(
            True,
            self.solution.solution_one(self.case_1)
        )
        
        self.assertEqual(
            False,
            self.solution.solution_one(self.case_2)
        )

    def test_solution_two(self):
        self.assertEqual(
            True,
            self.solution.solution_two(self.case_1)
        )
    
        self.assertEqual(
            False,
            self.solution.solution_two(self.case_2)
        )
    
    def test_solution_three(self):
        self.assertEqual(
            True,
            self.solution.solution_three(self.case_1)
        )
    
        self.assertEqual(
            False,
            self.solution.solution_three(self.case_2)
        )


if __name__ == '__main__':
    unittest.main()
