import unittest
from typing import List

from python.utils import CommonUtils


class Solution:
    """ 행렬의 덧셈
    행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
    2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution 을 완성해주세요.

    제한 조건
        행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

    입출력 예
    arr1                arr2                return
    [[1, 2], [2, 3]]    [[3, 4], [5, 6]]    [[4, 6], [7, 9]]
    [[1], [2]]          [[3], [4]]          [[4], [6]]
    """
    
    def my_solution(self, arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
        answer = [[] for x in range(len(arr2))]
        
        for i in range(len(arr1)):
            for j in range(len(arr1[i])):
                answer[i].append(arr1[i][j] + arr2[i][j])
        
        return answer
    
    def best_solution_i_think(self, arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
        answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
        return answer
    
    def other_solution_one(self, arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
        answer = []
        
        for i, j in zip(arr1, arr2):
            temp = []
            
            for t1, t2 in zip(i, j):
                temp.append(t1 + t2)
            
            answer.append(temp)
        
        return answer


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one = [
            [[1, 2], [2, 3]], [[3, 4], [5, 6]]
        ]
        
        self.case_two = [
            [[1], [2]], [[3], [4]]
        ]
        
        self.result_one = [[4, 6], [7, 9]]
        self.result_two = [[4], [6]]
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        result_1 = self.solution.my_solution(self.case_one[0], self.case_one[1])
        result_2 = self.solution.my_solution(self.case_two[0], self.case_two[1])
        
        self.assertEqual(
            self.result_one,
            result_1
        )
        
        self.assertEqual(
            self.result_two,
            result_2
        )

    @CommonUtils.logging_time
    def test_best_solution_i_think(self):
        result_1 = self.solution.best_solution_i_think(self.case_one[0], self.case_one[1])
        result_2 = self.solution.best_solution_i_think(self.case_two[0], self.case_two[1])
        
        self.assertEqual(
            self.result_one,
            result_1
        )
    
        self.assertEqual(
            self.result_two,
            result_2
        )
        

if __name__ == '__main__':
    unittest.main()
