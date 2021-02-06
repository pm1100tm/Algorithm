import unittest
from typing import List
from itertools import combinations

from python.utils import CommonUtils


class Solution:
    """ 두 개 뽑아서 더하기
    정수 배열 numbers가 주어집니다.
    numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는
    모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
    
    제한사항
        numbers의 길이는 2 이상 100 이하입니다.
        numbers의 모든 수는 0 이상 100 이하입니다.
    
    입출력 예
        [2,1,3,4,1] -> [2,3,4,5,6,7]
        [5,0,2,7] -> [2,5,7,9,12]
    """
    
    def my_solution(self, numbers: List[int]) -> List[int]:
        """ 77.8
        """
        numbers_copy = numbers
        answer = set()
        
        while numbers:
            last_num = numbers.pop()
            
            for n in numbers_copy:
                answer.add(n + last_num)
        
        return sorted(answer)

    def best_solution_i_think(self, numbers: List[int]) -> List[int]:
        answer = []
        num_list = answer(combinations(numbers, 2))
        
        for nums in num_list:
            answer.append(nums[1] + nums[2])
        
        return sorted(answer)


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_list = [
            [2, 1, 3, 4, 1],
            [5, 0, 2, 7]
        ]
        
        self.result_list = [
            [2, 3, 4, 5, 6, 7],
            [2, 5, 7, 9, 12]
        ]
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        
        for index, case in enumerate(self.case_list):
            self.assertEqual(
                self.result_list[index],
                self.solution.my_solution(case)
            )

    @CommonUtils.logging_time
    def test_best_solution_i_think(self):
        for index, case in enumerate(self.case_list):
            self.assertEqual(
                self.result_list[index],
                self.solution.my_solution(case)
            )
        

if __name__ == "__main__":
    unittest.main()
    