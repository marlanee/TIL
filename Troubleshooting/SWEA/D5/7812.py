"""
26.11.04.
SWEA 7812. 옥희의 OK! 부동산
1차 시도: PASS(30분)
졸업

목표: 숫자열 N, M이 주어진다.
    1. 숫자열 N에서 연속으로 선택한 숫자의 합이 M인 경우의 수를 구하여라
    2. 하나를 선택하는 것도 가능하다.
핵심로직: two-pointer algorithm
    1. N만큼 반복문 돌리기 / for right in range(N)
    2. while left <= right:
        if sum[left:right] == M:
            total += 1
시간복잡도:
"""

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    left = 0
    current_sum = 0
    total = 0

    for right in range(N):
        current_sum += numbers[right]

        while current_sum > M:
            current_sum -= numbers[left]
            left += 1

        if current_sum == M:
            total += 1

    print(f'#{tc} {total}')
        