# SWEA 1953. 탈주범 검거

# 1차 시도: FAIL
# 10. 02 복습 필요
# 복습: PASS(30분)
# 10. 7. 졸업

# 목표: N x M 격자. L 시간이 지난 후 범인이 존재할 수 있는 장소의 개수를 구하라
# 상태: total = 존재할 수 있는 장소의 개수 / count = 지난 시간 / q = 범인이 다음에 갈 장소
# 자료구조: BFS, visited
# 핵심 로직: 현재 터널의 출구 방향과 다음 터널의 반대편 입구가 모두 연결된 경우에만 이동한다
    # 1. queue에 맨홀 뚜껑의 위치를 담는다.
    # 2. queue에서 현재 위치를 popleft하여 해당 터널이 연결된 방향을 탐색한다
    # 3. total은 for문, count는 while문
    # 4. 방문하지 않았다면 queue에 집어넣는다.
# 종료 조건: count == L 일 때. / while < L / total 출력
# 시간복잡도: O(NM)

# from collections import deque

# tunnel = {
#     1: [0, 1, 2, 3],
#     2: [0, 1],
#     3: [2, 3],
#     4: [0, 3],
#     5: [1, 3],
#     6: [1, 2],
#     7: [0, 2]
# }
# opposite = [1, 0, 3, 2]

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# T = int(input())
# for tc in range(1, T + 1):
#     N, M, R, C, L = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(N)]

#     visited = [[False] * M for _ in range(N)]
#     count = 0
#     total = 0
#     q = deque([(R, C)])
#     visited[R][C] = True

#     while q:

#         if count == L:
#             break

#         count += 1

#         for _ in range(len(q)):
#             r, c = q.popleft()

#             total += 1

#             for d in tunnel[grid[r][c]]:
#                 nr = r + dr[d]
#                 nc = c + dc[d]
#                 if 0 <= nr < N and 0 <= nc < M:
#                     if not visited[nr][nc] and grid[nr][nc] != 0:
#                         if opposite[d] in tunnel[grid[nr][nc]]:
#                             q.append((nr, nc))
#                             visited[nr][nc] = True

#     print(f'#{tc} {total}')

# 아래는 chatgpt의 추천 방법

# from collections import deque

# tunnel = {
#     1: [0, 1, 2, 3],
#     2: [0, 1],
#     3: [2, 3],
#     4: [0, 3],
#     5: [1, 3],
#     6: [1, 2],
#     7: [0, 2]
# }
# opposite = [1, 0, 3, 2]

# dr = [-1, 1, 0, 0]
# dc = [0, 0, -1, 1]

# T = int(input())

# for tc in range(1, T + 1):
#     N, M, R, C, L = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(N)]

#     visited = [[0] * M for _ in range(N)]

#     q = deque([(R, C)])
#     visited[R][C] = 1

#     while q:
#         r, c = q.popleft()

#         if visited[r][c] == L:
#             continue

#         for d in tunnel[grid[r][c]]:
#             nr = r + dr[d]
#             nc = c + dc[d]

#             if not (0 <= nr < N and 0 <= nc < M):
#                 continue

#             if visited[nr][nc]:
#                 continue

#             if grid[nr][nc] == 0:
#                 continue

#             if opposite[d] not in tunnel[grid[nr][nc]]:
#                 continue

#             visited[nr][nc] = visited[r][c] + 1
#             q.append((nr, nc))

#     result = 0

#     for r in range(N):
#         for c in range(M):
#             if visited[r][c]:
#                 result += 1

#     print(f'#{tc} {result}')

# SWEA 1953. 탈주범 검거
# 복습: PASS(30분)

"""
목표:
    1. N x M 지하 터널 지도가 주어진다.
    2. 흉악범이 교도소를 탈출해 1시간 후 지하 터널로 들어갔다
    3. 흉악범은 1시간당 1 거리만큼 움직일 수 있다
    4. L 시간이 지난 후, 흉악범이 위치할 수 있는 위치의 개수를 구하시오
상태: 
    1. current = 도둑이 있는 현재 장소
    2. visited = 이미 도둑이 방문한 장소
    3. time = 지난 시간
자료구조: BFS, 델타 이동, visited
핵심 로직:
    1. time을 1로 설정함
    2. current에 도둑이 출발하는 장소를 넣음
    3. current를 순회하며 터널이 연결되어있고, 방문 처리되어 있지 않은 장소를 current에 넣음
    4. time += 1을 함
    5. time == L 이 되었을 때, while문이 종료되고 visited = True 처리되어있는 장소 총계를 출력함
종료 조건: while time < L: 
시간 복잡도: O(NM)
"""
from collections import deque

tunnel = {
    1 : [0, 1, 2, 3],
    2 : [0, 1],
    3 : [2, 3],
    4 : [0, 3],
    5 : [1, 3],
    6 : [1, 2],
    7 : [0, 2]
}

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
reverse = [1, 0, 3, 2]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    time = 1
    current = deque([(R, C)])
    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    count = 0

    while time < L:

        if not current:
            break

        for _ in range(len(current)):   # 한 사이클이 돌면 1시간이 경과했다는 의미
            r, c = current.popleft()

            if grid[r][c] != 0: # 터널이 연결되어 갈 수 있는지 확인하는 코드
                for d in tunnel[grid[r][c]]:
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if not (0 <= nr < N and 0 <= nc < M):
                        continue

                    if visited[nr][nc]:
                        continue

                    if grid[nr][nc] == 0:
                        continue

                    if reverse[d] in tunnel[grid[nr][nc]]:  # 다음 좌표와 통로가 연결되면
                        visited[nr][nc] = True  # 방문 처리
                        current.append((nr, nc))

        time += 1

    result = 0 

    for r in range(N):
        check = [visited[r][c] for c in range(M) if visited[r][c]]
        result += len(check)

    print(f'#{tc} {result}')