"""
문제 설명
-금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력.
대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표)등 또한 무시한다.
paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ['hit']
"""
import re
import collections
import pytest

from typing import List


class CountUtil:

    def get_clear_str_list(self, statement: str, ban_list: List[str]) -> List[str]:
        return [
            word for word in re.sub(r'[^\w]', ' ', statement)
                .lower().split() if word not in ban_list
        ]

    def solution_one(self, word_list: List[str]) -> str or None:
        counter: dict = collections.defaultdict(int)
        for word in word_list:
            counter[word] += 1
        return max(counter, key=counter.get)

    def solution_two(self, word_list: List[str]) -> str or None:
        counts = collections.Counter(word_list)
        return counts.most_common(1)[0][0]


if __name__ == "__main__":
    paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
    banned    = ['hit']
    
    count_util = CountUtil()
    
    solution_one_result = count_util.solution_one(
        count_util.get_clear_str_list(
            paragraph,
            banned
        )
    )
    print(solution_one_result)

    solution_two_result = count_util.solution_two(
        count_util.get_clear_str_list(
            paragraph,
            banned
        )
    )
    print(solution_two_result)


@pytest.fixture()
def statements():
    return """
    South Korea’s plan to step into a phased recovery back to normal life in November is gaining support with positive clinical test results of an experimental COVID-19 oral medication overseas.
Leading global drugmaker Merck & Co announced Friday that its experimental antiviral pill dubbed molnupiravir was shown to halve the chances of hospitalization or death for those infected with COVID-19.
Merck and its partner Ridgeback Biotherapeutics reported that 7.3 percent of patients who received molnupiravir died or were either hospitalized by 29 days after receiving the oral antiviral medicine, as opposed to 14.1 percent for placebo-administered patients.
No COVID-19 patient died after taking molnupiravir, compared to 8 deaths reported from the placebo group, the firms added.
The pill works by blocking the virus from replicating, as does some Acquired Immune Deficiency Syndrome drugs by inhibiting the replication of human immunodeficiency virus. If approved, it would be the first oral antiviral treatment against COVID-19 on the market.
Merck is preparing to file for emergency use authorization from the US Food and Drug Administration as soon as possible as its first step of gaining regulatory approvals from the global market.
The positive trial results from Merck champions Korean authorities’ plan to ease COVID-19 restrictions starting November and treat COVID-19 more like seasonal influenza.
Continued struggles of small business owners and declining consumer sentiment from restrictive social distancing rules have caused authorities to discuss easing anti-virus measures and “live with the coronavirus.”
The government announced earlier the new scheme will kick off when around 80 percent of adults are fully vaccinated. As of Friday’s end, 51.8 percent of South Korea’s population have been fully vaccinated, and 77.1 percent have received their first shots of COVID-19 vaccines.
As experts have pointed out securing effective, easily accessible COVID-19 treatment is key to normalization, the government has been looking to sign a deal with Merck to buy its oral treatment for 18,000 people. The government also plans to set aside a portion of its next year’s budget to buy enough doses for 20,000 people in 2022.
The Korea Disease Control and Prevention Agency is given 41.7 billion won to buy COVID-19 treatments next year, and it was known that Merck’s treatment costs about 900,000 won per person.
Yet experts have voiced concerns that the Korean government is purchasing far too fewer doses of COVID-19 treatments even though they will be critical in carrying out normalization efforts. They forecast that competition to buy COVID-19 treatments will get more intense later on, which is why Korea should stay upfront and purchase as many as possible in the early stage.
Merck said while announcing the clinical trial results that it plans to manufacture enough doses for 10 million people by the end of this year, 1.7 million of which already contracted to be provided to the US government.
"""

def test_quiz004_case_001(statements):
    test_count_util: CountUtil = CountUtil()
    result = test_count_util.solution_one(
        test_count_util.get_clear_str_list(
            statements, ['Korean']
        )
    )
    assert 'the' == result

def test_quiz004_case_002(statements):
    test_count_util: CountUtil = CountUtil()
    result = test_count_util.solution_two(
        test_count_util.get_clear_str_list(
            statements, ['the']
        )
    )
    assert 'to' == result

def test_quiz004_case_003(statements):
    test_count_util: CountUtil = CountUtil()
    result = test_count_util.solution_one(
        test_count_util.get_clear_str_list(
            statements, ['the', 'to']
        )
    )
    assert 'of' == result

def test_quiz004_case_004(statements):
    test_count_util: CountUtil = CountUtil()
    result = test_count_util.solution_one(
        test_count_util.get_clear_str_list(
            statements, ['the', 'to', 'of']
        )
    )
    assert 'covid' == result

def test_quiz004_case_005(statements):
    test_count_util: CountUtil = CountUtil()
    result = test_count_util.solution_one(
        test_count_util.get_clear_str_list(
            statements, ['the', 'to', 'of', 'covid']
        )
    )
    assert '19' == result
