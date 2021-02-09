import unittest
from typing import List


class Solution:
    """ 내적
    길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다.
    a와 b의 내적을 return 하도록 solution 함수를 완성해주세요.
    이때, a와 b의 내적은 a[0]*b[0] + a[1]*b[1] + ... + a[n-1]*b[n-1] 입니다. (n은 a, b의 길이)
    
    제한사항
        a, b의 길이는 1 이상 1,000 이하입니다.
        a, b의 모든 수는 -1,000 이상 1,000 이하입니다.

    입출력 예
        a           b               result
        [1,2,3,4]   [-3,-1,0,2]     3
        [-1,0,1]    [1,0,-1]        -2

    """
    
    def my_solution(self, a: List[int], b: List[int]):
        if len(a) == 1:
            return a[-1] * b[-1]
    
        answer = 0
        for index in range(len(a)):
            answer += a[index] * b[index]
    
        return answer
    
    def other_solution_one(self, a: List[int], b: List[int]):
        return sum([x*y for x, y in zip(a, b)])
    
    def other_solution_two(self, a: List[int], b: List[int]):
        return sum(map(lambda i: a[i] * b[i], range(len(a))))
    
    def other_solution_three(self, a: List[int], b: List[int]):
        answer = 0
        
        for x, y in zip(a, b):
            answer += x * y
        
        return answer


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_a = [
            [1, 2, 3, 4],
            [-1, 0, 1]
        ]
        
        self.case_b = [
            [-3, -1, 0, 2],
            [1, 0, -1]
        ]
        
        self.result = [
            3,
            -2
        ]
    
    def test_my_solution(self):
        count = 0
        
        for case_a, case_b in zip(self.case_a, self.case_b):
            result = self.solution.my_solution(case_a, case_b)
            
            self.assertEqual(
                self.result[count],
                result
            )
            
            count += 1

    def test_other_solution_one(self):
        count = 0
    
        for case_a, case_b in zip(self.case_a, self.case_b):
            result = self.solution.other_solution_one(case_a, case_b)
            
            self.assertEqual(
                self.result[count],
                result
            )
        
            count += 1

    def test_other_solution_two(self):
        count = 0
    
        for case_a, case_b in zip(self.case_a, self.case_b):
            result = self.solution.other_solution_two(case_a, case_b)
        
            self.assertEqual(
                self.result[count],
                result
            )
            
            count += 1

    def test_other_solution_three(self):
        count = 0
    
        for case_a, case_b in zip(self.case_a, self.case_b):
            result = self.solution.other_solution_three(case_a, case_b)
        
            self.assertEqual(
                self.result[count],
                result
            )
        
            count += 1


if __name__ == '__main__':
    unittest.main()
