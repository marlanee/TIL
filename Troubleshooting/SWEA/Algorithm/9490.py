# 풍선팡. 1차 시도: PASS(30분)

# 1. 목표: N x M 2차원 행렬에서 좌표 (r, c)을 선택할 때, 값 + 그 값만큼 좌우 행렬을 더한 값의 최댓값을 구해야 한다.
# 2. 상태: total 변수를 현재 최댓값을 담는 변수로 사용 / grid[r][c]가 현재 터뜨릴 풍선의 개수.
# 3. 자료구조: 델타 이동, 누적합
# 4. 핵심 로직
    # 1. for flower in range(grid[r][c]) 
    # 2. for i in range(4) / nr = r + dr[i], dc = c + dc[i]
    # 3. 델타 이동에서, 벽을 만나면 continue / if nr < 0 or nr >= N or nc < 0 or nc >= M
# 5. 종료 조건: r, c == N - 1, M - 1일 때 / 즉, r + c >= N + M - 2 일 때

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    total = 0

    for r in range(N):
        for c in range(M):
            flowers = grid[r][c]
            for f in range(1, flowers + 1):
                for i in range(4):
                    nr = r + (f * dr[i])
                    nc = c + (f * dc[i])

                    if nr < 0 or nr >= N or nc < 0 or nc >= M:
                        continue

                    flowers += grid[nr][nc]

            if flowers > total:
                total = flowers

    print(f'#{tc} {total}')