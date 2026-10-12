# SWEA 1767. 프로세서 연결하기
# 1차 시도: FAIL(90분) -> 힌트 참조 후 PASS
# 10. 4. 복습 필요
# 2차 시도: 거의 PASS(60분)
# 10. 15 복습 필요

# """
# 목표:
#     1. 0 또는 1로 채워진 N x N 격자가 주어진다
#     2. 1로 채워진 칸을 상하좌우 중 하나에 선을 연결하여 N - 1 벽에 연결시켜야 한다
#     3. 이미 N - 1에 위치한 1의 경우 연결된 것으로 간주한다
#     4. 최대한 많은 1을 벽에 연결시키고, 그 때의 최소 연결 길이를 구하라
# 상태: core = 1이 위치한 좌표를 담는 리스트. connected = 연결된 1의 수, length = 전선 길이의 누적합
# 자료구조: DFS, 백트래킹, 델타 탐색, 행렬 전치, visited
# 핵심 로직: 
#     1. core을 순회하며 하나씩, 4방향으로 순회하며 연결하고 시작함 / 방문 처리 필수
#     2. 좌, 우에 1 또는 2(선)이 있다면 continue 가지치기(전치 행렬의 경우 상, 하 개념임)
#     3. dfs(connected, length) 시작. 
#     4. 방문 처리된 core들을 제외하고 순회하며 재귀 호출 시작
#     5. 만약 연결할 1이 없다면, (count == 0), connected > total_connected 일 때 max(total_length, length) 비교
# 종료 조건: 반복문이 종료되었을 때
# 시간 복잡도: O(N^4) / O(N!)
# """

# def dfs(idx, connected, length):
#     global total_connected, total_length

#     if idx == core_num:
#         if connected > total_connected:
#             total_connected = connected
#             total_length = length

#         elif connected == total_connected:
#             total_length = min(total_length, length)

#         return

#     r, c = core[idx]

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#         check = False
#         count = 0

#         while 0 <= nr < N and 0 <= nc < N:
#             if grid[nr][nc] != 0:
#                 check = True
#                 break
#             nr = nr + dr[i]
#             nc = nc + dc[i]

#         nr = r + dr[i]
#         nc = c + dc[i]

#         if not check:
#             while 0 <= nr < N and 0 <= nc < N:
#                 grid[nr][nc] = 2
#                 nr = nr + dr[i]
#                 nc = nc + dc[i]
#                 count += 1

#             dfs(idx + 1, connected + 1, length + count)

#             nr = r + dr[i]
#             nc = c + dc[i]

#             while 0 <= nr < N and 0 <= nc < N:
#                 grid[nr][nc] = 0
#                 nr = nr + dr[i]
#                 nc = nc + dc[i]

#     dfs(idx + 1, connected, length)


# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input().split())) for _ in range(N)]

#     total_connected = 0
#     total_length = 0
#     core = []

#     for r in range(1, N - 1):
#         for c in range(1, N - 1):
#             if grid[r][c] == 1:
#                 core.append((r, c))

#     core_num = len(core)

#     dfs(0, 0, 0)

#     print(f'#{tc} {total_length}')

# SWEA 1767. 프로세서 연결하기
# 복습: 거의 PASS(1시간)

"""
목표: 
    1. N x N 크기의 cell이 주어짐
    2. cell에 존재하는 core에 전선을 가장자리까지 연결시켜야 함
    3. 전선은 교차할 수 없음
    4. 가장 많은 core를 연결시키고, 이 때 전선 길이의 합이 최소가 되는 값을 구하라
상태: 
    1. target_core = 벽에 붙어있지 않은 코어들의 좌표를 담는 리스트
    2. dfs(count, length, find) / count = 연결한 코어의 개수 / length = 연결한 길이 / find = 탐색한 코어의 개수
자료구조: DFS, 백트래킹
핵심로직:
    1. 벽에 붙어있지 않은 코어의 좌표를 찾아 리스트에 담음
    2. dfs를 호출함. 
    3. core를 선택하지 않는 재귀호출
    4. 4방향으로 연결 가능한지 탐색 후 연결하는 재귀 호출 / 백트래킹
    5. 벽에 붙어있지 않은 코어만큼 탐색을 완료했다면 재귀 호출 종료 후 갱신
종료조건: 
    1. dfs = count == len(target_core) 일 때
    2. 재귀 호출이 종료되었을 때
시간복잡도: 계산중
"""
from copy import deepcopy

def dfs(count, length, find):
    global max_connected, min_length, grid

    if target_len - find + count < max_connected:
        return

    if find == target_len:
        if count > max_connected:
            max_connected = count
            min_length = length
        elif count == max_connected:
            min_length = min(min_length, length)
        return

    dfs(count, length, find + 1)  # 해당 코어를 연결하지 않고 넘어가는 재귀 호출

    r, c = target_core[find]   # 이번에 연결할지 확인할 코어

    for d in range(4):  # 4방향 연결 탐색
        new_grid = deepcopy(grid)
        i = 1
        check = True
        while True:
            nr = r + dr[d] * i
            nc = c + dc[d] * i

            if not (0 <= nr < N and 0 <= nc < N):
                break

            if grid[nr][nc] != 0:
                check = False
                break

            grid[nr][nc] = 2
            i += 1

        if check:
            dfs(count + 1, length + i - 1, find + 1)

        grid = new_grid # 백트래킹

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    target_core = []
    min_length = float('inf')
    max_connected = 0

    for r in range(1, N - 1):   # 벽에 붙어있지 않은 코어의 좌표 찾기
        for c in range(1, N - 1):
            if grid[r][c] == 1:
                target_core.append((r, c))

    target_len = len(target_core)

    dfs(0, 0, 0)

    print(f'#{tc} {min_length}')


