""" no_1512.py

Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

특정한 숫자 배열 nums.
(i, j) 쌍은 good 이라고 불리는데, 만약 nums[i] == nums[j] and i < j 일 경우
good pair 를 리턴시켜라.

Example 1:
    Input: nums = [1,2,3,1,1,3]
    Output: 4
    Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Example 2:
    Input: nums = [1,1,1,1]
    Output: 6
    Explanation: Each pair in the array are good.

Example 3:
    Input: nums = [1,2,3]
    Output: 0
"""
from utils import CommonUtils
from typing import List


class Solution:
    
    @CommonUtils.logging_time
    def get_good_pairs_one(self, nums: List[int]) -> int:
        count = 0
        
        for i in range(len(nums)-1):
            for j in nums[i+1:]:
                if nums[i] == j:
                    count += 1
        
        return count


if __name__ == '__main__':
    solution = Solution()
    
    test_case_1 = [1, 2, 3, 1, 1, 3]
    test_case_2 = [1, 1, 1, 1]
    test_case_3 = [1, 2, 3]
    
    r1 = solution.get_good_pairs_one(test_case_1)
    r2 = solution.get_good_pairs_one(test_case_2)
    r3 = solution.get_good_pairs_one(test_case_3)
    
    print(r1, r2, r3)