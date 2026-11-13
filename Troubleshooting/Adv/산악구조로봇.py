# 261112. 기출. 산악 구조 로봇
# PASS(20분)

"""
목표: N x N 지도가 주어진다.
    1. (0, 0)에서 (N - 1, N - 1)까지 가는 최소 연료를 구하라
    2. 높이 차의 두 배 만큼 연료가 소모된다.
    3. 같은 높이면 연료가 1 소모된다
    4. 낮은 곳이면 연료 소모가 없다.
핵심로직: 다익스트라, heap
    1. dist 배열 생성
    2. (cost, r, c) 를 heap에다가 넣는다
    3. dist[r][c] <= cost면 넘어간다
    4. 작으면 갱신하고 heap에 넣는다
"""
from heapq import heappop, heappush

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dist = [[float('inf')] * N for _ in range(N)]

    dist[0][0] = 0  # 시작값 초기화

    heap = [(0, 0, 0)]

    while heap:
        cost, r, c = heappop(heap)

        if cost > dist[r][c]:
            continue

        if (r, c) == (N - 1, N - 1):
            break

        current = grid[r][c]

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            nxt = grid[nr][nc]

            if current == nxt:
                new_cost = cost + 1
            elif current > nxt:
                new_cost = cost
            else:
                new_cost = cost + (nxt - current) * 2

            if new_cost < dist[nr][nc]:
                dist[nr][nc] = new_cost
                heappush(heap, (new_cost, nr, nc))

    print(f'#{tc} {dist[N - 1][N - 1]}')