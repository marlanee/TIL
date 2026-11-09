# 261109. SWEA 5656. 벽돌 깨기
# 3차 시도: PASS(25분)
# 졸업
"""
목표: W x H 게임판이 주어진다.
    1. N개의 구슬을 떨어뜨려 가장 많은 벽돌을 부수려고 한다
    2. 남은 벽돌의 개수를 구하라.
    3. 벽돌에 새겨진 숫자 - 1 만큼 상하좌우로 연쇄 폭발한다.
핵심로직: DFS / 백트래킹
    1. 각 열마다 구슬을 떨어뜨리는 완전 탐색 로직 구현
    2. 열을 선택 후 연쇄 폭발 작용
    3. 연쇄 폭발 후 중력 작용
    4. dfs 호출
    5. 남은 구슬이 없으면 return
시간복잡도: O(W^N * WH)
"""

from collections import deque

def dfs(count, grid):
    global total
    if total == 0:
        return
    if count == N:
        # 남은 구슬 세는 코드
        result = count_left(grid)
        total = min(total, result)
        return

    # 구슬 선택하는 코드
    for col in range(W):
        next_grid = [row[:] for row in grid]

        # 연쇄 폭발 코드
        explosion(col, next_grid)

        # 중력 코드
        gravity(next_grid)

        dfs(count + 1, next_grid)

def gravity(grid):
    for col in range(W):
        before = []
        for row in range(H): 
            current = grid[row][col]
            if current:
                before.append(current)

        for row in range(H - 1, -1, -1):
            grid[row][col] = before.pop() if before else 0

def count_left(grid):
    total = W * H
    for row in grid:
        total -= row.count(0)

    return total

def explosion(col, grid):
    for row in range(H):
        if grid[row][col] != 0:
            break
    else:
        return

    q = deque()
    q.append((row, col, grid[row][col]))
    grid[row][col] = 0

    while q:
        r, c, power = q.popleft()

        for d in range(4):
            for p in range(1, power):
                nr = r + dr[d] * p
                nc = c + dc[d] * p

                if not (0 <= nr < H and 0 <= nc < W):
                    break

                if grid[nr][nc] != 0:
                    q.append((nr, nc, grid[nr][nc]))
                    grid[nr][nc] = 0


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1,  T + 1):
    N, W, H = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    total = W * H

    dfs(0, grid)

    print(f'#{tc} {total}')