# 달팽이 문제. 1차 시도: PASS(15분)

# 1. 목표: N * N 2차원 행렬을 달팽이 모양으로 숫자를 채우는 것
# 2. 구조: 우하좌상 규칙으로 델타 이동 규칙 설정
# 3. 종료: N * N 숫자를 모두 입력하면 종료

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [[0] * N for _ in range(N)]

    r, c = 0, 0 # 달팽이의 초기 위치 설정
    d = 0   # 달팽이가 가는 방향 direction의 약자

    dr = [0, 1, 0, -1]  # row 방향의 델타 이동 규칙
    dc = [1, 0, -1, 0]  # col

    for num in range(1, N * N + 1):
        grid[r][c] = num
        nr = r + dr[d]  # 달팽이의 다음 위치
        nc = c + dc[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= N or grid[nr][nc] != 0:
            d = (d + 1) % 4   # 벽, 숫자를 만나면 다음 방향으로 변경
            nr = r + dr[d]
            nc = c + dc[d]

        r, c = nr, nc

    print(f'#{tc}')
    for row in grid:
        print(*row)