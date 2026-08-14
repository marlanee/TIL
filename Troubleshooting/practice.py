# 26-08-14. 2차 시도:
from collections import deque

for i in range(1, 11):
    _ = input()
    numbers = deque(map(int, input().split()))

    minus_num = 1

    while True:
        x = numbers.popleft() - minus_num

        if x <= 0:
            numbers.append(0)
            break

        numbers.append(x)

        minus_num = (minus_num % 5) + 1

    print(f'#{i}', *numbers)