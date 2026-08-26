# 2026-08-26. 1차 시도: 12:31

# 완전 탐색인가? 설마, 아니겠지.
# 모든 경우의 수를 따져볼게. 일단은.
T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))

    count = 0

    for i in len(station):
        if station[0] > K:
            break
        if 


