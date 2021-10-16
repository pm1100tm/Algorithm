import unittest
import re


class Solution:
    """ 핸드폰 번호 가리기
    프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
    전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를
    전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
    
    제한 조건
        s는 길이 4 이상, 20이하인 문자열입니다.
    
    입출력 예
        phone_number    return
        '01033334444'   '*******4444'
        '027778888'     '*****8888'
    """
    
    def my_solution(self, phone_number: str) -> str:
        temp = phone_number[-4::]
        stars = re.sub('[0-9]', '*', phone_number[0:-4])
        return stars + temp
    
    def best_solution_i_think(self, phone_number: str) -> str:
        return '*' * (len(phone_number) - 4) + phone_number[-4:]


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case = [
            '01033334444',
            '027778888'
        ]
        
        self.result = [
            '*******4444',
            '*****8888'
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
