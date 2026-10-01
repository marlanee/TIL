# SWEA 1251. 하나로.
# 2차 복습: PASS(40분)

"""
목표: x, y 좌표로 섬들이 주어진다. 가장 짧은 거리로 모든 섬들을 연결하라. 그 후 거리 * 비용 값을 구하라
상태: selected = 이미 연결된 섬인지 확인하는 리스트, dist = 현재 측정한 MST와 섬 거리의 최솟값
자료구조: Prim, selected
핵심로직: count == N 이 될 때까지 MST에 계속 섬을 영입함
종료조건: count == N일 때
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    total = 0
    selected = [False] * N
    dist = [float('inf')] * N

    dist[0] = 0

    for _ in range(N):

        current = float('inf')

        for idx, d in enumerate(dist):
            if not selected[idx] and d < current:
                current = d
                count = idx

        selected[count] = True
        total += current

        for i in range(N):
            if not selected[i]:
                long = (X[count] - X[i]) ** 2 + (Y[count] - Y[i]) ** 2
                dist[i] = min(dist[i], long)

    result = round(total * E)

    print(f'#{tc} {result}')