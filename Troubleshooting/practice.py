# SWEA 2105. 디저트 카페
# 2차 복습: PASS(30분)

"""
목표: 디저트의 숫자(카페)가 채워진 N x N 지역이 주어진다.
    1. 최대한 많은 카페에 방문하려고 한다
    2. 반드시 사각형 모양을 그리며 이동해야 한다
    3. 같은 메뉴는 먹을 수 없다
    4. 최대 카페 방문수를 구하라
상태: 
    1. current = 현재 좌표에서 출발해서 먹은 디저트 메뉴
    2. max_count = 현재까지 찾은 최대 카페 방문수
자료구조: 델타 이동, dfs/백트래킹
핵심로직:
    1. grid를 순회  # 사각형을 못 그리는 출발점은 필요 없다. index를 제한한다.
        for r in range(N - 2)
            for c in range(1, N - 1)
    2. dfs 사용
        1. dfs(r, c, d, count)
        2. 가지치기 A: 같은 메뉴가 current에 들어있을 때 return
        3. 가지치기 B: 벽을 만나면 return
        3. 종료 조건: nr, nc == row, col일 때 max_count 갱신
        4. 재귀 호출 A: dfs(nr, nc, d, count + 1) # 방향을 바꾸지 않을 때
        5. 만약 d가 3보다 작을 때
            5 - 1. 재귀 호출 B: dfs(nr, nc, d + 1, count + 1) # 방향을 바꿀 때
종료 조건: grid 순회가 끝났을 때 max_count 출력
시간 복잡도: O(N^6)
"""

dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

def dfs(r, c, d, count):
    global max_count

    # 일단 이동
    nr = r + dr[d]
    nc = c + dc[d]  

    if not (0 <= nr < N and 0 <= nc < N):   # 벽 만나면 종료
        return

    if (nr, nc) == (row, col):  # 종료 조건
        max_count = max(max_count, count)
        return

    if grid[nr][nc] in current: # 이미 먹은 디저트면 종료
        return

    current.add(grid[nr][nc])
    # 방향을 바꾸지 않는 경우
    dfs(nr, nc, d, count + 1)
    # 방향을 바꾸는 경우
    if d < 3:
        dfs(nr, nc, d + 1, count + 1)
    current.remove(grid[nr][nc])


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_count = -1

    for row in range(N - 2):
        for col in range(1, N - 1):
            current = {grid[row][col]}  # 시간복잡도 문제로 set 사용
            dfs(row, col, 0, 1)

    print(f'#{tc} {max_count}')