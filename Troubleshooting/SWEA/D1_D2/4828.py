# SWEA 4828. min max

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    target = max(numbers) - min(numbers)

    print(f'#{tc} {target}')