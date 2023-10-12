import unittest
from datetime import date

from utils import CommonUtils


class Solution:
    """ 2016년
    2016년 1월 1일은 금요일입니다.
    2016년 a월 b일은 무슨 요일일까요?
    두 수 a,b 를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을 완성하세요.
    요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다.
    예를 들어 a=5, b=24라면 5월 24일은 화요일이므로 문자열 TUE를 반환하세요.
    
    제한 조건
        2016년은 윤년입니다.
        2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)
    
    입출력 예
        a   b   result
        5   24  TUE
    """
    
    def my_solution(self, a: int, b: int) -> str:
        days = {
            1: 'MON',
            2: 'TUE',
            3: 'WED',
            4: 'THU',
            5: 'FRI',
            6: 'SAT',
            7: 'SUN'
        }
        
        return days[date(2016, a, b).weekday() + 1]
    
    def best_solution_i_think(self, a: int, b: int) -> str:
        """ 이것은 코드인가 예술인가.. 배운 분..
        """
        
        answer = ""
        
        if a >= 2:
            b += 31
            if a >= 3:
                b += 29  # 2월
                if a >= 4:
                    b += 31  # 3월
                    if a >= 5:
                        b += 30  # 4월
                        if a >= 6:
                            b += 31  # 5월
                            if a >= 7:
                                b += 30  # 6월
                                if a >= 8:
                                    b += 31  # 7월
                                    if a >= 9:
                                        b += 31  # 8월
                                        if a >= 10:
                                            b += 30  # 9월
                                            if a >= 11:
                                                b += 31  # 10월
                                                if a == 12:
                                                    b += 30  # 11월
        b = b % 7
        
        if b == 1:
            answer = "FRI"
        elif b == 2:
            answer = "SAT"
        elif b == 3:
            answer = "SUN"
        elif b == 4:
            answer = "MON"
        elif b == 5:
            answer = "TUE"
        elif b == 6:
            answer = "WED"
        else:
            answer = "THU"
        
        return answer


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.a = 5
        self.b = 24
        self.result = "TUE"
        
        self.month = 2
        self.days  = [7, 8, 9, 10, 11, 12, 13]
        
        self.case_results = [
            'SUN',
            'MON',
            'TUE',
            'WED',
            'THU',
            'FRI',
            'SAT',
        ]

    @CommonUtils.logging_time
    def test_my_solution(self):
        case_one_result = self.solution.my_solution(self.a, self.b)
        
        self.assertEqual(
            self.result,
            case_one_result
        )
        
        for index in range(len(self.case_results)):
            
            result = self.solution.my_solution(self.month, self.days[index])
            
            self.assertEqual(
                self.case_results[index],
                result
            )
    
    @CommonUtils.logging_time
    def test_best_solution_i_think(self):
        case_one_result = self.solution.best_solution_i_think(self.a, self.b)
        
        self.assertEqual(
            self.result,
            case_one_result
        )
        
        for index in range(len(self.case_results)):
            result = self.solution.best_solution_i_think(self.month, self.days[index])
            
            self.assertEqual(
                self.case_results[index],
                result
            )


if __name__ == '__main__':
    unittest.main()
