import collections
import unittest
from typing import List

from utils import CommonUtils


class Solution:
    """ 완주하지 못한 선수
    수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
    마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
    완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.
    
    제한사항
        마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
        completion의 길이는 participant의 길이보다 1 작습니다.
        참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
        참가자 중에는 동명이인이 있을 수 있습니다.
    
    participant
        case 1 - [leo, kiki, eden]
        case 2 - [marina, josipa, nikola, vinko, filipa]
        case 3 - [mislav, stanko, mislav, ana]
    
    completion
        case 1 - [eden, kiki]
        case 2 - [josipa, filipa, marina, nikola]
        case 3 - [stanko, ana, mislav]
    
    return
        "leo"       : leo는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
        "vinko"     : vinko는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.
        "mislav"    : mislav는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
    """
    
    def my_solution_one(self, participant: List[str], completion: List[str]) -> str:
        """ 효율성 테스트에서 통과하지 못함 """
        
        for c in completion:
            if c in participant:
                participant.pop(participant.index(c))
        
        return "".join(participant)
    
    def my_solution_two(self, participant: List[str], completion: List[str]) -> str:
        participant.sort()
        completion.sort()
        
        for i in range(len(completion)):
            if completion[i] != participant[i]:
                return participant[i]
        
        return participant[-1]
    
    def best_solution_i_think(self, participant: List[str], completion: List[str]) -> str:
        answer = collections.Counter(participant) - collections.Counter(completion)
        return list(answer.keys())[0]
    
    def other_solution_one(self, participant: List[str], completion: List[str]) -> str:
        temp = 0
        dic = {}
        
        for part in participant:
            dic[hash(part)] = part
            temp += int(hash(part))
            
        for com in completion:
            temp -= hash(com)
            
        answer = dic[temp]
        
        return answer


class TestSolution(unittest.TestCase):
    
    def setUp(self) -> None:
        self.solution = Solution()
        
        self.case_one_participant   = ["leo", "kiki", "eden"]
        self.case_two_participant   = ["marina", "josipa", "nikola", "vinko", "filipa"]
        self.case_three_participant = ["mislav", "stanko", "mislav", "ana"]
        
        self.case_one_completion   = ["eden", "kiki"]
        self.case_two_completion   = ["josipa", "filipa", "marina", "nikola"]
        self.case_three_completion = ["stanko", "ana", "mislav"]
        
        self.case_one_result   = "leo"
        self.case_two_result   = "vinko"
        self.case_three_result = "mislav"
        
    @CommonUtils.logging_time
    def test_my_solution_two(self):
        
        result_one = self.solution.my_solution_two(
            self.case_one_participant,
            self.case_one_completion
        )

        result_two = self.solution.my_solution_two(
            self.case_two_participant,
            self.case_two_completion
        )
        
        result_three = self.solution.my_solution_two(
            self.case_three_participant,
            self.case_three_completion
        )
        
        self.assertEqual(self.case_one_result, result_one)
        self.assertEqual(self.case_two_result, result_two)
        self.assertEqual(self.case_three_result, result_three)
    
    @CommonUtils.logging_time
    def test_best_solution_i_think(self):
        result_one = self.solution.best_solution_i_think(
            self.case_one_participant,
            self.case_one_completion
        )
        
        result_two = self.solution.best_solution_i_think(
            self.case_two_participant,
            self.case_two_completion
        )
        
        result_three = self.solution.best_solution_i_think(
            self.case_three_participant,
            self.case_three_completion
        )
        
        self.assertEqual(self.case_one_result, result_one)
        self.assertEqual(self.case_two_result, result_two)
        self.assertEqual(self.case_three_result, result_three)
    
    @CommonUtils.logging_time
    def test_other_solution_one(self):
        result_one = self.solution.other_solution_one(
            self.case_one_participant,
            self.case_one_completion
        )
        
        result_two = self.solution.other_solution_one(
            self.case_two_participant,
            self.case_two_completion
        )
        
        result_three = self.solution.other_solution_one(
            self.case_three_participant,
            self.case_three_completion
        )
        
        self.assertEqual(self.case_one_result, result_one)
        self.assertEqual(self.case_two_result, result_two)
        self.assertEqual(self.case_three_result, result_three)


if __name__ == '__main__':
    unittest.main()


# Working Time[test_best_solution_i_think]: 9.179115295410156e-05 sec
# Working Time[test_my_solution_two]: 1.7881393432617188e-05 sec
# Working Time[test_other_solution_one]: 1.9788742065429688e-05 sec
