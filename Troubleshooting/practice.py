# SWEA 10966. 물놀이를 가자
# 10. 15. 복습: PASS(30분)
# 졸업

"""
목표: N x M 지도가 주어진다. 물이면 W, 땅이면 L로 지도에 표기되어 있다.
    1. 각각의 땅 L에서 가장 가까운 물 W로 가는 거리를 구하고
    2. 그 거리의 총합을 구하라
상태: 
    1. water = 물의 좌표를 담는 리스트, 
    2. dist = L에서 W 까지 가는 최소 거리를 담는 격자
    3. length = 거리
    4. next_water = 물의 다음 좌표 리스트
자료구조: Multi_source BFS, 델타 이동
핵심 로직: 
    1. while water:
    2. water을 순회하며 다음 좌표를 4방향으로 탐색
        0. dist[nr][nc] =< length면 continue
        1. dist[nr][nc] = length
        2. 탐색한 좌표는 next_water 리스트에 집어넣음
    3. length를 1 증가시킴. water = next_water로 갱신함
종료 조건: water가 비었을 때, dist를 순회하며 이동횟수의 합 출력
"""

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]

    water = []
    dist = [[float('inf')] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if grid[r][c] == 'W':
                water.append((r, c))
                dist[r][c] = -1

    length = 1

    while water:
        next_water = []
        for r, c in water:
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if not (0 <= nr < N and 0 <= nc < M):
                    continue

                if dist[nr][nc] <= length:
                    continue

                dist[nr][nc] = length
                next_water.append((nr, nc))

        length += 1
        water = next_water

    result = 0
    for r in range(N):
        for c in range(M):
            current = dist[r][c]
            if current > 0:
                result += current

    print(f'#{tc} {result}')