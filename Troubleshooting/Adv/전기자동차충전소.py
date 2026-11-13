# 261112. 기출. 전기자동차 충전소
# 1차 시도: FAIL(90분)

"""
목표: N개의 집이 있다. 충전소는 최대 2개까지 설치한다
    1. 각 집마다 충전소까지 허용 가능한 거리 d가 주어진다. house[n][2]
    2. 최소한의 충전소를 설치했을 때, 충전소와 N개의 집 사이 거리의 합이 최소가 되도록 값을 구하라
핵심로직:
    1. 완전 탐색으로 할 수 있을 것 같다. 다만 시간복잡도가 최악 O(N^5)일거다.
        1. 30 x 30 배열에 충전소를 하나씩 두고 조건 만족하는지 확인
        2. 안된다면 배열에 충전소를 하나 두고 나머지 충전소를 옮기며 조건 만족하는지 확인
    ?. 오잉? 충전소는 정수라는 말이 없네. 흠..
    2. 그건 어떨까? 각 집마다 범위가 닿는 격자에 +1씩 더하는거다.
        1. 격자에 N에 저장되어 있으면 그곳이 정답이다.
        2. 거리 판단은 튜플로 (N, length) 이런식으로 저장해두면 판별이 쉽다.
        3. 더 나아가 거리가 닿는 집을 튜플에 넣는거다. (N, length, [house1, house2])
        4. 그러면 충전소를 두 개 설치했을 때 모든 집에 보급되었는지 확인이 가능하다!
        5. 딕셔너리에 넣으면 되겠네.
    !!! 나는 두 번째 방법을 선택하겠다.
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    house = [list(map(int, input().split())) for _ in range(N)]

    dist = {}

    house_positions = {(x, y) for x, y, _ in house}

    for idx, h in enumerate(house):
        x, y, d = h
        for r in range(- d, d + 1):
            for c in range(- d, d + 1):
                nx = x + r
                ny = y + c

                if (nx, ny) in house_positions:
                    continue

                if not (-15 <= nx <= 15 and -15 <= ny <= 15):
                    continue

                distance = abs(x - nx) + abs(y - ny)

                if distance <= d:
                    dist.setdefault((nx, ny), {})
                    dist[(nx, ny)][idx] = distance

    current = float('inf')

    for A in dist.values():
        if len(A) == N:
            current = min(current, sum(A.values()))

    # 1개로 가능하다면 즉시 종료
    if current != float('inf'):
        print(f'#{tc} {current}')
        continue

    positions = list(dist.keys())
    K = len(positions)
   

    for i in range(K - 1):
        for j in range(i + 1, K):
            A = dist[positions[i]]
            B = dist[positions[j]]

            total = 0

            for h in range(N):
                total += min(
                    A.get(h, float('inf')),
                    B.get(h, float('inf'))
                )

                if total == float('inf'):
                    break

            current = min(current, total)

    if current == float('inf'):
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {current}')