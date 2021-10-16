import unittest
from typing import List

from utils import CommonUtils


class Solution:
    """ 전화번호 목록
    전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
    전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

    구조대 : 119
    박준영 : 97 674 223
    지영석 : 11 9552 4421
    
    전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
    어떤 번호가 다른 번호의 접두어인 경우가 있으면 false 를 그렇지 않으면 true 를 return 하도록 solution 함수를 작성해주세요.

    제한 사항
    phone_book 의 길이는 1 이상 1,000,000 이하입니다.
    각 전화번호의 길이는 1 이상 20 이하입니다.
    
    입출력 예제
        phone_book                          return
        ['119', '97674223', '1195524421']   false
        ['123', '456', '789']               true
        ['12', '123', '1235', '567', '88']  false
    
    """
    
    def my_solution(self, phone_book: List[str]) -> bool:
        """ 테스트 케이스 통과
        효율성 테스트 실패
        """
        answer = True
        phone_hash = {phone : 0 for phone in phone_book}
        
        for key in phone_hash.keys():
            
            for phone in phone_book:
                if phone == key or len(key) > len(phone):
                    continue
                
                if phone.startswith(key):
                    answer = False
                    break
        
        return answer
    
    def my_solution_two(self, phone_book: List[str]) -> bool:
        answer = True
        phone_book.sort()
        
        for i in range(len(phone_book) - 1):
            if phone_book[i + 1].startswith(phone_book[i]):
                answer = False
                break
        
        return answer

    def other_solution_one(self, phone_book: List[str]) -> bool:
        answer = True
        phone_numbers = sorted(phone_book)
        
        for p1, p2 in zip(phone_numbers, phone_book[1:]):
            if p2.startswith(p1):
                answer = False
                break
        
        return answer
    
    def other_solution_two(self, phone_book: List[str]) -> bool:
        answer = True
        for i in range(len(phone_book)):
            pivot = phone_book[i]
            
            for j in range(i + 1, len(phone_book)):
                
                if len(pivot) > len(phone_book[j]):
                    continue
                
                if pivot == phone_book[j][:len(pivot)]:
                    answer = False
                    break
        
        return answer


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

        self.case_1 = ['119', '97674223', '1195524421']
        self.case_2 = ['123', '456', '789']
        self.case_3 = ['12', '123', '1235', '567', '88']

        self.result_1 = False
        self.result_2 = True
        self.result_3 = False
    
    @CommonUtils.logging_time
    def test_my_solution(self):
        result_1 = self.solution.my_solution(self.case_1)

        self.assertEqual(
            self.result_1,
            result_1
        )

        result_2 = self.solution.my_solution(self.case_2)

        self.assertEqual(
            self.result_2,
            result_2
        )

        result_3 = self.solution.my_solution(self.case_3)

        self.assertEqual(
            self.result_3,
            result_3
        )
    
    def test_my_solution_two(self):
        result_1 = self.solution.my_solution_two(self.case_1)

        self.assertEqual(
            self.result_1,
            result_1
        )

        result_2 = self.solution.my_solution_two(self.case_2)

        self.assertEqual(
            self.result_2,
            result_2
        )

        result_3 = self.solution.my_solution_two(self.case_3)

        self.assertEqual(
            self.result_3,
            result_3
        )


if __name__ == '__main__':
    unittest.main()
