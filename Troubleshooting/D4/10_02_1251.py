# SWEA 1251. 하나로.

# 1차 시도: PASS(30분)
# 9. 23. 복습 필요
# 복습: PASS(40분)
# 10.2. 복습 필요

# 목표: 각 섬을 모두가 연결되도록, 다만 최소의 거리로 연결되도록 연결하고 그 비용을 구하라.
# 상태: visited = MST에 포함된 섬인지 여부 / dist = 현재 MST와 각 섬을 연결하는 최소 비용
# 자료구조: Prim, visited, dist
# 핵심로직:
    # 1. 행복하지 않은 섬 중 dist가 가장 작은 섬을 선택
    # 2. 해당 섬을 MST에 포섭하고 total에 비용 추가
    # 3. 새로 추가된 섬을 기준으로 나머지 섬의 dist 갱신
    # 4. 모든 섬이 MST에 포섭될 때까지 반복
# 종료조건: while 반복문이 종료될 때

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())

#     X = list(map(int, input().split()))
#     Y = list(map(int, input().split()))
#     E = float(input())

#     visited = [False] * N

#     dist = [float('inf')] * N

#     dist[0] = 0

#     total = 0

#     for _ in range(N):

#         min_cost = float('inf')
#         current = -1

#         for i in range(N):
#             if not visited[i] and dist[i] < min_cost:
#                 min_cost = dist[i]
#                 current = i

#         visited[current] = True
#         total += min_cost

#         for next_node in range(N):

#             if visited[next_node]:
#                 continue

#             dx = X[current] - X[next_node]
#             dy = Y[current] - Y[next_node]

#             cost = dx * dx + dy * dy

#             if cost < dist[next_node]:
#                 dist[next_node] = cost

#     answer = round(total * E)
    
#     print(f'#{tc} {answer}')

# SWEA 1251. 하나로.

# 복습: PASS(40분)
# 10.2. 복습 필요

# 목표: 섬들이 주어진다. 섬들이 가장 짧은 길이의 선분으로 연결되도록 연결하라.
# 상태: visited = 이미 연결한 섬인지, 아닌지 판별. dist = MST에 속한 섬 그룹과 해당 섬의 현재 최소 거리
# 자료구조: Prim
# 핵심 로직: 
    # 1. visited로 MST에 속했는지를 확인 가능함
    # 2. dist를 MST에 새로운 섬이 올 떄마다 갱신함. -> 연산량이 줄어드는 효과
# 종료 조건: len(known) == N, 비용 출력

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    visited = [False] * N
    dist = [float('inf')] * N
    current = 0
    dist[0] = 0

    known = []

    while len(known) < N:

        min_count = float('inf')

        for i in range(N):
            if not visited[i]:
                if dist[i] < min_count:
                    min_count = dist[i]
                    current = i

        visited[current] = True
        known.append(current)

        for j in range(N):
            if not visited[j]:
                cal = abs(X[current] - X[j]) ** 2 + abs(Y[current] - Y[j]) ** 2
                dist[j] = min(dist[j], cal)

    cost = sum(dist) * E

    print(f'#{tc} {round(cost)}')