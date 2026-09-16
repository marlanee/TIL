from collections import deque


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = deque(map(int, input().split()))

    for i in range(M):
        numbers.append(numbers.popleft())

    print(f'#{tc} {numbers[0]}')