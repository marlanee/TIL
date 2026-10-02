T = int(input())
for tc in range (1, T+1):
    N,M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sum_max = 0

    for r in range(N-M+1):
        for c in range(N-M+1):
            total = 0
            for i in range(M):
                for j in range(M):
                    total += arr[r+i][c+j]

                    if total > sum_max:
                        sum_max = total



    print(f'#{tc} {sum_max}')   