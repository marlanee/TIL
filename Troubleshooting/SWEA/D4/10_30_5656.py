# SWEA 5656. 벽돌 깨기
# 1차 시도: FAIL(90분)
# 큰 방향은 구현 성공했으나 여러 기능을 연결하는 구현 실패
# 10. 8 복습 필요
# 26. 10. 27.
# SWEA 5656. 벽돌 깨기
# 1차 복습: 1시간(FAIL) -> 힌트 참조 후 3분(PASS)
# 부족한 점: 백트래킹(객체 복사) / 중력 처리
# 10. 30. 복습 필요

"""
목표: 벽돌이 들어 있는 W x H 게임판이 주어진다.
    1. 구슬을 떨어뜨려 벽돌을 깨뜨린다.
    2. 구슬은 좌, 우로만 움직이며 맨 위의 벽돌만 깨뜨릴 수 있다.
    3. 벽돌은 숫자 1~9로 표현된다.
    4. 타격을 입은 벽돌은 상하좌우로 (숫자 - 1)칸 만큼 같이 타격한다.
    5. 타격은 연쇄로 작용한다.
    6. N개의 벽돌을 떨어뜨려 최대한 많은 벽돌을 제거하고, 남은 벽돌의 개수를 구하라.
상태:
    1. count = 구슬을 떨어뜨린 횟수
    2. min_remain = 현재까지 구한 최소 남은 벽돌 개수
자료구조: DFS/백트래킹, BFS
핵심로직:
    1. 한 턴마다, 0 ~ W-1 열까지 구슬을 떨어뜨려보는 완전 탐색이 필요해 보인다.
    2. dfs 내부에 for w in range(W) 필요.
    3. dfs 재귀 호출은 딱 하나. 떨어뜨리는 것. 
    4. 떨어뜨리고 나서 연쇄 타격 후, 백트래킹
    5. count == N 이면 종료 후 최대값 갱신
    6. 가지치기: 해당 열에 벽돌이 없으면 return
종료조건: 재귀 호출이 종료되었을 때, min_remain 출력
시간 복잡도: 계산중
"""

from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(count, check_grid):
    global min_remain

    if min_remain == 0:
        return

    if count_bricks(check_grid) == 0:
        min_remain = 0
        return

    if count == N:
        min_remain = min(min_remain, count_bricks(check_grid))
        return

    for w in range(W):
        next_grid = [row[:] for row in check_grid]
        if not explosion(w, next_grid):   # 해당 열에 벽돌이 없을 경우
            continue
        dfs(count + 1, next_grid)

def count_bricks(check_grid):  # 남은 벽돌 개수 세는 함수
    count = 0
    for row in check_grid:
        count += row.count(0)

    result = H * W - count

    return result

def explosion(w, check_grid):   # 연쇄 타격 작용 계산 함수
    q = deque()

    for r in range(H):  # 초기 타격 벽돌 입력
        current = check_grid[r][w]
        if current >= 1:
            q.append((r, w, current))
            check_grid[r][w] = 0
            break

    if not q:   # 열에 아무것도 없을경우
        return False

    while q:    # 벽돌 연쇄작용
        r, c, power = q.popleft()

        for i in range(1, power):
            for d in range(4):
                nr = r + dr[d] * i
                nc = c + dc[d] * i

                if not (0 <= nr < H and 0 <= nc < W):
                    continue

                current = check_grid[nr][nc]

                if current >= 1:
                    q.append((nr, nc, current))
                    check_grid[nr][nc] = 0

    # 벽돌을 아래로 내리는 코드 구현
    for c in range(W):
        bricks = []

        for r in range(H):
            if check_grid[r][c] != 0:
                bricks.append(check_grid[r][c])

        for r in range(H - 1, -1, -1):
            if bricks:
                check_grid[r][c] = bricks.pop()
            else:
                check_grid[r][c] = 0

    return check_grid

T = int(input())
for tc in range(1, T + 1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]

    min_remain = W * H  # 최솟값 러프하게 설정

    dfs(0, grid)

    print(f'#{tc} {min_remain}')
    
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

# from collections import deque
# from copy import deepcopy

# def dfs(count):
#     global min_result, grid

#     if min_result == 0:
#         return

#     if count == N:
#         check = W * H
#         for row in grid:
#             check -= row.count(0)

#         min_result = min(min_result, check)
#         return

#     for col in range(W):
#         backup = deepcopy(grid)

#         for row in range(H):
#             brick = grid[row][col]

#             if brick == 0:
#                 continue

#             bricks = deque([(row, col, brick)])
#             grid[row][col] = 0

#             while bricks:
#                 r, c, power = bricks.popleft()

#                 for i in range(4):
#                     for distance in range(1, power):
#                         nr = r + dr[i] * distance
#                         nc = c + dc[i] * distance

#                         if not (0 <= nr < H and 0 <= nc < W):
#                             break

#                         next_power = grid[nr][nc]

#                         if next_power == 0:
#                             continue

#                         grid[nr][nc] = 0

#                         if next_power > 1:
#                             bricks.append((nr, nc, next_power))

#             break

#         for c in range(W):
#             remaining = [
#                 grid[r][c]
#                 for r in range(H)
#                 if grid[r][c] != 0
#             ]

#             column = [0] * (H - len(remaining)) + remaining

#             for r in range(H):
#                 grid[r][c] = column[r]

#         dfs(count + 1)

#         grid = backup

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# T = int(input())
# for tc in range(1, T + 1):
#     N, W, H = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(H)]

#     min_result = W * H - N

#     dfs(0)

#     print(f'#{tc} {min_result}')