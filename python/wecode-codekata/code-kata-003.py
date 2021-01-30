""" 문제
String 형인 str 인자에서 중복되지 않은 알파벳으로 이루어진 제일 긴 단어의 길이를 반환해주세요.

str = "abcabcabc"
return은 3
=> 'abc' 가 제일 길기 때문

str = "aaaaa"
return은 1
=> 'a' 가 제일 길기 때문

str = "sttrg"
return은 3
=> 'trg' 가 제일 길기 때문
"""
import unittest
from python.utils import CommonUtils


class Solution:
    
    @CommonUtils.logging_time
    def most_longest_word_1(self, words: str) -> int:
        
        if not words:
            return 0
        
        chars = ''
        max_count = 0
        
        for word in words:
            
            if chars.find(word) != -1:
                
                if max_count < len(chars):
                    max_count = len(chars)
                
                chars = ''
                chars += word
                continue
                
            chars = chars + word
        
        if max_count < len(chars):
            return len(chars)
        
        return max_count
    
    @CommonUtils.logging_time
    def most_longest_word_2(self, words: str) -> int:
        
        if not words:
            return 0
        
        chars = ''
        count_list = []
        
        for word in words:
            
            if chars.find(word) != -1:
                count_list.append(len(chars))
                chars = ''
                chars += word
                continue
                
            chars = chars + word
        
        return max(count_list)
    

class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
    
    def test_1_most_longest_word_1(self):
        case = "abcabcabc"
        
        self.assertEqual(
            3,
            self.solution.most_longest_word_1(case)
        )
    
    def test_2_most_longest_word_1(self):
        case = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        
        self.assertEqual(
            1,
            self.solution.most_longest_word_1(case)
        )
    
    def test_3_most_longest_word_1(self):
        case = "sttrg"
        
        self.assertEqual(
            3,
            self.solution.most_longest_word_1(case)
        )
    
    def test_4_most_longest_word_1(self):
        case = ""
        
        self.assertEqual(
            0,
            self.solution.most_longest_word_1(case)
        )
    
    def test_5_most_longest_word_1(self):
        case = "aaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        
        self.assertEqual(
            2,
            self.solution.most_longest_word_1(case)
        )


if __name__ == '__main__':
    unittest.main()