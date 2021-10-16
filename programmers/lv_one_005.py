""" K번째수

배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면

array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
2에서 나온 배열의 3번째 숫자는 5입니다.
배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
    array의 길이는 1 이상 100 이하입니다.
    array의 각 원소는 1 이상 100 이하입니다.
    commands의 길이는 1 이상 50 이하입니다.
    commands의 각 원소는 길이가 3입니다.

입출력 예
    array    : [1, 5, 2, 6, 3, 7, 4]
    commands : [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    return   : [5, 6, 3]

입출력 예 설명
    [1, 5, 2, 6, 3, 7, 4]를 2번째부터 5번째까지 자른 후 정렬합니다. [2, 3, 5, 6]의 세 번째 숫자는 5입니다.
    [1, 5, 2, 6, 3, 7, 4]를 4번째부터 4번째까지 자른 후 정렬합니다. [6]의 첫 번째 숫자는 6입니다.
    [1, 5, 2, 6, 3, 7, 4]를 1번째부터 7번째까지 자릅니다. [1, 2, 3, 4, 5, 6, 7]의 세 번째 숫자는 3입니다.
"""
from typing import List
from utils import CommonUtils
import unittest


class Solution:
    
    @CommonUtils.logging_time
    def my_solution(self, array: List[int], commands: List[List[int]]) -> List[int]:
        return [sorted(array[command[0]-1:command[1]])[command[2]-1] for command in commands]
    
    @CommonUtils.logging_time
    def solution_one(self, array: List[int], commands: List[List[int]]) -> List[int]:
        return list(map(lambda x: sorted(array[x[0] - 1:x[1]])[x[2] - 1], commands))
    
    @CommonUtils.logging_time
    def solution_two(self, array: List[int], commands: List[List[int]]) -> List[int]:
        answer = []
        
        for i, j, k in commands:
            answer.append(sorted(array[i-1 : j])[k - 1])
        
        return answer
    
    @CommonUtils.logging_time
    def solution_three(self, array: List[int], commands: List[List[int]]) -> List[int]:
        return [
            sorted(array[i-1 : j])[k - 1]
            for i, j, k in commands
        ]


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one_array    = [1, 5, 2 , 6 , 3, 7 , 4]
        self.case_one_commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    
    def test_my_solution(self):
        result = self.solution.my_solution(
            self.case_one_array,
            self.case_one_commands
        )
        
        self.assertEqual(
            [5, 6, 3],
            result
        )
    
    def test_solution_one(self):
        result = self.solution.solution_one(
            self.case_one_array,
            self.case_one_commands
        )
        
        self.assertEqual(
            [5, 6, 3],
            result
        )
    
    def test_solution_two(self):
        result = self.solution.solution_two(
            self.case_one_array,
            self.case_one_commands
        )
        
        self.assertEqual(
            [5, 6, 3],
            result
        )
    
    def test_solution_three(self):
        result = self.solution.solution_three(
            self.case_one_array,
            self.case_one_commands
        )
        
        self.assertEqual(
            [5, 6, 3],
            result
        )


if __name__ == '__main__':
    unittest.main()
