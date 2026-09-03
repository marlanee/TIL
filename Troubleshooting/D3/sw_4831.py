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

# T = int(input())

# for tc in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     stations = [0] + list(map(int, input().split())) + [N]

#     count = 0
#     cur_idx = 0

#     while cur_idx < len(stations) - 1:
#         # 1. 다음 충전소까지 거리가 K보다 크면 절대 도달 불가
#         if stations[cur_idx + 1] - stations[cur_idx] > K:
#             count = 0
#             break

#         next_idx = cur_idx
#         while next_idx + 1 < len(stations) and stations[next_idx + 1] - stations[cur_idx] <= K:
#             next_idx += 1

#         if next_idx == len(stations) - 1:
#             break

#         cur_idx = next_idx
#         count += 1

# print(f'{tc} {count}')

# 전기 버스. 풀이 시간: 16:45

# 1. 목표: 최소한의 충전 횟수로 목적지에 도달하고, 충전 회수를 구하는 것
# 2. 구조: 
    # 1. 버스의 위치를 l로 설정
    # 2. l + K < 충전기 거리일 경우 0 출력
    # 3. l + K 거리 안에 충전기가 여러개 일 경우 l + K 내의 가장 큰 충전기로 이동
    # 4. l + K >= N 일 경우 종료
# 3. 종료: l + K >= N 일 경우.

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split()) # K는 최대 이동 거리, N은 정류장의 개수, M은 충전기의 개수
    stations = list(map(int, input().split()))  # 충전기의 위치 stations의 약자

    current = 0   # 버스의 출발 위치
    count = 0   # 충전을 몇 번 했는지를 담는 변수
    rs = stations[::-1]

    while current + K < N:
        for i in range(M):
            if current + K >= rs[i] and current < rs[i]:
                current = rs[i]
                count += 1
                break
        else:
            count = 0
            break
        
    print(f'#{tc} {count}')