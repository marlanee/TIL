# SWEA 1868. 파핑파핑 지뢰찾기

# 1차 시도: FAIL(40분)
# 9. 21. 복습 필요

# 목표: 지뢰가 아닌 모든 칸을 열기 위해 필요한 최소 클릭 수를 구한다.
# 상태:
    # 1. grid =  원본 지뢰판
    # 2. mine_count = 각 칸 주변 8방향의 지뢰 개수
    # 3. visited = 이미 열린 칸 여부
    # 4. count = 직접 클릭한 회수
# 자료구조: BFS, deque, 8방향 델타 탐색
# 핵심 로직: 
    # 1. 모든 '.'에 대해 주변 지뢰 개수를 mine_count에 저장한다.
    # 2. 아직 방문하지 않은 mine_count == 0 칸을 찾으면 count += 1
    # 3. 해당 0에서 BFS를 시작한다.
    # 4. 주변 숫자칸은 방문 처리한다. 그 칸도 0이면 queue에 넣어 계속 확장한다.(재귀 호출)
    # 5. 모든 0 영역을 처리한 후에도 방문하지 않은 '.'을 처리한다.
    # 6. 자동으로 열리지 않는 칸이므로 직접 찾아내 count += 1을 해준다.
# 종료 조건: '.'이 하나도 없어질 때, count 출력
# 시간복잡도: O(N^2)

from collections import deque

def BFS(r, c):

    q = deque([(r, c)])

    while q:
        r, c = q.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and grid[nr][nc] != '*':
                    visited[nr][nc] = True

                    if mine_count[nr][nc] == 0:
                        q.append((nr, nc))

# 우측부터 시계방향
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    grid = [list(input()) for _ in range(N)]
    mine_count = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    count = 0

    for r in range(N):
        for c in range(N):
            if grid[r][c] == '.':
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < N:
                        if grid[nr][nc] == '*':
                            mine_count[r][c] += 1

    for r in range(N):
        for c in range(N):
            if grid[r][c] == '.' and mine_count[r][c] == 0 and not visited[r][c]:
                visited[r][c] = True
                count += 1
                BFS(r, c)


    for r in range(N):
        for c in range(N):
            if grid[r][c] == '.' and not visited[r][c]:
                visited[r][c] = True
                count += 1

    print(f'#{tc} {count}')