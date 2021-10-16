"""
n개의 정수를 가진 배열이 있다.
이 배열은 양의정수와 음의 정수를 모두 가지고 있다. 이제 당신은 이 배열을 좀 특별한 방법으로 정렬해야 한다.
정렬이 되고 난 후, 음의 정수는 앞쪽에 양의정수는 뒷쪽에 있어야 한다. 또한 양의정수와 음의정수의 순서에는 변함이 없어야 한다.
예. -1 1 3 -2 2 ans: -1 -2 1 3 2.
"""


''' 배열에 0 이 없을 경우: 방법 1'''
nlist_no_zero = [-1, 1, 3, -2, 2]
def special_sort_one():
    new_list = [i for i in nlist_no_zero if i < 0] + [i for i in nlist_no_zero if i > 0]
    print(new_list) # [-1, -2, 1, 3, 2]

special_sort_one()


''' 배열에 0 이 없을 경우: 방법 2 >> 버블정렬 응용'''
def special_sort_two():
    cnt = 0
    nlist = [-1, 1, 3, -2, 2]
    for i in range(len(nlist)):
        for j in range(len(nlist) - i):
            if j < len(nlist) - 1:
                if nlist[j] > 0 and nlist[j+1] < 0:
                    cnt += 1
                    k = nlist[j]
                    nlist[j] = nlist[j+1]
                    nlist[j+1] = k
    print(nlist) # [-1, -2, 1, 3, 2]
    print(cnt) # 2 (음수 값이 옮겨지는 횟수 만큼 카운팅 된다)

special_sort_two() # [-1, -2, -5, 1, 3, 2]


''' 배열에 0 이 있을 경우: '''
nlist_one = [0, -1, 1, 3, -5, -2, 2]
nlist_two = [-1, 1, 3, -5, -2, 2, 0]
def special_sort_thee(nlist):
    negative_numlist = [i for i in nlist if i < 0]
    positive_numlist = [i for i in nlist if i > 0]
    if ",".join([str(i) for i in nlist]).count("0") > 0:
        negative_numlist.append(0)

    print(negative_numlist + positive_numlist)

special_sort_thee(nlist_one) # [-1, -5, -2, 0, 1, 3, 2]
special_sort_thee(nlist_two) # [-1, -5, -2, 0, 1, 3, 2]