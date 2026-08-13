# 26-08-13. 2차 시도: 
# 농작물 수확 문제

T = int(input())

for i in range(1, T + 1):   # 테스트 케이스 T만큼 반복
    N = int(input())   # 격자의 크기

    grid = [list(map(int, input().strip())) for _ in range(N)]   # N 크기의 격자 생성

    K = N // 2
    total_profit = 0

    for x in range(N):
        an = abs(K - x)
        total_profit += sum(grid[x][an:N-an])

    print(f'#{i} {total_profit}')