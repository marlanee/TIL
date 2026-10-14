# SWEA 5653. 줄기세포배양
# 뭔놈의 줄기세포를 배양하냐.
# 1차 시도: 17:16

"""
목표: N x M 격자 내부에 줄기세포들이 주어진다. K 시간이 지난 후 살아있는 줄기세포의 수를 구하시오
상태: 
    1. time = 현재까지 지난 시간
    2. x, y, life, count = 좌표, 생명력, 목숨
자료구조: BFS, visited(세트 처리)
핵심 로직:
    1. 줄기세포들의 좌표와 생명력, 목숨을 unactivate 리스트에 담음
    2. activate 된 줄기세포를 순회하며 네 방향으로 번식함
        0. 이미 방문했다면 continue
        1. next_unactivate 딕셔너리에 번식할 줄기세포의 좌표와 생명력을 넣음
        2. activate 줄기세포들의 목숨을 1 감소시킴. 만약 0이 된다면 제거함
    3. unactivate 리스트에 있는 줄기세포들의 목숨(부화시간)을 1감소시킴. 만약 0이 된다면 activate로 이동함. 목숨도 초기화됨
    4. unactivate 리스트에 next_unactivate 딕셔너리에 있는 줄기세포들을 추가함. 만약 길이가 1보다 크다면, 생명력이 높은 줄기세포를 집어넣음

종료 조건: if time == K / 살아있는 줄기세포들의 수를 출력
"""

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = set()
    time = 0
    unactivate = deque()
    activate = deque()

    for r in range(N):
        for c in range(M):
            life = grid[r][c]
            if life >= 1:
                unactivate.append((r, c, life, life))

    print(unactivate)
