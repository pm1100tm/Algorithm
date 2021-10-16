import unittest
from typing import List

from utils import CommonUtils


class Solution:
    """ 크레인 인형뽑기 게임
    """
    
    def my_solution(self, board: List[List[int]], moves: List[int]):
        count = 0
        answer = []
        
        for m in moves:
            
            for b in board:
                
                if b[m - 1] != 0:
                    temp = b[m - 1]
                    
                    if not answer:
                        b[m - 1] = 0
                        answer.append(temp)
                        break

                    if answer[-1] != temp:
                        b[m - 1] = 0
                        answer.append(temp)
                        break
                        
                    else:
                        count += 2
                        b[m - 1] = 0
                        answer.pop()
                        break
        
        return count


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one = {
            'board' : [
                [0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1]
            ],
            'moves' : [1, 5, 3, 5, 1, 2, 1, 4]
        }
        
        self.case_one_result = 4
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        result = self.solution.my_solution(
            self.case_one['board'], self.case_one['moves']
        )
        
        self.assertEqual(
            self.case_one_result,
            result
        )


if __name__ == '__main__':
    unittest.main()
