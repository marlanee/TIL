T = int(input())
for tc in range(1, T + 1):
    N, numbers = input().split()

    result = ''

    for n in numbers:
        result += format(int(n, 16), 'b04')

    print(f'#{tc} {result}')