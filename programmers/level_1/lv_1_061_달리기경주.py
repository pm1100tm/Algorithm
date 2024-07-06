"""달리기 경주
https://school.programmers.co.kr/learn/courses/30/lessons/178871
"""
from utils import prvalue


@prvalue(print_result=True)
def solution(players: list[str], callings: list[str]):
    """
    시간 초과: case 9~13
    문제는 아래의 코드에 있다.
    - index = players.index(called_name)
    players 리스트와 called_name 리스트의 길이가 길어질수록, 매번 index 값을 찾는 것은 오버헤드를
    발생시킨다. (index 메서드는 O(n))
    players 가 n 이고 called_name 이 m 이라면, 각각의 called_name 의 index 값을 찾는 것의
    시간복잡도는 O(n * m) 이다.
    """
    for called_name in callings:
        index = players.index(called_name)
        players[index - 1], players[index] = players[index], players[index - 1]

    return players


@prvalue(print_result=True)
def solution2(players: list[str], callings: list[str]):
    players_rank: dict = {p: i for i , p in enumerate(players)}

    for player_name in callings:
        rank: int = players_rank[player_name]
        if rank <= 0:
            continue

        # save player in front temporary
        player_name_in_front = players[rank - 1]

        # swap
        players[rank - 1], players[rank] = players[rank], players[rank - 1]

        # update player_rank with player_name
        players_rank[player_name] -= 1
        players_rank[player_name_in_front] += 1

    player_name_and_rank = sorted(players_rank.items(), key=lambda x: x[1])

    return [player_name for (player_name, rank) in player_name_and_rank]


if __name__ == '__main__':
    assert solution2(
        ["mumu", "soe", "poe", "kai", "mine"],
        ["kai", "kai", "mine", "mine"],
    ) == ["mumu", "kai", "mine", "soe", "poe"]
