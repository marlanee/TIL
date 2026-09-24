# SWEA 1251. 하나로.

# 1차 시도: PASS(30분)
# 9. 23. 복습 필요

# 목표: 각 섬을 모두가 연결되도록, 다만 최소의 거리로 연결되도록 연결하고 그 비용을 구하라.
# 상태: visited = MST에 포함된 섬인지 여부 / dist = 현재 MST와 각 섬을 연결하는 최소 비용
# 자료구조: Prim, visited, dist
# 핵심로직:
    # 1. 행복하지 않은 섬 중 dist가 가장 작은 섬을 선택
    # 2. 해당 섬을 MST에 포섭하고 total에 비용 추가
    # 3. 새로 추가된 섬을 기준으로 나머지 섬의 dist 갱신
    # 4. 모든 섬이 MST에 포섭될 때까지 반복
# 종료조건: while 반복문이 종료될 때

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    visited = [False] * N

    dist = [float('inf')] * N

    dist[0] = 0

    total = 0

    for _ in range(N):

        min_cost = float('inf')
        current = -1

        for i in range(N):
            if not visited[i] and dist[i] < min_cost:
                min_cost = dist[i]
                current = i

        visited[current] = True
        total += min_cost

        for next_node in range(N):

            if visited[next_node]:
                continue

            dx = X[current] - X[next_node]
            dy = Y[current] - Y[next_node]

            cost = dx * dx + dy * dy

            if cost < dist[next_node]:
                dist[next_node] = cost

    answer = round(total * E)
    
    print(f'#{tc} {answer}')