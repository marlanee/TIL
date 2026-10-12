# SWEA 1247. 최적 경로
# 1차 시도: PASS(30분)
# 졸업
# 풀고 보니 D5 문제였다. 얼탱

"""
목표: 
    1. 회사에서 출발해 N명의 고객 집을 방문한 후 집으로 돌아가려 한다.
    2. 가장 짧은 경로의 길이를 구하시오
상태: visited = 이미 방문한 고객 집, customer = 방문한 고객 수, length = 현재까지의 길이, 마지막으로 선택한 고객의 집 좌표
자료구조: DFS / 백트래킹 / visited
핵심로직:
    # Prim처럼 보이지만, 그렇지 않음. 연결 거리가 아닌 이동 거리를 구해야 하기 때문
    1. 가능한 좌표 방문 순서를 모두 탐색하여 최솟값을 갱신함
    2. dfs(x, y, customer, length)
    3. if customer == N: x, y 와 집의 거리를 더한 후 최솟값 갱신
    4. 가지치기: length >= min_length + 200
종료조건: customer == N / 
시간복잡도: O(N!)
"""

def dfs(x, y, customer, length):
    global min_length

    if length >= min_length:
        return

    if customer == N:
        current = abs(coordinates[2] - x) + abs(coordinates[3] - y)
        min_length = min(min_length, current + length)
        return

    for i in range(4, 2 * N + 4, 2):
        if not visited[i//2]:
            visited[i//2] = True
            cx, cy = coordinates[i], coordinates[i + 1]
            current = abs(x - cx) + abs(y - cy)
            dfs(cx, cy, customer + 1, length + current)
            visited[i//2] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    coordinates = list(map(int, input().split()))

    visited = [False] * (N + 2)
    min_length = float('inf')

    dfs(coordinates[0], coordinates[1], 0, 0)

    print(f'#{tc} {min_length}')
