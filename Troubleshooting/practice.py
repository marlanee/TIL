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


