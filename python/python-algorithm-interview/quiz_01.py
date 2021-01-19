import collections
import re
from typing import Deque

from python.utils import CommonUtils


"""
01. 유효한 팰린드롬
주어진 문자열 팰린드롬인지 화인하기.
단, 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
"""
class PalindromeCheck:
    
    @CommonUtils.logging_time
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return False
        
        strs = []
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True
    
    def isPalindrome_by_deque(self, s: str) -> bool:
        if not s:
            return False
        
        strs: Deque = collections.deque()
        
        for char in strs:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True
    
    def isPalindrome_by_slicing(self, s: str) -> bool:
        if not s:
            return False
        
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
        

if __name__ == '__main__':
    check = PalindromeCheck()
    
    r1 = check.isPalindrome("test")
    r2 = check.isPalindrome_by_deque("as issi sa")
    r3 = check.isPalindrome_by_slicing("as issi sa")
    
    print(r1, r2, r3)
