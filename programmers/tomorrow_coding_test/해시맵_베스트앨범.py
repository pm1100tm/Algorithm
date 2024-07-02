"""베스트앨범
https://school.programmers.co.kr/tryouts/85919/challenges?language=python3
"""
from collections import defaultdict


def solution(genres, plays):
    song_by_genres_map = defaultdict(lambda: {'count': 0, 'songs': []})
    for i, (genre, play_count) in enumerate(zip(genres, plays)):
        song_by_genres_map[genre]['count'] += play_count
        song_by_genres_map[genre]['songs'].append({
            'pk': i,
            'play_count': play_count
        })

    answer = []
    for genre, play_list in sorted(
        song_by_genres_map.items(),
        key=lambda item: item[1]['count'],
        reverse=True
    ):
        sorted_songs = sorted(
            play_list['songs'],
            key=lambda x: (x['play_count'], -x['pk']),
            reverse=True
        )[:2]
        for s in sorted_songs:
            answer.append(s['pk'])

    return answer


if __name__ == '__main__':
    solution(
        ["classic", "pop", "classic", "classic", "pop"],
        [500, 600, 150, 800, 2500],
    )
