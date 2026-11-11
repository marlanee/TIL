# 261111. SWEA 1265. 달란트2
# 1차 시도: PASS(14분)

"""
목표: N개의 숫자와 P의 묶음 수가 주어진다.
    1. P 묶음의 수의 합은 N이다
    2. 이 때 P묶음의 최대 곱을 구하시오.
핵심 로직:
    1. 최대값을 구하기 위해 숫자를 배분하려면, 최대한 균등하게 쪼개야 한다
    2. 우선 N을 P로 나눈 후 그 값을 각 묶음에 더한다
    3. 집합의 합이 N이 될 때까지 각 묶음에 1을 더한다
    4. 각 묶음의 곱을 출력한다.
시간복잡도: O(P)
"""

T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())

    start = N // P

    bucket = [start] * P
    current = start * P

    for i in range(P):
        if current == N:
            break
        bucket[i] += 1
        current += 1

    total = 1
    for b in bucket:
        total *= b

    print(f'#{tc} {total}')