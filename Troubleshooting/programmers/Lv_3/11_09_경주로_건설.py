# 261107. programmers. 경주로 건설
# 1차 시도: RuntimeError(30분) / DFS로 런타임 에러. 다익스트라 구현 요규
# 11. 9. 복습 필요
"""
목표: N x N 크기의 부지가 주어진다.
    1. 이 곳에 경주로를 건설해야 한다
    2. 직선 도로 하나당 100원
    3. 코너 하나당 500원이 소요된다.
    4. 출발지(0, 0)부터 도착점(N-1,N-1)까지 최소 설치비용을 구하라
핵심로직: DFS/백트래킹, 
    1. visited를 만들자. N x N 크기로.
    2. 4방향으로 랜덤 이동한다. 
    3. 도착 지점에 도달하면 최솟값을 갱신한다.
"""
from heapq import heappush, heappop
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]



def solution(board):
    N = len(board)
    best_cost = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]

    pq = [(0, 0, 0, -1)]

    while pq:
        cost, r, c, d = heappop(pq)

        if d != -1 and cost > best_cost[r][c][d]:
            continue

        if (r, c) == (N - 1, N - 1):
            return cost

        for nd in range(4):
            nr = r + dr[nd]
            nc = c + dc[nd]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if board[nr][nc] != 0:
                continue

            if d == -1 or nd == d:
                new_cost = cost + 100
            else:
                new_cost = cost + 600

            if new_cost < best_cost[nr][nc][nd]:
                best_cost[nr][nc][nd] = new_cost
                heappush(pq, (new_cost, nr, nc, nd))
    return -1


board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]

print(solution(board))