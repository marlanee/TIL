# SWEA 1949. 등산로 조성

# 복습: PASS(30분)
# 졸업

# 목표: 임의의 숫자로 채워진 N x N 행렬에서, 내림차순으로 만들 수 있는 가장 긴 길의 길이를 구하여라.
# 상태: visited = 방문 여부 파악. used = 공사 여부 파악, length = 현재까지 만든 길의 길이
# 자료구조: dfs, visited, 델타 탐색
# 핵심 로직:
    # 1. 가장 높은 봉우리 탐색, 관리하는 리스트 생성
    # 2. 각 봉우리별 순회 시작
    # 3. dfs(r, c, length, used)
    # 4. 공사도 못하고, 길이 막혀있을 경우 length 갱신 후 return
# 종료 조건: 마지막 봉우리까지 dfs 순회가 끝났을 떄. 최종 갱신된 length 출력

def dfs(r, c, length, used):
    global result
    result = max(result, length)

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:

            if grid[nr][nc] < grid[r][c]:
                visited[nr][nc] = True
                dfs(nr, nc, length + 1, used)
                visited[nr][nc] = False

            elif grid[nr][nc] - K < grid[r][c] and not used:
                origin = grid[nr][nc]
                grid[nr][nc] = grid[r][c] - 1
                visited[nr][nc] = True
                dfs(nr, nc, length + 1, used=True)
                grid[nr][nc] = origin
                visited[nr][nc] = False
            
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    top_num = max(map(max, grid))
    top_list = []
    visited = [[False] * N for _ in range(N)]
    result = 0

    for r_idx, row in enumerate(grid):
        for c_idx, col in enumerate(row):
            if col == top_num:
                top_list.append((r_idx, c_idx))

    for r, c in top_list:
        visited[r][c] = True
        dfs(r, c, 1, False)
        visited[r][c] = False

    print(f'#{tc} {result}')

