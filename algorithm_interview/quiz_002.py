"""
02. 문자열 뒤집기
문자열을 뒤집는 함수를 작성하라.
입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
"""
from typing       import List
from utils import CommonUtils


class ReverseStr:
    
    @CommonUtils.logging_time
    def reverse_by_two_pointer(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left  += 1
            right -= 1
    
    @CommonUtils.logging_time
    def reverse_by_list_method(self, s: List[str]) -> None:
        s.reverse()
    
    @CommonUtils.logging_time
    def reverse_by_slice(self, s: List[str]) -> None:
        s = s[::-1]
    

if __name__ == "__main__":
    revers_str = ReverseStr()
    
    revers_str.reverse_by_two_pointer(['a', 'b', 'c', 'd', 'e'])
    revers_str.reverse_by_list_method(['a', 'b', 'c', 'd', 'e'])
    revers_str.reverse_by_slice(['a', 'b', 'c', 'd', 'e'])
