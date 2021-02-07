import unittest
import string


class Solution:
    """ 시저 암호
    어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다.
    예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다.
    문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.
    
    제한 조건
        공백은 아무리 밀어도 공백입니다.
        s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
        s의 길이는 8000이하입니다.
        n은 1 이상, 25이하인 자연수입니다.
    
    입출력 예
        s        n   result
        'AB'     1   'BC'
        'z'      1   'a'
        'a B z'  4   'e F d'
    """
    
    def my_solution(self, caesar: str, n: int) -> str:
        answer = ''
        
        for char in caesar:
            
            if char == ' ':
                answer += ' '
                continue
            
            temp = ord(char) + n

            if char.isupper():
                if temp > 90:
                    answer += chr(temp - 26)
                    
                else:
                    answer += chr(temp)
            
            if char.islower():
                if temp > 122:
                    answer += chr(temp - 26)
                    
                else:
                    answer += chr(temp)
        
        return answer
    
    def best_solution_i_think(self, s: str, n: int) -> str:
        result = ''
        
        for char in s:
            
            if not char.isalpha():
                result += char
                continue
            
            if char.islower():
                result += chr((ord(char) - ord("a") + n) % 26 + ord("a"))
            else:
                result += chr((ord(char) - ord("A") + n) % 26 + ord("A"))
        
        return result
    
    def other_solution_one(self, s: str, n: int) -> str:
        result = ""
        base = ""
        for c in s:
            if c in string.ascii_lowercase:
                base = string.ascii_lowercase
                
            elif c in string.ascii_uppercase:
                base = string.ascii_uppercase
            
            else:
                result += c
                continue
            
            a = base.index(c) + n
            result += base[a % len(base)]
            
        return result


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one_str = 'AB'
        self.case_one_n = 1
        self.case_one_result = 'BC'

        self.case_two_str = 'z'
        self.case_two_n = 1
        self.case_two_result = 'a'

        self.case_three_str = 'a B z'
        self.case_three_n = 4
        self.case_three_result = 'e F d'
    
    def test_my_solution(self):
        self.solution = Solution()
        
        result = self.solution.my_solution(
            self.case_one_str,
            self.case_one_n
        )
        
        self.assertEqual(
            self.case_one_result,
            result
        )

    def test_best_solution_i_think_one(self):
        self.solution = Solution()
    
        result = self.solution.best_solution_i_think(
            self.case_one_str,
            self.case_one_n
        )
    
        self.assertEqual(
            self.case_one_result,
            result
        )
    
    def test_best_solution_i_think_two(self):
        self.solution = Solution()
        
        result = self.solution.best_solution_i_think(
            self.case_two_str,
            self.case_two_n
        )
        
        self.assertEqual(
            self.case_two_result,
            result
        )

    def test_best_solution_i_think_three(self):
        self.solution = Solution()
    
        result = self.solution.best_solution_i_think(
            self.case_three_str,
            self.case_three_n
        )
    
        self.assertEqual(
            self.case_three_result,
            result
        )


if __name__ == '__main__':
    unittest.main()
