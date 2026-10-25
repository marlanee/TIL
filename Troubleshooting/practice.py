# 26. 10. 26
# SWEA 2117. 홈 방범 서비스.
# 1차 복습: PASS(30분)
# 졸업

"""
목표: N * N 크기의 도시가 주어진다.
    1. 이 곳에 마름모 모양으로 홈방범 서비스를 제공하려고 한다.
    2. 비용은 마름모 모양의 영역과 일치한다
    3. 한 집에 방법 서비스를 제공하면 M 가격을 받는다
    4. 이익이 0 이상이 되는 선에서 가장 많은 집들에 서비스를 제공하라.
상태: 
    1. max_house = 현재까지 찾은 최대 방법 서비스 집의 개수
자료구조: 단순 반복문
핵심로직:
    1. K == N - 1까지 반복문을 돌린다.
    2. grid를 순회하며 K만큼의 마름모 범위로 가장 많은 집들에 서비스를 제공하는지 확인한다
        1. 단, 이익이 0 이상이어야 한다.
종료조건: 가장 큰 K 반복문이 종료되었을 때, 최대값 출력
시간복잡도:
"""

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_house = 0

    for K in range(1, N + 2):
        cost = K * K + (K - 1) * (K - 1)
        for row in range(N):
            for col in range(N):
                current_house = 0

                # 마름모 범위 탐색
                for r in range(row - K + 1,row + K):
                    for c in range(col - K + 1, col + K):
                        # 범위가 나갔는지 제한.
                        if not (0 <= r < N and 0 <= c < N):
                            continue

                        if (abs(r - row) + abs(c - col)) > K - 1:
                            continue

                        if grid[r][c] == 1:
                            current_house += 1

                # 탐색 종료 후 최댓값 갱신
                if max_house < current_house:
                    if cost <= current_house * M:
                        max_house = current_house

    print(f'#{tc} {max_house}')