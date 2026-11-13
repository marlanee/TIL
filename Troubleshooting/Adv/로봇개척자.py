# 261113. 기출. 로봇 개척자.
# 1차 시도: FAIL(90분)

"""
목표: N x N 행성이 있다.
    1. 임의의 농지에 씨를 심은 수를 k 라고 할 때,
    2. 농지에 씨를 심으면 3 + k일에 곡식이 열린다.
    3. 로봇이 곡물을 수확한다.
        1. 오전에 아래의 작업 중 하나를 수행한다
            1. 현재 농지가 빈 농지이고, 다음 농지로 이동할 수 있으면 씨를 심는다.
            2. 현재 농지에 곡식이 열린 경우 수확한다. 수확하면 농지는 텅 빈다.
        2. 오후에는, 상하좌우중 한 곳으로 이동한다.
            1. 빈 농지 또는 곡식이 열린 농지로만 이동 가능하다.
            2. 이동 가능한 곳이 여러 개인 경우, (로봇의 방향 기준)우하좌상 순서로 우선 이동한다
            3. 이동 불가시 현 위치에 머무른다.
    4. M일동안 곡식을 가장 많이 수확할 수 있는 시작 위치와 방향을 찾고 수확 횟수를 출력하라
핵심로직: 시뮬레이션
    1. grid 반복문에 방향 반복문으로 출발시킨다 / 함수에 넣는다
    2. 함수는 로봇을 M일만큼 동작시키고 수확값을 반환한다
    3. 최댓값을 갱신한다.
"""

def robot(r, c, d, day):
    global result

    total = 0

    while day < M + 1:

        # 하루의 시작. 심어놓은 곡식이 자란다
        for lr in range(N):
            for lc in range(N):
                if land[lr][lc][1] is not None and land[lr][lc][1] != 0:
                    land[lr][lc][1] -= 1

        nr, nc, nd = r, c, d

        for i in range(4):
            next_d = (d + directions[i]) % 4
            next_r = r + dr[next_d]
            next_c = c + dc[next_d]

            if grid[next_r][next_c] != 0:
                continue

            if land[next_r][next_c][1] in (None, 0):
                nr, nc, nd = next_r, next_c, next_d
                break

        if land[r][c][1] == 0:
            total += 1
            land[r][c][1] = None

        elif land[r][c][1] is None and (nr, nc) != (r, c):
            land[r][c][1] = land[r][c][0] + 4
            land[r][c][0] += 1

        r, c, d = nr, nc, nd

        day += 1

    return total

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

directions = [1, 0, -1, -2]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for r in range(1, N - 1):
        for c in range(1, N - 1):
            for d in range(4):
                land = [[[1, None] for _ in range(N)] for _ in range(N)]  # 곡물을 관리하는 배열
                if grid[r][c] == 0:
                    total = robot(r, c, d, 1)
                    result = max(result, total)

    print(f'#{tc} {result}')