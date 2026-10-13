# SWEA 2105. 디저트 카페
# 복습: FAIL(80분)
# 10. 21. 복습 필요

"""
목표: N x N 지역에 디저트 카페가 모여 있다. 그 안에는 디저트 종류가 적혀진 카페들이 있다.
    1. 임의의 한 지점에서 마름모 모양을 그리며 카페로 돌아와야 한다.
        1. *지정: 우하 -> 좌하 -> 좌상 -> 우상 순서 고정*
    2. 이 때 같은 종류의 디저트를 먹어서는 안된다.
    3. 이 조건을 만족하는 길로 갈 때, 가능한 길의 최대 길이를 구하라
상태: dessert = 이미 먹은 디저트의 리스트. origin_r, c = 처음 출발한 위치, length = 현재 누적길이
자료구조: dfs / 백트래킹
핵심로직:
    1. grid를 순회함
        1. for r in range(0, N - 2)
            for c in range(1, N - 1)
    2. dessert = {grid[r][c]} 세트를 만듦. 이미 먹었는지 확인하기 위함임
    2-2. origin_r, origin_c = r, c
    3. dfs(r + 1, c + 1, d(0), length(1)) 호출
    4. dfs 내부에서 가지치기: if grid[r][c] in dessert 면 return
    5. dfs 종료조건: if r, c == origin_r, origin_c 면 최댓값 갱신
        1. max_length = max(max_length, length)
    6. 재귀호출 1: 방향 그대로
        1. dfs(r + dr[d], c + dc[d], d, length + 1)
    7. 재귀호출 2: 방향 바꿈
        1. if d < 3:
            dfs(r + dr[d + 1], c + dc[d], d + 1, length + 1)
    8. 재귀 호출마다 백트래킹이 필요함. 음식을 집어넣고 빼는.
종료조건:
시간복잡도: 코드 작성 후 계산
"""

def dfs(r, c, d, length):
    global max_length

    for nd in (d, d + 1):  # 직진 / 다음 방향으로 전환
        if nd > 3:
            continue

        nr = r + dr[nd]
        nc = c + dc[nd]

        if not (0 <= nr < N and 0 <= nc < N):
            continue  # 이 후보만 제외하고 다른 후보 확인

        # 시작점 복귀는 디저트 중복 검사보다 먼저!
        if (nr, nc) == (origin_r, origin_c):
            max_length = max(max_length, length)
            continue

        food = grid[nr][nc]
        if food in dessert:
            continue

        dessert.add(food)
        dfs(nr, nc, nd, length + 1)
        dessert.remove(food)
        
dr = [1, 1, -1, -1]
dc = [1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_length = -1

    for r in range(0, N - 2):
        for c in range(1, N - 1):
            dessert = {grid[r][c]}
            origin_r, origin_c = r, c
            dfs(r, c, 0, 1)

    print(f'#{tc} {max_length}')