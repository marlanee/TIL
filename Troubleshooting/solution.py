# 261108. SWEA 차량 정비소
# 3차 시도: 40분(PASS)

"""
목표: N개의 접수 창구, M개의 정비 창구가 주어진다.
    1. K명의 고객이 정비소를 방문한다. 고객번호가 1~K번까지 주어진다.
    2. 접수 창구의 규칙
        1. 여러 고객이 기다리면 낮은 고객번호가 우선한다
        2. 빈 창구가 여러개면 접수 창구번호가 작은 곳으로 간다
    3. 정비 창구의 규칙
        1. 먼저 기다리는 고객이 우선한다
        2. 접수 창구번호가 작은 고객이 우선한다
        3. 정비 창구번호가 작은 곳으로 간다
    4. A, B 접수창구 및 정비창구를 이용한 고객번호의 합을 구하라
핵심로직: 시뮬레이션
    1. 정비 창구 이용 고객 처리 / 정비 창구 -> 완료
    2. 접수 창구 이용 고객 처리 / 접수 창구 -> 정비 대기열
    3. 정비 대기열 고객 처리 / 정비 대기열 -> 정비 창구
    4. 도착 고객 처리 / 도착 -> 접수 대기열
    5. 접수 대기열 고객 처리 / 접수 대기열 -> 접수 창구
시간복잡도:
"""
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())

    receipt_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    arrival_time = list(map(int, input().split()))

    finish = 0
    customers = [[-1, -1] for _ in range(K)]

    receipt_using = [[-1, -1] for _ in range(N)]
    repair_using = [[-1, -1] for _ in range(M)]

    receipt_waiting = deque()
    repair_waiting = deque()

    current_time = 0

    while finish != K:
        # 1. 정비 창구 처리
        for idx, (user, time) in enumerate(repair_using):
            if time != -1:
                time += 1
                if time == repair_time[idx]:
                    finish += 1
                    repair_using[idx] = [-1, -1]
                    continue
                repair_using[idx] = [user, time]

        # 2. 접수 창구 처리
        for idx, (user, time) in enumerate(receipt_using):
            if time != -1:
                time += 1
                if time == receipt_time[idx]:
                    repair_waiting.append([user, 0])
                    receipt_using[idx] = [-1, -1]
                    continue
                receipt_using[idx] = [user, time]

        # 3. 정비 대기열 처리
        for idx, (r, t) in enumerate(repair_using):
            if not repair_waiting:
                break
            if r == -1:
                user, time = repair_waiting.popleft()
                customers[user][1] = idx + 1
                repair_using[idx] = [user, 0]

        # 4. 도착 고객 처리
        for user, s in enumerate(arrival_time):
            if s == current_time:
                receipt_waiting.append([user, 0])

        # 5. 접수 대기열 고객 처리
        for idx, (r, t) in enumerate(receipt_using):
            if not receipt_waiting:
                break
            if r == -1:
                user, time = receipt_waiting.popleft()
                customers[user][0] = idx + 1
                receipt_using[idx] = [user, 0]

        current_time += 1

    total = 0

    for idx, (a, b) in enumerate(customers):
        if (a, b) == (A, B):
            total += idx + 1

    if total == 0:
        total = -1

    print(f'#{tc} {total}')