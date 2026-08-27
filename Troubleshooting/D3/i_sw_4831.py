# 2026-08-26. 1차 시도: Half(35분)

# 완전 탐색인가? 설마, 아니겠지.
# 모든 경우의 수를 따져볼게. 일단은.
# T = int(input())
# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     station = list(map(int, input().split()))

#     count = 0
#     bus = 0

#     for i in range(M):
#         if bus >= station[i]:
#             continue
#         elif bus + K >= N:
#             break
#         elif station[i] - bus > K:
#             count = 0
#             break
#         elif i + 1 < M and station[i + 1] - bus <= K:
#             mx = 0
#             for x in range(1, M-i):
#                 if station[i+x] - bus <= K:
#                     mx = x
#             count += 1
#             bus = station[i + mx]
#             continue
#         else:
#             count += 1
#             bus = station[i]

#     if bus + K < N:
#         count = 0

#     print(f'#{tc} {count}')

# 다 풀었다. gemini의 코드 버그 피드백을 바탕으로 수정한 게 전부다.
# 잘 작동한다고 한다. 그러나.. 아쉽다.

# 아래는 Gemini의 추천 코드다.

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stations = [0] + list(map(int, input().split())) + [N]

    count = 0
    cur_idx = 0

    while cur_idx < len(stations) - 1:
        # 1. 다음 충전소까지 거리가 K보다 크면 절대 도달 불가
        if stations[cur_idx + 1] - stations[cur_idx] > K:
            count = 0
            break

        next_idx = cur_idx
        while next_idx + 1 < len(stations) and stations[next_idx + 1] - stations[cur_idx] <= K:
            next_idx += 1

        if next_idx == len(stations) - 1:
            break

        cur_idx = next_idx
        count += 1

print(f'{tc} {count}')