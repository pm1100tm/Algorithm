"""[1차] 캐시
https://school.programmers.co.kr/learn/courses/30/lessons/17680
"""
from utils import prvalue

from collections import OrderedDict, deque


class LimitedDict(OrderedDict):
    def __init__(self, limit):
        self.limit = limit
        super().__init__()

    def __setitem__(self, key: str, value):
        if self.limit == 0:
            return
        if key in self:
            # Remove the existing item before re-adding it to update the order
            del self[key]
        elif len(self) >= self.limit:
            # Remove the first item (oldest)
            self.popitem(last=False)
        super().__setitem__(key, value)


@prvalue(print_result=True)
def solution(cache_size: int, cities: list[str]) -> int:
    TIME_CACHE_MISS = 5
    TIME_CACHE_HITS = 1

    cal = 0
    cache = LimitedDict(limit=cache_size)
    for city in cities:
        name = city.lower()
        if name not in cache:
            cal += TIME_CACHE_MISS
        else:
            cal += TIME_CACHE_HITS

        cache[name] = 0

    return cal


def solution2(cache_size: int, cities: list[str]) -> int:
    buffer = deque(maxlen=cache_size)
    time_to_take = 0

    if not cache_size:
        return len(cities) * 5

    for c in cities:
        _c = c.lower()
        if _c in buffer:
            buffer.remove(_c)
            buffer.append(_c)
            time_to_take += 1
        else:
            buffer.append(_c)
            time_to_take += 5

    return time_to_take


# Node, LRUCache 클래스로 head, tail 개념으로 구현하는 방법(추후 정리 필요)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # maps key to Node
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add(self, node):
        # always add the new node right after head
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            # remove from the end
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


if __name__ == '__main__':
    assert solution(
        3,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
        ]
    ) == 50
    assert solution(
        3,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "Jeju",
            "Pangyo",
            "Seoul",
            "Jeju",
            "Pangyo",
            "Seoul",
        ]
    ) == 21
    assert solution(
        2,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ]
    ) == 60
    assert solution(
        5,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA", "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ]
    ) == 52
    assert solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]) == 16
    assert solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25
    assert solution(1, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]) == 25
    assert solution(1, ["Jeju", "jeju", "Seoul", "seoul", "LA"]) == 17
    assert solution(3, ["Jeju", "jeju", "jeju", "jeju", "LA", "lA"]) == 14
    assert solution(2, ["a", "b", "a", "a", "b"]) == 13
    assert solution(3, ["A", "B", "C", "A", "D", "G", "A"]) == 27
