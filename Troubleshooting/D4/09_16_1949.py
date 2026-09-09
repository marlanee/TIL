# 등산로 조정. 1차 시도: FAIL
# 등산로 조정. 2차 시도: FAIL(30분) / 복습 시간(30분)
# 26. 9. 16. 복습 필요

# 1. 목표: N x N 행렬에서, 가장 높은 봉우리에서 시작해 내림차순으로 이동하며, 가장 긴 길의 길이를 구한다.
# 2. 상태: 완전 탐색에서 필요한 정보는 좌표의 위치, 길이, 공사의 사용 여부이다.
# 3. 자료구조: dfs, 델타 이동
# 4. 핵심 로직: 각 최대 봉우리만큼 반복, dfs로 4방향 탐색을 실시하며, 막히면 공사를 시도해본다. 가장 긴 길이를 탐색한다.
# 5. 종료: 모든 dfs 탐색이 끝나면 종료

# def dfs(r, c, length, used):
#     global max_length

#     if length > max_length:
#         max_length = length

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]

#         if not 0 <= nr < N or not 0 <= nc < N:
#             continue
#         if visited[nr][nc]:
#             continue

#         if grid[nr][nc] < grid[r][c]:
#             visited[nr][nc] = True
#             dfs(nr, nc, length + 1, used)
#             visited[nr][nc] = False

#         elif not used and grid[nr][nc] - K < grid[r][c]:
#             h = grid[nr][nc]
#             grid[nr][nc] = grid[r][c] - 1

#             visited[nr][nc] = True
#             dfs(nr, nc, length + 1, used = True)
#             visited[nr][nc] = False
#             grid[nr][nc] = h
            

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]


# T = int(input())
# for tc in range(1, T + 1):
#     N, K = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(N)]
#     max_length = 0

#     # 일단 최대 봉우리의 숫자가 뭔지 찾아야된다.
#     max_n = max(map(max, grid))

#     max_list = []   # 최대 봉우리의 좌표를 저장하는 리스트를 만들었다.

#     for r in range(N):
#         for c in range(N):
#             if grid[r][c] == max_n:
#                 max_list.append((r, c)) # 최대 봉우리를 찾으면 좌표를 리스트에 넣는다.

#     visited = [[False] * N for _ in range(N)]   # 방문한 좌표로 다시 돌아가는 것을 방지하는 행렬이다.

#     for r, c in max_list:   # 자, 이제 dfs를 시작해보자. 최대 봉우리에서부터 시작하는 것이다.
#         visited[r][c] = True
#         dfs(r, c, 1, False)
#         visited[r][c] = False

#     print(f'#{tc} {max_length}')

# 등산로 조정. 2차 시도: FAIL(30분) / 복습 시간(30분)
# 백트래킹을 모두 빼먹었다. 그래서 바꾼 길이 복구되지 않았다.
# 함수를 끝내는 시점이 이상했다. continue가 필요했다.

# 1. 목표
    # 1. N x N 2차원 행렬이 주어짐. 
    # 2. 가장 높은 숫자의 좌표에서 시작해, 행 또는 열로 내림차순으로 이동함
    # 3. 만약 막힐 경우,  단 한번 최대 K만큼 숫자를 줄일 수 있음
    # 4. 이러한 조건을 만족하는 가장 긴 길의 길이를 구하는 것
# 2. 상태
    # 1. 최댓값인 봉우리는 max_list에 좌표를 넣어 관리함
    # 2. 재귀 함수의 필요 요소: r, c, length, used
    # 3. max_length를 전역값으로 지정해 반복문에서도 지속 갱신되게 관리함
# 3. 자료구조: 재귀함수, 리스트 사용 for 반복문, 델타 이동
# 4. 핵심 로직
    # 1. 다음 길의 숫자가 더 낮을 경우 이동, length + 1 / if grid[nr][nc] < grid[r][c]. dfs(nr, nc , length + 1, used)
    # 2. 길이 막혔을 때, grid[nr][nc] - K < grid[r][c], used == False 일 경우 grid[nr][nc] = grid[r][c] - 1
    # 3. grid[nr][nc] >= grid[r][c], used == True 일 경우 return length
    # 4. return한 length와 max_length를 비교해서, length > max_length 일 경우 갱신. 
# 5. 종료 조건: 반복문의 마지막 봉우리 재귀 함수 호출이 모두 종료되었을 때

def dfs(r, c, length, used):
    global max_length

    max_length = max(length, max_length)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        if visited[nr][nc]:
            continue

        if grid[r][c] > grid[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc, length + 1, used)
            visited[nr][nc] = False

        elif grid[nr][nc] - K < grid[r][c] and used == False:
            original = grid[nr][nc]
            grid[nr][nc] = grid[r][c] - 1
            visited[nr][nc] = True
            dfs(nr, nc, length + 1, True)
            grid[nr][nc] = original
            visited[nr][nc] = False
        

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_length = 0

    max_num = max(map(max, grid))
    max_list = []

    visited = [[False] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if grid[r][c] == max_num:
                max_list.append((r, c))

    for r, c in max_list:
        visited[r][c] = True
        dfs(r, c, 1, used=False)
        visited[r][c] = False

    print(f'#{tc} {max_length}')