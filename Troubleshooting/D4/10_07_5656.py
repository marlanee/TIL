# SWEA 5656. 벽돌 깨기
# 1차 시도: FAIL(90분)
# 큰 방향은 구현 성공했으나 여러 기능을 연결하는 구현 실패
# 10. 8 복습 필요

"""
목표: 
    1. W x H의 2차원 벽돌 게임판이 주어진다.
    2. 공을 N 번 떨어뜨려 가장 많은 벽돌을 부수고, 남은 벽돌의 개수를 구해라.
상태: min_result = 최소 벽돌 수 / count = 구슬을 쏜 횟수 / col = 떨어뜨릴 구슬의 위치
자료구조: DFS / 백트래킹 / 델타 이동 / BFS
핵심 로직:
    1. 0부터 W - 1까지 공을 떨어뜨리는 경우의 수를 모두 탐색한다.
    2. 공을 떨어뜨린 후 남은 벽돌의 상태를 변경한다
    3. dfs(col, count + 1) 재귀 호출 후 백트래킹
    4. count == N 일 경우 남은 벽돌 수를 갱신한다.
종료 조건: 재귀 호출이 종료되었을 때, 최솟값 출력
"""
# from collections import deque
# from copy import deepcopy

# def dfs(col, count):
#     global min_result, grid

#     if count == N:
#         check = W * H
#         for row in grid:
#             check -= row.count(0)

#         min_result = min(min_result, check)
#         return

#     if col == W:
#         return

#     dfs(col + 1, count)

#     for row in range(H):
#         brick = grid[row][col]

#         if brick == 1:
#             grid[row][col] = 0
#             break

#         if brick > 1:
#             bricks = deque([(row, col)])

#             while bricks:
#                 r, c = bricks.popleft()

#                 for i in range(4):
#                     nr, nc = r, c

#                     for _ in range(grid[r][c] - 1):
#                         nr = nr + dr[i]
#                         nc = nc + dc[i]

#                         if 0 <= nr < H and 0 <= nc < W:

#                             if grid[nr][nc] == 1:
#                                 grid[nr][nc] = 0
#                             elif grid[nr][nc] > 1:
#                                 bricks.append((nr, nc))

#                 grid[r][c] = 0
                        
#             break

#     for r in range(H - 1, 0, -1):
#         for c in range(W):
#             if grid[r][c] == 0 and grid[r - 1][c] != 0:
#                 grid[r][c] = grid[r - 1][c]
#                 grid[r - 1][c] = 0

#     dfs(col, count + 1)

#     grid = original_grid


# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# T = int(input())
# for tc in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(H)]
#     original_grid = deepcopy(grid)

#     min_result = W * H - N

#     dfs(0, 0)

#     print(f'#{tc} {min_result}')

# 아래는 Gpt의 힌트 코드다.

from collections import deque
from copy import deepcopy

def dfs(count):
    global min_result, grid

    if min_result == 0:
        return

    if count == N:
        check = W * H
        for row in grid:
            check -= row.count(0)

        min_result = min(min_result, check)
        return

    for col in range(W):
        backup = deepcopy(grid)

        for row in range(H):
            brick = grid[row][col]

            if brick == 0:
                continue

            bricks = deque([(row, col, brick)])
            grid[row][col] = 0

            while bricks:
                r, c, power = bricks.popleft()

                for i in range(4):
                    for distance in range(1, power):
                        nr = r + dr[i] * distance
                        nc = c + dc[i] * distance

                        if not (0 <= nr < H and 0 <= nc < W):
                            break

                        next_power = grid[nr][nc]

                        if next_power == 0:
                            continue

                        grid[nr][nc] = 0

                        if next_power > 1:
                            bricks.append((nr, nc, next_power))

            break

        for c in range(W):
            remaining = [
                grid[r][c]
                for r in range(H)
                if grid[r][c] != 0
            ]

            column = [0] * (H - len(remaining)) + remaining

            for r in range(H):
                grid[r][c] = column[r]

        dfs(count + 1)

        grid = backup

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    min_result = W * H - N

    dfs(0)

    print(f'#{tc} {min_result}')