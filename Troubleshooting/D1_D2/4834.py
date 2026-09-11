# SWEA 4834. 숫자 카드

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input()))

    bag = {}

    for n in numbers:
        bag.setdefault(n, [])
        bag[n].append(n)

    target = 0
    sub = 0

    for key, value in bag.items():
        if len(value) > target:
            target = len(value)
        elif len(value) == target:
            if key > sub:
                sub = key

    print(f'#{tc} {sub} {target}')