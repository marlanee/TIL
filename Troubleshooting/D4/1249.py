# 보급로. 1차 시도: FAIL / 2차 시도: PASS(180분)
# 보급로. 2차 시도: PASS(32분)
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
# import heapq

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     grid = [list(map(int, input())) for _ in range(N)]

#     INF = float('inf')  # 이게 무한이다.
#     dist = [[INF] * N for _ in range(N)]

#     heap = [(0, 0, 0)]
#     dist[0][0] = 0

#     while heap:
#         cost, r, c = heapq.heappop(heap)
#         if cost > dist[r][c]:
#             continue

#         dr = [1, -1, 0, 0]
#         dc = [0, 0, 1, -1]

#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]

#             if 0 <= nr < N and 0 <= nc < N:
#                 new_cost = cost + grid[nr][nc]

#                 if new_cost < dist[nr][nc]:
#                     dist[nr][nc] = new_cost
#                     heapq.heappush(heap, (new_cost, nr, nc))

#     print(f'#{tc} {dist[N - 1][N - 1]}')

# 보급로. 2차 시도: PASS(32분)

# 1. 목표: 2차원 행렬에서 (0, 0)부터 (N - 1, N - 1)까지 가는 길의 최소 누적합 구하기
# 2. 상태: dist[r][c] 를 누적합으로 관리할 것
# 3. 자료구조
    # 1. grid: 행렬 좌표로 가기 위한 비용을 담은 2차원 행렬
    # 2. dist: 행렬 좌표로 가기 위한 누적합을 담은 행렬
    # 3. heap: 최소 누적합을 찾기 위한 관리 리스트.
# 4. 핵심 로직
    # 1. heapq 라이브러리를 호출해서, heap 리스트에서 최소 cost부터 탐색
    # 2. if cost > dist[r][c] 일 경우 구시대의 낡은 유물이므로 continue
    # 3. new_cost = cost + grid[nr][nc] 로 그 길의 새로운 누적합 변수 선언
    # 4. if new_cost < dist[nr][nc] 일 경우 dist[nr][nc]로 누적합 갱신(relaxation)
    # 5. 갱신이 되었다면, heap에 추가. heapq.heqppush(heap, (new_cost, nr, nc))
    # 6. 델타 이동 사용. cost, r, c = heapq.heappop(heap)으로 꺼내서, 델타 이동으로 최소 cost 주위의 누적합을 탐색
# 5. 종료: heap에서 r == N - 1, c == N - 1에 해당하는 값이 튀어나왔을 경우. 
    # 1. 목적지가 heap에서 pop된 순간, 그 비용은 최솟값으로 확정된다.
import heapq

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input())) for _ in range(N)]

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]

    heap = [(0, 0 ,0)]  # 초기 시작시 비어있으면 안 되므로, (0, 0)의 값을 미리 넣어준다.

    dist[0][0] = 0  # 시작점까지의 최소 비용은 0이다.

    while heap:
        cost, r, c = heapq.heappop(heap)

        if cost > dist[r][c]:   # 구시대의 유물은 버린다.
            continue

        if r == N - 1 and c == N - 1:
            break

        for i in range(4):  # 4방향으로 탐색한다. 델타 이동
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:     # 격자를 넘어가면 안되므로, 한계 설정
                new_cost = cost + grid[nr][nc]  # 이 길로 갔을 때, 그 좌표의 새로운 누적합이다.

                if new_cost < dist[nr][nc]: # 기존에 구해둔 누적합보다 새로운 누적합이 작으면 갱신한다.
                    dist[nr][nc] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc))  # 나중에 신규 누적합 경로에서 시작할 수 있도록 heap 리스트에 추가한다.

    print(f'#{tc} {dist[N - 1][N - 1]}')