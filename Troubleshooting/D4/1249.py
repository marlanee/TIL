# 보급로. 1차 시도: FAIL / 2차 시도: PASS(180분)
# 인생 첫 D4 문제다. 체감이 어떨지 궁금하다. 일단 도전.

# Chatgpt가 문제 풀기 전에 주석을 작성하라고 한다. 필수라고 한다. 아주 가혹한 녀석이다. 군 시절 포대장이 생각난다.
# 1. 목표: 2차원 행렬에서, 출발지(0, 0)부터 도착지(N - 1, N - 1)까지의 최소 누적합을 구해야 한다.
# 2. 상태: dist[r][c]가 누적합이다.
# 3. 자료구조: 
    # 1. grid: 구멍의 깊이, 도착시 더해야 하는 숫자
    # 2. dist: grid와 동일한 크기의 격자. 각 지점의 누적합을 저장
    # 3. heap: 각 지점의 누적합, 각 지점의 위치를 보관하는 리스트. heapq로 알고리즘을 구현하는 핵심 파츠
# 4. 핵심 로직: 
    # 1. if cost > dist[r][c] / continue: 이미 더 좋은 방법을 찾았다면, 구시대의 유물은 갖다 버리는 코드
    # 2. 델타 탐색: 상하좌우를 미리 리스트로 선언해두고, 반복문으로 최소 누적합 주변을 탐색
    # 3. relaxation(거리 갱신): 
    #    if new_cost < dist[nr][nc]:
    #       dist[nr][nc] = new_cost
    #       heap에 (new_cost, nr, nc)를 넣는다.
# 5. 종료: while heap: 이 종료될 때. 그렇게 되면 모든 dist가 최소 누적합으로 가득 차게 됨. 이 때 dist[N - 1][N - 1]을 구하면 됨
import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]

    INF = float('inf')  # 이게 무한이다.
    dist = [[INF] * N for _ in range(N)]

    heap = [(0, 0, 0)]
    dist[0][0] = 0

    while heap:
        cost, r, c = heapq.heappop(heap)
        if cost > dist[r][c]:
            continue

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                new_cost = cost + grid[nr][nc]

                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))

    print(f'#{tc} {dist[N - 1][N - 1]}')