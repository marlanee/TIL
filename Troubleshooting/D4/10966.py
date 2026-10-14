# SWEA 10966. 물놀이를 가자

# 물놀이? 재밌겠다. 

# 1차 시도: Runtime Error(15분) / 힌트 참조 PASS(30분)
# 신규 개념: Multi-source BFS
# 9. 30. 복습 필요
# 1차 복습: PASS(20분)
# 10. 7. 복습 필요 / 새로운 개념이기 때문
# 10. 15. 복습: PASS(30분)
# 졸업

# 목표: N x M 격자가 주어진다. W 또는 L 로 채워져 있다. 모든 L에서 가장 가까운 W로 이동할 때, 이동 횟수의 총합을 구하라
# 상태: dist[r][c] = 해당 육지에서 가장 가까운 물까지의 거리
# 자료구조: deque, 2차원 dist 배열, Multi-source BFS
# 핵심로직:
    # 1. 모든 W를 queue에 동시에 넣는다.
    # 2. BFS를 레벨 단위로 진행한다.
    # 3. 처음 방문하는 L의 dist를 현재 거리 d로 갱신한다.
    # 4. 갱신한 L을 queue에 넣어 다음 거리 탐색에 사용한다.
    # 5. 모든 L의 dist 합을 구한다.
# 종료 조건: queue가 빌 때

# from collections import deque

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     grid = [input() for _ in range(N)]
#     dist = [[-1] * M for _ in range(N)]

#     water = deque()
#     total = 0

#     for r in range(N):
#         for c in range(M):
#             if grid[r][c] == 'W':
#                 water.append((r, c))
#                 dist[r][c] = 0

#     while water:

#         r, c = water.popleft()  # 아주 그냥 독이 스멀스멀 퍼져나가지?

#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]

#             if 0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1:
#                 dist[nr][nc] = dist[r][c] + 1
#                 water.append((nr, nc))

#     for r in range(N):
#         for c in range(M):
#             if grid[r][c] == 'L':
#                 total += dist[r][c]

#     print(f'#{tc} {total}')

# SWEA 10966. 물놀이를 가자

# 1차 복습: PASS(20분)

# 목표: 
    # 1. W, L 로 가득한 N x M 2차원 격자가 주어진다. 각 L에서 가장 가까운 W까지 이동한다고 하자.
    # 2. 모든 L에서, W까지 도달하는 거리의 합을 구하라.
# 상태: dist = 각 L에서 W까지 도달하는 최소 거리를 담은 격자판. step = W의 좌표 리스트. next_step = 다음 BFS
# 자료구조: dist, multi-source-BFS, deque, 델타 탐색
# 핵심로직: W에서 출발하여 너비순으로 dist를 탐색 후 저장
# 종료 조건: queue가 빌 때(모든 도달 가능한 칸의 최단거리가 확정됐을 때)
# from collections import deque

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     grid = [input() for _ in range(N)]

#     dist = [[-1] * M for _ in range(N)]
#     step = deque()

#     for r in range(N):
#         for c in range(M):
#             if grid[r][c] == 'W':
#                 step.append((r, c))
#                 dist[r][c] = 0

#     while step:

#         r, c = step.popleft()

#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]

#             if 0 <= nr < N and 0 <= nc < M and dist[nr][nc] == -1:
#                 dist[nr][nc] = dist[r][c] + 1
#                 step.append((nr, nc))

#     total = 0

#     for r in range(N):
#         for c in range(M):
#             if grid[r][c] == 'L':
#                 total += dist[r][c]

#     print(f'#{tc} {total}')


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