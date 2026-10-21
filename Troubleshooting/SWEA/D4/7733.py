# SWEA 7733. 치즈 도둑

# 1차 시도: PASS(30분)
# 졸업

# 목표: 
    # 1. 1 ~ 100까지의 숫자로 채워진 N x N 2차원 행렬이 주어진다. 
    # 2. X일이 지나면 X 이하의 숫자는 모두 사라진다.
    # 3. 상하좌우로 연결된 치즈 덩어리들이 가장 많은 날 X를 구하라
# 상태: visited = 먹혀버린 치즈들. count = 치즈 덩어리의 개수, result = 현재까지의 최고 기록
# 자료구조: DFS, visited, 델타 이동
# 핵심 로직: 
    # 1. DFS에는 r, c만 매개변수로 넘김
    # 2. 메인 코드에서 grid를 순회하며 count의 개수를 찾음
    # 3. while문으로 day <= 100 설정함
# 종료 조건: day = 100이 되었을 때, result 출력

def dfs(r, c):

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc)



dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    day = 1
    result = 1

    while day <= 100:
        visited = [[False] * N for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if visited[r][c]:
                    continue
                if grid[r][c] <= day:
                    visited[r][c] = True

        count = 0

        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    visited[r][c] = True
                    dfs(r, c)
                    count += 1

        result = max(result, count)

        day += 1

    print(f'#{tc} {result}')