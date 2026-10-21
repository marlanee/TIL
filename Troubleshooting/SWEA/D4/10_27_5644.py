# SWEA 5644. 무선 충전
# 10. 20. 1차 시도: FAIL(2시간) / 구현 완성도 부족
# 10. 27. 복습 필요

"""
목표: BC들이 설치되어 있는 10 x 10 지도가 주어진다. 
    1. 사용자 A, B가 주어진 궤적으로 이동한다
    2. 이동하며 (C)맨해튼 거리 안에 있는 BC로 뭔가를 충전한다.
    3. 매 초마다 해당 BC의 P만큼 충전한다
    4. 여러 BC의 C에 들어왔을 때, 하나를 선택해 접속이 가능하다
    5. A, B가 동일한 BC를 선택할수도 있으나, 효율이 절반이 된다
    6. A, B가 M시간만큼 이동한 후, 가능한 최대 충전량을 구하라
상태: 
    1. info_A, B = A, B의 이동 궤적
    2. BC = BC들의 (X, Y, C, P)가 담긴 리스트
자료구조: DFS, 델타 이동
핵심 로직:
    1. while < M: / M시간동안 반복
    2. A의 선택지 확인
        1. BC를 순회하며 맨해튼 거리가 C보다 작거나 같으면 index를 선택지에 넣음
    3. B의 선택지 확인
        2. BC를 순회하며 맨해튼 거리가 C보다 작거나 같으면 index를 선택지에 넣음
    4. 고르는 방법 완전탐색
        1. 같은걸 고르는 경우
        2. 다른걸 고르는 경우
    5. 탐색 종료 후 산출한 최댓값을 누적시킴
종료조건: 시간이 M이 되었을 때
시간 복잡도:
"""

# dx = [0, 0, 1, 0, -1]
# dy = [0, 1, 0, -1, 0]

# T = int(input())
# for tc in range(1, T + 1):
#     M, A = map(int, input().split())
#     info_A = list(map(int, input().split()))
#     info_B = list(map(int, input().split()))
#     BC = [list(map(int ,input().split())) for _ in range(A)]

#     t = 0 
#     total = 0
#     ax, ay = 1, 1
#     bx, by = 10, 10

#     while t < M + 1:
#         max_current = 0 # t 시간일 때 최대 충전량
#         A_current = []  # A의 BC 선택지
#         B_current = []  # B의 BC 선택지

#         for idx, (x, y, c, p) in enumerate(BC):
#             if abs(x - ax) + abs(y - ay) <= c:
#                 A_current.append(idx)
#             if abs(x - bx) + abs(y - by) <= c:
#                 B_current.append(idx)

#         if A_current and B_current: # 둘 다 충전할 BC가 있을 경우 완전탐색
#             for a in A_current:
#                 for b in B_current:
#                     if a == b:
#                         max_current = max(max_current, BC[a][3])
#                     else:
#                         max_current = max(max_current, BC[a][3] + BC[b][3])
#         elif A_current:   # A_current만 참일경우
#             for a in A_current:
#                 max_current = max(max_current, BC[a][3])
#         elif B_current:
#             for b in B_current:
#                 max_current = max(max_current, BC[b][3])

#         t += 1
#         total += max_current

#         if t >= M:
#             break

#         ax = ax + dx[info_A[t]]
#         ay = ay + dy[info_A[t]]
#         bx = bx + dx[info_B[t]]
#         by = by + dy[info_B[t]]
#         print((ax, ay), (bx, by))
#         print(info_B[t], (dx[info_B[t]], dy[info_B[t]]))


#     print(f'#{tc} {total}')

dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    info_A = list(map(int, input().split()))
    info_B = list(map(int, input().split()))
    BC = [list(map(int ,input().split())) for _ in range(A)]

    t = 0 
    total = 0
    ar, ac = 1, 1
    br, bc = 10, 10

    for t in range(M + 1):
        if t > 0:
            ar = ar + dr[info_A[t - 1]]
            ac = ac + dc[info_A[t - 1]]
            br = br + dr[info_B[t - 1]]
            bc = bc + dc[info_B[t - 1]]

        max_current = 0 # t 시간일 때 최대 충전량
        A_current = []  # A의 BC 선택지
        B_current = []  # B의 BC 선택지

        for idx, (x, y, c, p) in enumerate(BC):
            if abs(x - ac) + abs(y - ar) <= c:
                A_current.append(idx)
            if abs(x - bc) + abs(y - br) <= c:
                B_current.append(idx)

        if A_current and B_current: # 둘 다 충전할 BC가 있을 경우 완전탐색
            for a in A_current:
                for b in B_current:
                    if a == b:
                        max_current = max(max_current, BC[a][3])
                    else:
                        max_current = max(max_current, BC[a][3] + BC[b][3])
        elif A_current:   # A_current만 참일경우
            for a in A_current:
                max_current = max(max_current, BC[a][3])
        elif B_current:
            for b in B_current:
                max_current = max(max_current, BC[b][3])

        t += 1
        total += max_current

    print(f'#{tc} {total}')