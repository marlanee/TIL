# SWEA 1226. 미로1

# 1차 시도: FAIL(30분)

# 목표: 16 X 16 2차원 행렬에서, 입구(2)로 시작하는 곳에서 출구(3)으로 도달 가능한지 여부 파악
# 상태: grid = 주어진 2차원 행렬, visited = 방문한 곳을 나타내는 16 x 16 2차원 행렬
# 자료구조: DFS, 델타 이동
# 핵심로직
    # 1. 방문한 곳은 visited = True로 표기, True일 경우 방문 금지
    # 2. 좌우상하가 1일경우 방문 금지
    # 3. 만약 이동한 곳이 외딴 곳일경우(Visited, 방문한 0) 백트래킹 / return
# 종료조건: DFS 함수가 종료되었을 때, 가능하면 1, 아니면 0 출력

def maze(r, c):

    if grid[r][c] == 3:
        return 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if grid[nr][nc] != 1 and visited[nr][nc] != True:
            visited[nr][nc] = True

            if maze(nr, nc) == 1:
                return 1

    return 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(1, 11):
    tc = int(input())

    grid = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    for index, row in enumerate(grid):  # 2의 좌표 구함
        if 2 in row:
            r, c = index, row.index(2)

    visited[r][c] = True

    print(f'#{tc} {maze(r, c)}')