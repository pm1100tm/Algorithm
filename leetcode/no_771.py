""" 771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
    Input: jewels = "aA", stones = "aAAbbbb"
    Output: 3
    
Example 2:
    Input: jewels = "z", stones = "ZZ"
    Output: 0

Constraints:
    1 <= jewels.length, stones.length <= 50
    jewels and stones consist of only English letters.
    All the characters of jewels are unique.
"""
from utils import CommonUtils
import unittest


class Solution:
    
    @CommonUtils.logging_time
    def num_jewel_in_stone_one(self, jewels: str, stones: str) -> int:
        return sum(stones.count(jewel) for jewel in jewels)
    
    @CommonUtils.logging_time
    def num_jewel_in_stone_two(self, jewels: str, stones: str) -> int:
        result = 0
        
        for stone in stones:
            if stone in jewels:
                result += 1
        
        return result
    
    @CommonUtils.logging_time
    def num_jewel_in_stone_three(self, jewels: str, stones: str) -> int:
       return sum(jewel in stones for jewel in jewels)


class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.solution = Solution()
    
    def test_num_jewel_in_stone_one_1(self):
        jewels = 'aA'
        stones = 'aAAbbbb'
        
        result = self.solution.num_jewel_in_stone_one(jewels, stones)
        self.assertEqual(3, result)

    def test_num_jewel_in_stone_one_2(self):
        jewels = 'z'
        stones = 'ZZ'
    
        result = self.solution.num_jewel_in_stone_one(jewels, stones)
        self.assertEqual(0, result)
    

if __name__ == '__main__':
    unittest.main()
