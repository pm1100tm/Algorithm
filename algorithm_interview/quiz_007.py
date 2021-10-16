"""
타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴
"""
import pytest
import collections

from typing import List


class TargetIndex:
    
    @classmethod
    def my_solution_one(cls, number_list: List[int], target_number: int) -> (int, int):
        answer = []
        for i in range(len(number_list)):
            temp = target_number - number_list[i]
            
            for j in range(i + 1, len(number_list)):
                if temp == number_list[j]:
                    answer.append(i)
                    answer.append(number_list.index(number_list[j]))
                    return tuple(answer)
        
        return 0, 0
    
    @classmethod
    def my_solution_two(cls, number_list: List[int], target_number: int) -> (int, int):
        for i, n in enumerate(number_list):
            number = target_number - n
            
            if number in number_list[i+1:]:
                return i, number_list[i+1:].index(number) + 1
        
        return 0, 0
