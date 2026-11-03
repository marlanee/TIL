# 26. 10. 30.
# SWEA 7793. 오! 나의 여신님
# 1차 시도: 코드 작성(40분) 디버깅(20분)
# 졸업

"""
목표: N x M 지도가 주어진다.
    1. BFS로 확장되는 악마의 손아귀를 피해야 한다
    2. 최단 시간으로 여신 S 한테 가야한다. 
    3. 이 때의 시간을 구하라
상태:
자료구조: 델타 이동, DFS/백트래킹, BFS, visited
핵심로직:
    1. 수연이의 위치에서 DFS 시작
    2. 악마 손아귀 발동. BFS
    3. 상하좌우 4방향 중 하나로 이동 / 돌, 손아귀면 이동 불가 continue
    4. dfs 재귀호출
    5. 간 길을 다시 돌아올 일은 없을테니, visited 처리를 하자
종료조건:
시간복잡도:
"""

from collections import deque
from copy import deepcopy

def dfs(r, c, time, dfs_grid, devil_q):
    global min_time

    next_grid = [row[:] for row in dfs_grid] # 원본에 영향 안 가도록 복사 구현 / 백트래킹

    q = deepcopy(devil_q) # 백트래킹을 위해 저장

    q = devil_power(next_grid, q)

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if not (0 <= nr < N and 0 <= nc < M):
            continue

        if dfs_grid[nr][nc] == 'D':
            if not min_time.isdecimal():
                min_time = time + 1
            elif min_time.isdecimal():
                min_time = min(min_time, time + 1)
            return

        if dfs_grid[nr][nc] == '.' and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, time + 1, next_grid, q)
            visited[nr][nc] = False

def devil_power(devil_grid, q):

    next_q = deque()

    while q:
        r, c = q.pop()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if devil_grid[nr][nc] == '.':
                devil_grid[nr][nc] = '*'
                next_q.append((nr, nc))

    return next_q

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]

    for r in range(N):  # 여신, 수연, 악마 위치 찾기
        for c in range(M):
            if grid[r][c] == 'S':
                suyeon_r, suyeon_c = r, c
                grid[r][c] = '.'
                visited[r][c] = True
            elif grid[r][c] == 'D':
                goddess_r, goddess_c = r, c
            elif grid[r][c] == '*':
                devil_r, devil_c = r, c

    min_time = 'GAME OVER'
    devil_q = deque([(devil_r, devil_c)])

    dfs(suyeon_r, suyeon_c, 0, grid, devil_q)

    print(f'#{tc} {min_time}')