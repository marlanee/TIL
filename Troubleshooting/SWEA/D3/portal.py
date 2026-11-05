T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    portal = list(map(int, input().split()))

    visited = [False] * N
    visited[0] = True

    total = 0

    point = 0

    while point < N - 1:

        if not visited[point]:
            visited[point] = True
            point = portal[point] - 1
        else:
            point += 1

        total += 1

    print(f'#{tc} {total}')