""" 문제 설명

매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다.
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은
두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
    scoville의 길이는 2 이상 1,000,000 이하입니다.
    K는 0 이상 1,000,000,000 이하입니다.
    scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
    모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

입출력 예
    scoville : [1, 2, 3, 9, 10, 12]
    K        : 7
    return   : 2

입출력 예 설명
    스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
    새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
    가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

    스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
    새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
    가진 음식의 스코빌 지수 = [13, 9, 10, 12]

    모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
"""
def my_answer(scoville, K):
    answer = 0
    mixed_value = 0
    
    if min(scoville) >= K:
        return -1
    
    array_scovile = sorted(scoville, reverse=True)
    
    while mixed_value < K:
        min_first = array_scovile.pop()
        min_second = array_scovile.pop()
        
        mixed_value = min_first + (min_second * 2)
        answer += 1
        if K <= mixed_value:
            break
        
        array_scovile.append(mixed_value)
    
    return answer


import heapq
def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    mix_count = 0
    
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        except IndexError:
            return -1
        mix_count += 1
    
    return mix_count


scoville = [1, 2, 3, 9, 10, 12]
K = 7
r = solution(scoville, K)
print(r)


""" 문제 설명
0과 1로 이루어진 2n x 2n 크기의 2차원 정수 배열 arr이 있습니다.
당신은 이 arr을 쿼드 트리와 같은 방식으로 압축하고자 합니다. 구체적인 방식은 다음과 같습니다.

당신이 압축하고자 하는 특정 영역을 S라고 정의합니다.
만약 S 내부에 있는 모든 수가 같은 값이라면, S를 해당 수 하나로 압축시킵니다.

그렇지 않다면, S를 정확히 4개의 균일한 정사각형 영역(입출력 예를 참고해주시기 바랍니다.)으로 쪼갠 뒤,
각 정사각형 영역에 대해 같은 방식의 압축을 시도합니다.

arr이 매개변수로 주어집니다. 위와 같은 방식으로 arr을 압축했을 때,
배열에 최종적으로 남는 0의 개수와 1의 개수를 배열에 담아서 return 하도록 solution 함수를 완성해주세요.

제한사항
    arr의 행의 개수는 1 이상 1024 이하이며, 2의 거듭 제곱수 형태를 하고 있습니다. 즉, arr의 행의 개수는 1, 2, 4, 8, ..., 1024 중 하나입니다.
    arr의 각 행의 길이는 arr의 행의 개수와 같습니다. 즉, arr은 정사각형 배열입니다.
    arr의 각 행에 있는 모든 값은 0 또는 1 입니다.

입출력 예
[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
>> [4, 9]

[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],
[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
>> [10, 15]
"""
def too_hard():
    pass
















