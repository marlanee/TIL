# SWEA 1861. 정사각형 방
# 1차 시도: FAIL(1시간)
# 9. 14. 복습 필요

# 1. 목표
    # 1. N x N 행렬에서, 좌표 (r, c)에서 상하좌우가 +1 인 경우에만 이동한다.
    # 2. 이 때, 어떤 좌표(r, c)에서 시작해야 가장 많은 방을 이동할 수 있는지 구하시오.
# 2. 상태: max_r, max_c = 현재까지 찾은 최고의 좌표 / room = 이동한 방의 수 / max_room = 현재까지 최고의 방 수
# 3. 자료구조: DFS/백트래킹, 델타 이동
# 4. 핵심로직
    # 1. 재귀 함수 호출 / DFS / 백트래킹
    # 2. 만약 갈 곳이 없으면 room의 개수와 max_room 개수를 비교 후 갱신, return
    # 3. 델타 이동. for 반복문으로 4방향 탐색
    # 4. 항상 1 더 커야되니까, 백트래킹을 할 필요는 없을수도. visited 행렬이 불필요.
    # 5. global max_r, max_c
# 5. 종료 조건: 함수의 호출이 모두 종료될 때, max_r, max_c 출력

def escape(r, c, room):

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue

        if grid[nr][nc] == grid[r][c] + 1:
            return escape(nr, nc, room + 1)

    return room
            
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_room = 0
    start_room = float('inf')

    for r in range(N):
        for c in range(N):
            current_room = escape(r, c, 1)
            if current_room > max_room:
                max_room = current_room
                start_room = grid[r][c]

            elif current_room == max_room:
                start_room = min(start_room, grid[r][c])

    print(f'#{tc} {start_room} {max_room}')