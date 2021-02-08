import unittest
from math import sqrt


class Solution:
    """ 정수 제곱근 판별
    임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
    n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고,
    n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
    
    제한 사항
        n은 1이상, 50000000000000 이하인 양의 정수입니다.
    
    입출력 예
        n       return
        121     144
        3       -1
        4       2
        15      -1
    """
    
    def my_solution(self, n: int) -> int:
        _sqrt = str(sqrt(n)).split('.')
        if _sqrt[1] == '0':
            return (int(sqrt(n)) + 1)**2
        
        return -1
    
    def best_solution_i_think(self, n: int) -> int:
        sqr = n ** (1/2)
        if sqr % 1 == 0:
            return int((sqr + 1)) ** 2
        
        return -1


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case = [
            121,
            3,
            50000000000000
        ]
        
        self.result = [
            144,
            -1,
            -1,
            2
        ]
    
    def test_my_solution(self):
        for index, case in enumerate(self.case):
            result = self.solution.my_solution(case)
            
            self.assertEqual(
                self.result[index],
                result
            )

    def test_best_solution_i_think(self):
        for index, case in enumerate(self.case):
            result = self.solution.best_solution_i_think(case)
            
            self.assertEqual(
                self.result[index],
                result
            )


if __name__ == '__main__':
    unittest.main()
