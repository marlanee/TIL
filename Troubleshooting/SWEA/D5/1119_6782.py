# 261112. SWEA 6782. 현주가 좋아하는 제곱근 놀이
# 1차 시도: FAIL(17분)
# 11. 19. 복습 필요 / 학습 내용, 제곱근, 그리디

"""
목표: 2이상의 정수 N이 주어진다.
    1. 다음의 규칙을 거쳐 N을 2로 만드려 한다
        1. N을 N + 1로 바꿀 수 있다
        2. 루트 N이 정수일 때, N을 루트 N으로 바꿀 수 있다.
    2. N을 2로 만들기 위해 조작해야 하는 횟수의 최솟값을 구하라.
핵심 로직:
    1. 루트 N 변환이 가능할때마다 변환하는게 정답 아닐까? 아닌가?
    2. 만약 아니라면 DFS 돌려야 되는데, 흠..
    3. 1번의 증명이 안 되니까 DFS 돌리자.
"""
# def dfs(N, count):
#     global min_count

#     if count >= min_count:
#         return

#     if N == 2:
#         min_count = count
#         return

#     root_N = N ** 0.5

#     if root_N == int(root_N):
#         dfs(root_N, count + 1)

#     dfs(N + 1, count + 1)


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())

#     min_count = float('inf')

#     dfs(N, 0)

#     print(f'#{tc} {min_count}')

import math

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    count = 0

    while N > 2:
        root = math.isqrt(N)

        if root * root < N:
            root += 1

        next_square = root * root

        count += next_square - N + 1

        N = root

    print(f'#{tc} {count}')