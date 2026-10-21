# 섬 찾기

# 1차 시도: PASS(17분)

# 목표: 2차원 격자가 주어진다. 1은 섬이다. 상하좌우대각선에 1이 추가로 있다면, 연결된 하나의 섬이다. 섬의 개수를 찾아라.
# 상태: visited = 이미 찾은 섬인지 확인, grid = 섬 정보를 갖는 2차원 행렬, count = 섬의 개수
# 자료구조: DFS
# 핵심 로직: 
    # 1. 2차원 행렬을 row, col을 모두 순회하며 1을 찾는다.
    # 2. 1을 찾는다면, count += 1을 한 후 DFS로 상하좌우대각선에 1이 있는지 끝까지 탐색한다.
    # 3. 그 1은 다음 r, c가 되며 visited = True 처리가 된다.
    # 4. dfs 함수의 요소는 (r, c) = dfs(r, c)
# 종료 조건: 반복문의 순회가 모두 끝났을 떄, count를 출력

def dfs(r, c):

    for d in range(8):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M:
            if grid[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                dfs(nr, nc)


dr = [1, 1, 1, 0, -1, -1, -1, 0]
dc = [1, 0, -1, -1, -1, 0, 1, 1]    

N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
count = 0

for r in range(N):
    for c in range(M):
        if grid[r][c] == 1 and not visited[r][c]:
            visited[r][c] = True
            dfs(r, c)
            count += 1

print(count)