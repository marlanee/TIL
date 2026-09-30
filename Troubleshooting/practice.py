# SWEA 1953. 탈주범 검거

# 1차 시도: 16:58

# 목표: N x M 격자. L 시간이 지난 후 범인이 존재할 수 있는 장소의 개수를 구하라
# 상태: total = 존재할 수 있는 장소의 개수 / count = 지난 시간 / q = 범인이 다음에 갈 장소
# 자료구조: BFS, visited
# 핵심 로직: 
    # 1. queue에 맨홀 뚜껑의 위치를 담는다.
    # 2. queue.pop() 으로 위치를 꺼내고 nr, nc를 구한다.
    # 3. total은 for문, count는 while문
    # 4. 방문하지 않았다면 queue에 집어넣는다.
# 종료 조건: count == L 일 때. / while < L / total 출력

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]
    count = 0
    total = 0
    q = deque([(R, C)])
    grid[R][C] = True

    while q:

        if count == L:
            break

        count += 1

        for _ in range(len(q)):
            r, c = q.popleft()

            total += 1

            if grid[r][c] == 1:
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
            elif grid[r][c] == 2:
                for i in range(2):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
            elif grid[r][c] == 3:
                for i in range(2, 4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
            elif grid[r][c] == 4:
                for i in range(0, 4, 3):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
            elif grid[r][c] == 5:
                for i in range(1, 4, 2):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
            elif grid[r][c] == 6:
                for i in range(1, 3):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True
            elif grid[r][c] == 7:
                for i in range(0, 3, 2):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] != 0 and not visited[nr][nc]:
                        q.append((nr, nc))
                        visited[nr][nc] = True

    print(f'#{tc} {total}')