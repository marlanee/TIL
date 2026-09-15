# A형 문제. 로봇 개척자

# 1차 시도: 10:33

# 목표
#   1. N x N 행렬이 주어진다. 로봇이 돌아다니며 씨(2)를 뿌리는데, 5일 뒤에 수확이 가능해진다.
#   2. 산(1)에 막히면 갈 수 없다. 로봇은 씨앗을 뿌린 뒤, [우, 상, 좌, 하] 순서로 이동한다.
#   3. 씨앗(2~6)인 곳에도 갈 수 없다. 오로지 농지(0) 또는 곡식(7)만 갈 수 있다.
#   4. 이 행렬에서, 로봇의 위치와 시작 방향을 임의로 정할 때 곡식의 최대 수확량을 구하시오
# 상태: (r, c) = 로봇의 시작 위치. total = 수확 횟수, day = 동작 일 수, start = 출발 가능한 지점을 관리하는 리스트
# 자료구조: BFS
# 핵심 로직
#   1. r, c부터 grid를 순회하면서 total을 갱신하는거다.
#   2. 반복문이 모두 종료되었을 때, 수확 횟수를 출력
#   3. 출발 가능한 r, c 위치를 저장해놓는 start 리스트를 만들자.

import copy

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())    # N은 행렬의 크기, M은 로봇의 동작 일수
    grid = [list(map(int, input().split())) for _ in range(N)]

    total = 0
    start = []

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                start.append((r, c))    # 구했다.

    for sr, sc in start:
        for start_dir in range(4):
            r, c = sr, sc
            day = 0
            target = 0
            ngrid = copy.deepcopy(grid)
            direction = start_dir

            while day < M:
                for row in range(N):
                    for col in range(N):
                        if 1 < ngrid[row][col] < 7:
                            ngrid[row][col] += 1
                ngrid[r][c] = 2

                priority = [(direction -1) % 4, direction, (direction + 1) % 4, (direction + 2) % 4]
                for d in priority:
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if ngrid[nr][nc] == 0:
                        r, c = nr, nc
                        direction = d
                        break
                    elif ngrid[nr][nc] == 7:
                        target += 1
                        direction = d
                        r, c = nr, nc
                        break
                day += 1

            if target > total:
                total = target

    print(f'#{tc} {total}')