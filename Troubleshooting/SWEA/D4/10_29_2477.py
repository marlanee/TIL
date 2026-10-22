# SWEA 2477. 차량 정비소
# 26. 10. 22
# 1차 시도: FAIL(2시간)
# 10. 26. 복습 필요

"""
목표: 차량 정비소에 접수 창구와 정비 창구가 있다.
    1. A 접수 창구와 B 정비 창구를 이용한 손님 고객번호의 합을 구하라
    2. 손님들은 각기 다른 시간에 도착하며 아래의 규칙에 따라 창구를 이용한다.
    3. 접수 창구: 
        0. 고객이 도착하면 접수 창구번호가 작은 곳부터 채운다.
        1. 접수 창구가 가득 차 있으면 초과한 고객들은 기다린다.
        2. 여러 고객이 기다릴 경우 고객번호가 낮은 순서대로 우선 접수
    4. 정비 창구:
        1. 고객이 도착하면 정비 창구번호가 작은 곳부터 채운다.
        2. 여러 고객이 기다릴 경우, 먼저 기다린 고객을 우선한다
        3. 두 명이 동시에 접수 창구로 왔다면, 접수 창구번호가 작은 고객을 우선
상태: 
    1. waiting_reception = 접수 창구 대기명단
    2. using_reception = 접수 창구 이용자 명단
    3. waiting_repair = 정비 창구 대기명단
    4. using_repair = 정비 창구 이용자 명단
자료구조: 단순 반복문
핵심로직:
    1. while arrival and using_reception and using_repair and waiting_reception:
    2. using_repair에 있는 고객들의 using_time 을 1 줄인다.
        1. using_time == 0일 경우 그 창구를 비운다.
    3. using_reception에 있는 고객들의 using_time을 1 줄인다
        1. using_time == 0일 경우 그 창구를 비우고 waiting_repair로 이동한다.
    4. waiting_repair에 있는 손님들을 using_repair에 넣는다
        0. 창구가 비워져 있을 경우에만 넣는다,
        1. 이 때, user_log[손님 번호]에 repair 번호를 append
    5. arrival을 1 감소시킨다. 
        1. 0이 된 손님은 waiting_reception에 넣는다
        2. arrival에서 제거한다. / continue로 해결
    6. waiting_reception에 있는 고객들을 using_reception에 넣는다
        1. 창구가 비워져 있을 경우에만 넣는다.
        2. 이 때 user_log[손님 번호]에 reception 번호를append
종료 조건: 도착할 손님, 이용중인 고객, 대기중인 고객이 모두 없을 때.
"""

T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    arrival = list(map(int, input().split()))

    waiting_reception = []
    using_reception = [(_, 0) for _ in range(N)]
    waiting_repair = []
    using_repair = [(_, 0) for _ in range(M)]
    user_log = [[] for _ in range(K)]
    completed = 0
    time = 0

    while completed < K:
        next_waiting_reception = []
        next_waiting_repair = []
        next_arrival = []

        for idx, (person, using_time) in enumerate(using_repair):
            if using_time > 0:
                using_time -= 1

                if using_time == 0:
                    completed += 1
                    using_repair[idx] = (-1, 0)
                else:
                    using_repair[idx] = (person, using_time)

        for idx, (person, using_time) in enumerate(using_reception): 
            using_time -= 1
            
            if using_time == 0:
                next_waiting_repair.append((person, using_time))
            using_reception[idx] = (person, using_time)

        next_waiting_repair.sort()

        for person, using_time in next_waiting_repair:
            waiting_repair.append((person, using_time))

        for w_person, w_using_time in waiting_repair:   # 먼저 기다리던 사람들을 정비 창구 이용하도록
            assigned = False
            for idx, (person, using_time) in enumerate(using_repair):
                if using_time <= 0:
                    using_repair[idx] = (w_person, repair[idx])
                    user_log[w_person].append(idx)
                    assigned = True
                    break
            if not assigned:
                next_waiting_repair.append((w_person, w_using_time))

        for person, arrival_time in enumerate(arrival):
            if arrival_time == time:
                waiting_reception.append((person, 0))

        for w_person, w_using_time in waiting_reception:
            assigned = False
            for idx, (person, using_time) in enumerate(using_reception):
                if using_time <= 0:
                    using_reception[idx] = (w_person, reception[idx])
                    user_log[w_person].append(idx)
                    assigned = True
                    break
            if not assigned:
                next_waiting_reception.append((w_person, w_using_time))

        waiting_reception = next_waiting_reception
        waiting_repair = next_waiting_repair
        arrival = next_arrival
        time += 1

    total = 0
    
    for person, (a, b) in enumerate(user_log):
        if (a, b) == (A - 1, B - 1):
            total += 1 + person

    print(f'#{tc} {total}')




                

        

