# SWEA 2105. 디저트 카페

# 1차 시도: Neutral(60분)
# 10. 5. 복습 필요

"""
목표: 
    1. 1~ 100 범위의 정수로 가득한 N x N 격자가 주어짐. 
    2. 한 점(r, c)에서 출발해 대각선으로만 중복되는 숫자 없이 움직일 수 있음
    3. 단, 대각선 방향은 시계 방향 순서로만 바꿀 수 있음 / 그대로 가거나, 시계방향 순으로 바뀌거나.
    4. 예시) (좌, 상) -> (우, 상) -> (우, 하) -> (좌, 하) / 이 4가지 케이스만 존재 가능
상태: visited = 이미 방문했는지 확인
자료구조: dfs, 델타 탐색, visited, 백트래킹
핵심 로직: 
    1. grid를 순회함.
    2. dfs(r, c, d) 호출
    3. dfs 내에서 그냥 직진하는 케이스와 방향을 바꾸는 호출을 만듦
    4. 격자 밖으로 나가거나, visited = True면 return함.
    5. grid[nr][nc] == grid[row][col] 일 경우 최대값을 갱신함
    6. 반복문이 종료되면 종료
종료 조건: grid 순회가 종료되면 최대값 출력
시간복잡도:
"""

# def dfs(r, c, d, count):
#     global result

#     nr = r + dr[d]
#     nc = c + dc[d]

#     if not (0 <= nr < N and 0 <= nc < N):
#         return

#     if count >= 6:
#         return

#     if nr == row and nc == col:
#         result = max(result, len(dessert))
#         return

#     if grid[nr][nc] in dessert:
#         return

#     dessert.add(grid[nr][nc])

#     dfs(nr, nc, d, count)
#     dfs(nr, nc, (d + 1) % 4, count + 1)

#     dessert.remove(grid[nr][nc])

# dr = [-1, -1, 1, 1]
# dc = [-1, 1, 1, -1]

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]

#     result = -1

#     for row in range(N):
#         for col in range(N):
#             for d in range(4):
#                 dessert = {grid[row][col]}
#                 dfs(row, col, d, 1)

#     print(f"#{tc} {result}")

# 아래는 Chatgpt가 추천해준 코드다

"""
목표: 
    1. 대각선으로 사각형 경로를 만들며,
    2. 같은 종류의 디저트를 중복해서 먹지 않을 때
    3. 먹을 수 있는 디저트의 최대 개수를 구한다
상태: r, c = 현재 위치 / d = 현재 진행 방향 / count = 현재까지 먹은 디저트 개수 / eaten = 현재 경로에서 먹은 디저트 종류
자료구조: DFS, 백트래킹, 델타 탐색, boolean 배열
핵심 로직:
    1. 모든 칸을 사각형의 시작 꼭짓점으로 탐색한다
    2. 시작 방향은 ↘로 고정한다
    3. 현재 방향으로 직진하거나 다음 방향으로 한 번 꺾는다
    4. 방향은 ↘ → ↙ → ↖ → ↗ 순서로만 진행한다.(*대칭 구조이기 때문이다*)
    5. 이미 먹은 디저트라면 해당 경로를 중단한다
    6. 시작점으로 돌아오면 result를 갱신한다
    7. DFS 종료 후 eaten 상태를 복구한다
종료 조건: 시작점으로 돌아왔거나 더 이상 유효한 이동이 없을 때
"""

def dfs(r, c, d, count):
    global result

    for nd in (d, d + 1):

        if nd >= 4:
            continue

        nr = r + dr[nd]
        nc = c + dc[nd]

        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if nr == start_r and nc == start_c:
            result = max(result, count)
            continue

        dessert = grid[nr][nc]

        if eaten[dessert]:
            continue

        eaten[dessert] = True

        dfs(nr, nc, nd, count + 1)

        eaten[dessert] = False

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    result = -1
    eaten = [False] * 101

    for start_r in range(N):
        for start_c in range(N):

            eaten[grid[start_r][start_c]] = True

            nr = start_r + dr[0]
            nc = start_c + dc[0]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            dessert = grid[nr][nc]

            if eaten[dessert]:
                continue

            eaten[dessert] = True

            dfs(nr, nc, 0, 2)

            eaten[dessert] = False
            eaten[grid[start_r][start_c]] = False

    print(f'#{tc} {result}')