# Ladder1 1차 시도: PASS(38분)

# 1. 목표: 100 x 100 행렬에서, 2가 표기된 좌표에서 사다리를 타고 올라가 r이 0이 될 때, c를 구하기
# 2. 상태: r, c: 현재 사다리 위치 / d: 현재 진행 방향
# 3. 자료구조: 델타 이동, 맨 아래 row에서 시작(grid[r][c] == 2, r==99)
# 4. 핵심로직
    # 0. while True:
    # 1. 델타: dr = [-1, 0, 0], dc = [0, -1, 1] / d = 0
    # 1. 우선 전진, nr = r + dr[d], nc = c + dc[d]
    # 2. 좌측이 벽이 아니고, 1이 있으면 좌측으로 방향 전환 if not c - 1 < 0 and grid[r][c - 1] == 1:, d + 1
    # 3. 우측이 벽이 아니고, 1이 있으면 우측으로 방향 전환 if not c + 1 >= N and grid[r][c + 1] == 1:, d + 2
    # 4. 그 방향으로 전진. 
    # 5. 만약 전진한 좌표 위에 1이 있으면 다시 위로 방향 전환. if grid[r -1][c] == 1: d = 0
# 5. 종료조건: r == 0 일때 종료

dr = [-1, 0, 0]
dc = [0, -1, 1]

for _ in range(1, 11):
    tc = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]

    # 일단 찾아야지, 2가 어디 있는지.
    r = 99
    c = grid[99].index(2)

    d = 0

    while True:
        r = r + dr[d]
        c = c + dc[d]
        if r == 0:
            break

        if d == 0 and not c - 1 < 0 and grid[r][c - 1] == 1:
            d = 1
        elif d == 0 and not c + 1 >= 100 and grid[r][c + 1] == 1:
            d = 2
        elif d != 0 and grid[r - 1][c] == 1:
            d = 0

    print(f'#{tc} {c}')