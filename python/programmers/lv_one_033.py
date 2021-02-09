import unittest


class Solution:
    """ 짝수와 홀수
    정수 num 이 짝수일 경우 Even 을 반환하고 홀수인 경우 Odd 를 반환하는 함수, solution 을 완성해주세요.
    
    제한 조건
        num 은 int 범위의 정수입니다.
        0은 짝수입니다.
    
    입출력 예
        num	    return
        3       'Odd'
        4       'Even'
    """
    
    def my_solution(self, num: int) -> str:
        return 'Odd' if num % 2 != 0 else 'Even'
    
    def pythonic_code_i_think(self, num: int) -> str:
        return 'Odd' if num % 2 else 'Even'


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case = [
            3,
            4,
            0,
            123415125213123
        ]
        
        self.result = [
            'Odd',
            'Even',
            'Even',
            'Odd'
        ]
    
    def test_my_solution(self):
        
        for index, case in enumerate(self.case):
            result = self.solution.my_solution(case)
            
            self.assertEqual(
                self.result[index],
                result
            )
            

if __name__ == '__main__':
    unittest.main()