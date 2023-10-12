import unittest

from utils import CommonUtils


class Solution:
    """ 약수의 합
    정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
    
    제한 사항
        n은 0 이상 3000이하인 정수입니다.
    
    입출력 예
        n   return
        12  28
        5   6
    """
    
    def my_solution(self, n: int) -> int:
        answer = 0
        
        if not n:
            return 0
        
        for i in range(n):
            if n % (i + 1) == 0:
                answer += i + 1
        
        return answer
    
    def other_solution_one(self, n: int) -> int:
        if not n:
            return 0
        
        return sum([i + 1 for i in range(n) if n % (i + 1) == 0])
    

class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case = [
            0,
            1,
            5,
            12,
            100,
            3000
        ]
        
        self.case_result = [
            0,
            1,
            6,
            28,
            217,
            9360
        ]
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        
        for index, case in enumerate(self.case):
            
            result = self.solution.my_solution(case)
            
            self.assertEqual(
                self.case_result[index],
                result
            )

    @CommonUtils.logging_time
    def test_other_solution_one(self):
        for index, case in enumerate(self.case):
            result = self.solution.other_solution_one(case)
            
            self.assertEqual(
                self.case_result[index],
                result
            )


if __name__ == '__main__':
    unittest.main()
