# SWEA 4875. 미로

# 1차 시도: PASS(20분)

# 목표: N x N 2차원 행렬의 좌표 (r, c)(2) 에서 (r, c)(3)까지 도착할 수 있는지 파악하기
# 상태: gird = 미로 정보 / visited = 이미 방문했는지 확인 / r, c = 현재 위치
# 자료구조: DFS / 델타 이동 / visited
# 핵심로직: 3을 만나면 1을 return
# 종료 조건: 더 이상 나아갈 수 없으면 0, 3을 만나면 1 출력
def maze(r, c):

    if grid[r][c] == 3:
        return 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] != 1 and not visited[nr][nc]:
            visited[nr][nc] = True
            if maze(nr, nc) == 1:
                return 1
            
    return 0

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 2의 좌표를 찾자.
    for idx, row in enumerate(grid):
        if 2 in row:
            r, c = idx, row.index(2)

    visited[r][c] = True

    result = maze(r, c)

    print(f'#{tc} {result}')