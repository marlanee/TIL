# 2026-08-12 # 1차 시도: PASS (풀이 시간:45분)
# 농작물 수확하기
# 이번에도 2차원 행렬 문제다. 다만 크기가 항상 홀수이다. (1 ~ 49)
# 정사각형 마름모에 해당하는 행렬의 총합을 반환하면 된다.

# T = int(input())

# for i in range(1, T + 1):
#     N = int(input())
#     if N == 1:
#         print(f'#{i} {int(input())}')
#         continue
#     grid = [list(map(int, input().strip())) for _ in range(N)]   # 리스트 컴프리헨션으로 깔끔하게 농장 grid 생성

#     # 자 이제 농작물을 수확하자. 어떤 알고리즘을 사용해야 할까?
#     # for 반복문으로 i가 N이 될 때까지 
#     sum_total = 0
#     K = N // 2
#     sum_total += grid[0][K]
#     sum_total += grid[N-1][K]
#     for x in range(1, K):
#         sum_total += sum(grid[x][K - x:K + x + 1])
#         if x + K  + 2== N:
#             break

#     minus_num = 0
#     for y in range(K, N):
#         sum_total += sum(grid[y][minus_num:N - minus_num])
#         minus_num += 1
#         if K - minus_num == 0:
#             break
#     print(f'#{i} {sum_total}')

# 위 코드는 내 코드, 아래는 gemini의 코드. 수준 차이를 보라.
T = int(input())

for i in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().strup()) for _ in range(N))]

    K = N // 2
    sum_total = 0

    for r in range(N):
        dist = abs(K - r)
        sum_total += sum(grid[r][dist:N - dist])   # 절댓값을 이용해서 수학적 대칭성을 활용했다.

    print(f'#{i} {sum_total}')

    