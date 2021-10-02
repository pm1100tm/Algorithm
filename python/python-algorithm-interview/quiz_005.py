"""
문제 설명
문자열 배열을 받아 에너그램 단위로 그룹핑
['eat', 'tea', 'ate', 'nat', 'bat']
"""
import collections
from typing import List


class GroupingEnneagram:
    
    def arrange_fn(self, s):
        return s[0], s[-1]
    
    def arrange_grouping_solution(self, str_list: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for word in str_list:
            anagrams[''.join(sorted(word))].append(word)
        
        for anagram in anagrams.values():
            anagram.sort()
        
        return list(anagrams.values())
    
    def arrange_grouping_one(self, str_list: List[str]) -> List[List[str]]:
        enneagram_dict = collections.defaultdict()
        for word in str_list:
            enneagram_dict[''.join(sorted(word))] = []
        
        for word in str_list:
            if ''.join(sorted(word)) in enneagram_dict:
                enneagram_dict[''.join(sorted(word))].append(word)
                enneagram_dict[''.join(sorted(word))].sort()
        
        return list(enneagram_dict.values())


if __name__ == '__main__':
    anagram_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    
    grouping_enneagram               = GroupingEnneagram()
    result_arrange_grouping_one      = grouping_enneagram.arrange_grouping_one(anagram_list)
    result_arrange_grouping_solution = grouping_enneagram.arrange_grouping_solution(anagram_list)
    
    print(result_arrange_grouping_one)
    print(result_arrange_grouping_solution)
