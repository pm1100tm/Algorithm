def quiz_1_solution(record: list[str]):
    name_map = {}
    status_log = []

    for r in record:
        log = r.split()
        status, uid = log[0], log[1]
        if status != 'Change':
            status_log.append([status, uid])
        if status == 'Enter' or status == 'Change':
            name_map[uid] = log[2]

    answer = []
    for log in status_log:
        status, uid = log
        ret = f'{name_map[uid]}님이'
        if status == 'Enter':
            ret += ' 들어왔습니다.'
        elif status == 'Leave':
            ret += ' 나갔습니다.'
        answer.append(ret)

    return answer


def quiz_2_solution(people: list[int], limit: int):
    people.sort()
    left = 0
    right = len(people) - 1
    boats = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
        right -= 1
        boats += 1

    return boats


if __name__ == '__main__':
    assert (
       quiz_1_solution(
           [
               "Enter uid1234 Muzi",
               "Enter uid4567 Prodo",
               "Leave uid1234",
               "Enter uid1234 Prodo",
               "Change uid4567 Ryan"
           ]
       ) == [
           'Prodo님이 들어왔습니다.',
           'Ryan님이 들어왔습니다.',
           'Prodo님이 나갔습니다.',
           'Prodo님이 들어왔습니다.',
        ]
    )
    assert quiz_2_solution([70, 50, 80, 50], 100) == 3
    assert quiz_2_solution([70, 80, 50], 100) == 3
