# 261111. SWEA 1245. 균형점
# 1차 시도: FAIL(1시간)
# 학습 내용: 이분 탐색

"""
목표: n개의 자성체들이 x축에 일렬로 있다
    1. 양쪽의 힘이 같은 균형점들의 x 좌표를 구하라
    2. n개의 자성체가 있다면 n - 1개의 균형점이 존재한다.
핵심 로직: 
    1. 이분 탐색.
    2. 인접한 자성체 두 개를 선택해서 그 사이에 있는 균형점을 구한다
    3. 중점을 설정하고 어디쪽 중력이 강한지 계산한다
    4. 큰 중력의 반대 방향으로 균형점은 이동해야 한다.
    5. 이에 따라 lo나 hi의 위치를 조정한다. 놀랍게도, 기존의 절반은 버릴 수 있다.
    6. 그래서 O(log N)이 나오지만.. 최종 시간복잡도는 다르다.
"""
# 이게 말이 되는 문제인가? 맨 왼쪽에 ton618이 있고 오른쪽에는 쫌쫌따리 지구별 행성밖에 없으면 균형점이 어떻게 존재해?

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    magnets = list(map(int, input().split()))
    X = magnets[:N]
    mass = magnets[N:]

    total = []

    for i in range(N - 1):
        lo = X[i]
        hi = X[i + 1]

        for _ in range(100):
            mid = (lo + hi) / 2

            left_force = 0
            right_force = 0

            for j in range(N):
                d = X[j] - mid
                gravity = mass[j] / (d * d)
                if j <= i:
                    left_force += gravity
                else:
                    right_force += gravity

            if left_force > right_force:
                lo = mid
            else:
                hi = mid

        total.append((lo + hi) / 2)

    print(f'#{tc}', *[f"{z:.10f}" for z in total])