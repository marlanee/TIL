# 261105. SWEA 1907 모래성 쌓기
# 1차 시도: 30분(Runtime Error) + 20분(힌트 참조 후 PASS)
# 학습 내용: BFS, visited
# 11. 12. 복습 필요
"""
목표: H x W 의 문자열이 주어진다.
    1. 모래와 빈 땅이 주어진다.
    2. 숫자를 기준으로, 파도가 칠 때, 8방향에 빈 땅이 숫자보다 크거나 같다면 빈 땅으로 변한다.
    3. 모래성의 형태가 변하지 않는 최소 파도의 횟수를 구하라
핵심로직:
    1. 모래의 좌표와 튼튼함을 담은 리스트를 만든다.
    2. 하나씩 빼서 8방향을 확인한다.
        1. 만약 빈 땅이 숫자보다 크거나 같으면 빈 땅으로 변화시킨다.
        2. next_sand에 넣지 않는다
"""
from collections import deque

dr = [1, -1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, 1, -1, -1, 1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    empty_count = [[0] * W for _ in range(H)]
    queued = [[False] * W for _ in range(H)]

    q = deque()

    for r in range(H):
        for c in range(W):
            power = grid[r][c]
            if power.isnumeric():

                for d in range(8):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if grid[nr][nc] == '.':
                        empty_count[r][c] += 1

                if int(power) <= empty_count[r][c]:
                    queued[r][c] = True
                    q.append((r, c))

    total_wave = 0

    while q:
        for _ in range(len(q)):
            r, c = q.popleft()

            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]

                if queued[nr][nc]:
                    continue

                if grid[nr][nc] != '.':
                    empty_count[nr][nc] += 1
                    if int(grid[nr][nc]) <= empty_count[nr][nc]:
                        queued[nr][nc] = True
                        q.append((nr, nc))

            grid[r][c] = '.'

        total_wave += 1

    print(f'#{tc} {total_wave}')