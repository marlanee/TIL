# SWEA 5644. 무선 충전
# 10. 20. 1차 시도: FAIL(2시간) / 구현 완성도 부족
# 10. 27. 복습 필요
# 26. 10. 30.
# SWEA 5644. 무선 충전
# 2차 시도: PASS(52분)
# 졸업

"""
목표: 10 x 10지도가 주어진다.
    1. 배터리 충전소 BC가 임의의 영역에 배치되어 있다.
    2. 사용자 두 명이 (1, 1) / (10, 10)지점에서 주어진 경로로 출발한다.
    3. 이동 중에 BC와의 거리가 맨해튼 거리 이하로 가까워지면 접속이 가능하다
    4. 여러 BC중에 연결 가능하면 연결할 BC를 선택할 수 있다
    5. 한 BC에 두 명의 사용자가 접속할 수도 있으나, 충전 양이 2분의 1로 줄어든다. / BC는 짝수
    6. 두 사용자가 모든 이동을 마치고 난 후, 충전할 수 있는 최대값을 구하라
상태:
    1. total = 현재까지 구한 충전량의 최대값
자료구조:
핵심로직:
    1. 사용자 A, B의 자리에서 선택할 수 있는 BC를 탐색한다.
        1. 배터리들의 좌표들과의 맨해튼 거리를 구한다
        2. 맨해튼 거리가 C 이하이면 선택지에 넣는다
        3. A, B 가 선택할 수 있는 BC의 경우의 수를 완전 탐색한다
            1. 이중 for문
        4. 가장 큰 값을 total에 더한다
    2. 사용자 A, B를 이동시킨다.
종료조건: 
시간복잡도: O(MA)
"""

def find_BC(r, c):
    current_list = []
    for i in range(len(BC_info)):
        if (abs(r - BC_info[i][1]) + abs(c - BC_info[i][0])) <= BC_info[i][2]:
            current_list.append(i)

    return current_list


dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    A_direction = list(map(int, input().split()))
    B_direction = list(map(int, input().split()))
    BC_info = [list(map(int, input().split())) for _ in range(A)]   # [X, Y, C, P]

    total = 0
    ar, ac = 1, 1
    br, bc = 10, 10

    T = 0

    while T < M + 1:
        current = 0

        BC_of_A = find_BC(ar, ac)
        BC_of_B = find_BC(br, bc)

        if BC_of_A and BC_of_B:
            for a in BC_of_A:
                for b in BC_of_B:
                    if a != b:
                        current = max(current, BC_info[a][3] + BC_info[b][3])
                    elif a == b:
                        current = max(current, BC_info[a][3])
        elif BC_of_A:
            for a in BC_of_A:
                current = max(current, BC_info[a][3])
        elif BC_of_B:
            for b in BC_of_B:
                current = max(current, BC_info[b][3])

        total += current

        if T == M:
            break

        ar = ar + dr[A_direction[T]]
        ac = ac + dc[A_direction[T]]
        br = br + dr[B_direction[T]]
        bc = bc + dc[B_direction[T]]

        T += 1


    print(f'#{tc} {total}')
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