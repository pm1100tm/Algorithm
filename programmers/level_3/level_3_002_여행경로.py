"""여행경로
https://school.programmers.co.kr/learn/courses/30/lessons/43164
"""
from collections import defaultdict
from utils import prvalue


@prvalue(print_result=True)
def solution(tickets: list[list[str]]) -> list[str]:
    graph = defaultdict(list)
    for vertex, edge in tickets:
        graph[vertex].append(edge)

    for vertex in graph:
        graph[vertex].sort()

    paths: list[list[str]] = []

    def dfs(airport: str, path: list[str], used_tickets):
        if paths:
            return

        if len(used_tickets) == len(tickets):
            paths.append(path)
            return

        next_airports = graph[airport]
        if not next_airports:
            return

        for next_airport in next_airports:
            ticket = [airport, next_airport]
            if used_tickets.count(ticket) < tickets.count(ticket):
                dfs(next_airport, path + [next_airport], used_tickets + [ticket])

    dfs("ICN", ["ICN"], [])

    if not paths:
        return []

    return paths[0]


if __name__ == '__main__':
    assert solution(
        [["ICN", "JFK"], ["ICN", "IAD"], ["JFK", "HND"], ['JFK', 'HND']]
    ) == []
    assert solution(
        [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    ) == ["ICN", "JFK", "HND", "IAD"]
    assert solution(
        [
            ["ICN", "SFO"],
            ["ICN", "ATL"],
            ["SFO", "ATL"],
            ["ATL", "ICN"],
            ["ATL", "SFO"],
        ],
    ) == ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
