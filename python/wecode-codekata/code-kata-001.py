""" 문제
two_sum() 에 숫자 리스트와 '특정 수'를 인자로 넘기면,
더해서 '특정 수'가 나오는 index를 배열에 담아 return 하라.

제약 조건:
    nums: 숫자 배열
    target: 두 수를 더해서 나올 수 있는 합계
    return: 두 수의 index를 가진 숫자 배열
    target으로 보내는 합계의 조합은 배열 전체 중에 2개 밖에 없다고 가정한다.

예제:
    nums : [4, 9, 11, 14]
    target : 13
    nums[0] + nums[1] = 4 + 9 = 13
    return : [0, 1]
"""
import unittest
from typing import List
from python.utils import CommonUtils


class Solution:
    
    @CommonUtils.logging_time
    def two_sum(self, num_list: List[int], target: int) -> ():
        
        for num in num_list:
            if num > target:
                continue
            
            temp = target - num
            
            if temp in num_list:
                return num_list.index(num), num_list.index(temp)


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
        
        self.case_1 = ([4, 9, 11, 14], 13)
        self.case_2 = ([4, 10, 120, 30, 20, 50], 60)
    
    def test_two_sum_case_1(self):
        n_list = self.case_1[0]
        target = self.case_1[1]
        
        result = self.solution.two_sum(n_list, target)
        self.assertEqual(
            (0, 1),
            result
        )
    
    def test_two_sum_case_2(self):
        n_list = self.case_2[0]
        target = self.case_2[1]
        
        result = self.solution.two_sum(n_list, target)
        
        self.assertEqual(
            (1, 5),
            result
        )

        
if __name__ == "__main__":
    unittest.main()
