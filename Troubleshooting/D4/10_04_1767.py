# SWEA 1767. 프로세서 연결하기
# 1차 시도: FAIL(90분) -> 힌트 참조 후 PASS
# 10. 4. 복습 필요

"""
목표:
    1. 0 또는 1로 채워진 N x N 격자가 주어진다
    2. 1로 채워진 칸을 상하좌우 중 하나에 선을 연결하여 N - 1 벽에 연결시켜야 한다
    3. 이미 N - 1에 위치한 1의 경우 연결된 것으로 간주한다
    4. 최대한 많은 1을 벽에 연결시키고, 그 때의 최소 연결 길이를 구하라
상태: core = 1이 위치한 좌표를 담는 리스트. connected = 연결된 1의 수, length = 전선 길이의 누적합
자료구조: DFS, 백트래킹, 델타 탐색, 행렬 전치, visited
핵심 로직: 
    1. core을 순회하며 하나씩, 4방향으로 순회하며 연결하고 시작함 / 방문 처리 필수
    2. 좌, 우에 1 또는 2(선)이 있다면 continue 가지치기(전치 행렬의 경우 상, 하 개념임)
    3. dfs(connected, length) 시작. 
    4. 방문 처리된 core들을 제외하고 순회하며 재귀 호출 시작
    5. 만약 연결할 1이 없다면, (count == 0), connected > total_connected 일 때 max(total_length, length) 비교
종료 조건: 반복문이 종료되었을 때
시간 복잡도: O(N^4) / O(N!)
"""

def dfs(idx, connected, length):
    global total_connected, total_length

    if idx == core_num:
        if connected > total_connected:
            total_connected = connected
            total_length = length

        elif connected == total_connected:
            total_length = min(total_length, length)

        return

    r, c = core[idx]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        check = False
        count = 0

        while 0 <= nr < N and 0 <= nc < N:
            if grid[nr][nc] != 0:
                check = True
                break
            nr = nr + dr[i]
            nc = nc + dc[i]

        nr = r + dr[i]
        nc = c + dc[i]

        if not check:
            while 0 <= nr < N and 0 <= nc < N:
                grid[nr][nc] = 2
                nr = nr + dr[i]
                nc = nc + dc[i]
                count += 1

            dfs(idx + 1, connected + 1, length + count)

            nr = r + dr[i]
            nc = c + dc[i]

            while 0 <= nr < N and 0 <= nc < N:
                grid[nr][nc] = 0
                nr = nr + dr[i]
                nc = nc + dc[i]

    dfs(idx + 1, connected, length)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    total_connected = 0
    total_length = 0
    core = []

    for r in range(1, N - 1):
        for c in range(1, N - 1):
            if grid[r][c] == 1:
                core.append((r, c))

    core_num = len(core)

    dfs(0, 0, 0)

    print(f'#{tc} {total_length}')