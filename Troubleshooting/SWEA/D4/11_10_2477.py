# SWEA 2477. 차량 정비소
# 26. 10. 22
# 1차 시도: FAIL(2시간)
# 10. 26. 복습 필요
<<<<<<<< HEAD:Troubleshooting/SWEA/D4/11_05_2477.py
========
# 2차 실패
# 11. 10. 복습 필요
>>>>>>>> e878e5d3996c8a35183726f0c6d714ab1870080b:Troubleshooting/SWEA/D4/11_10_2477.py
'''
26. 11. 02.
SWEA 2477. 차량 정비소
2차 시도: 28분 / 16:24

목표: N개의 접수 창구의 M개의 정비 창구가 있다.
    1. K명의 고객이 차량 정비소를 방문했다.
    2. 고객이 tk초 후 정비소에 도착하면, 빈 접수 창구에 가서 고장을 접수한다
        1. 먼저 기다리는 고객이 먼저다
        2. 빈 창구가 여러 곳인 경우 접수 창구번호가 작은 곳으로 간다
    3. 빈 접수 창구가 없다면, 창구가 빌 때까지 기다린다
    4. 고장 접수가 완료되면 정비 창구로 이동한다
        1. 먼저 기다리는 고객이 우선한다
        2. 두 명 이상의 고객이 동시에 정비 창구로 갈 경우, 접수 창구번호가 작은 고객이 우선한다
        3. 빈 창구가 여러 곳일 경우 정비 창구번호가 작은 곳으로 간다.
    5. 빈 정비 창구에 가서 차량을 정비 받는다
    6. 빈 정비 창구가 없다면 빈 정비 창구가 생길 때까지 기다린다.
    7. A접수 창구와 B정비 창구를 이용한 고객들의 번호의 합을 구하라 / 없을 경우 -1을 출력
상태: 
자료구조: 시뮬레이션
핵심로직:
    0. while문을 돌림. time을 1씩 늘림 / len(finished) == K가 될때까지 극한 반복
    1. 접수 창구 대기장소로 이동: 고객들을 순회하며 도착한 고객을 대기장소로 이동시킴
    2. 접수 창구 진행도 갱신: 
        1. 최초 손님의 딕셔너리는 {1: [time + recept_time[창구번호], 창구번호]} 이다.
        2. 손님의 arrive_time[1][0] += 1
        3. 만약 arrive_time[1][0] == time이면 정비 창고 대기장소로 이동한다.
    3. 접수 창구 대기 손님들을 접수 창구로 보낸다.
    4. 정비 창구 진행도 갱신
        1. 완료되면 finish += 1
    5. 정비 창구 대기 손님들을 정비 창구로 보낸다.
    6. time += 1

종료조건:
시간복잡도:
'''

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    recept_time = list(map(int, input().split()))
    repair_time = list(map(int, input().split()))
    arrvie_time = list(map(int, input().split()))

    using_recept = [[-1, -1] for _ in range(N)]
    using_repair = [[-1, -1] for _ in range(M)]

    user_info = [[] for _ in range(K)] 

    finished = 0
    time = 0
    recept_waiting = deque()
    repair_waiting = deque()

    while finished != K:

        for user_idx, u in enumerate(arrvie_time):   # 접수 대기열에 도착한 손님 넣기
            if u == time:
                recept_waiting.append(user_idx)

        add_waiting = []

        for recept_idx, (user_idx, check) in enumerate(using_recept): # 접수 창구 진행도 갱신
            if check >= 0:
                check -= 1
                if check == 0:
<<<<<<<< HEAD:Troubleshooting/SWEA/D4/11_05_2477.py
                    repair_waiting.append(user_idx)
========
                    add_waiting.append([recept_idx, user_idx])
>>>>>>>> e878e5d3996c8a35183726f0c6d714ab1870080b:Troubleshooting/SWEA/D4/11_10_2477.py
                    using_recept[recept_idx] = [-1, -1]
                    continue
                using_recept[recept_idx] = [user_idx, check]

<<<<<<<< HEAD:Troubleshooting/SWEA/D4/11_05_2477.py
========
        # 정비 창구 대기열에 넣기
        add_waiting.sort()
        for recept_idx, user_idx in add_waiting:
            repair_waiting.append(user_idx)

>>>>>>>> e878e5d3996c8a35183726f0c6d714ab1870080b:Troubleshooting/SWEA/D4/11_10_2477.py
        for recept_idx, (user_idx, check) in enumerate(using_recept):   # 접수 대기열 -> 접수
            if not recept_waiting:
                break
            if check == -1:
                user_idx = recept_waiting.popleft()
                using_recept[recept_idx] = [user_idx, recept_time[recept_idx]]
                user_info[user_idx].append(recept_idx + 1)  # 접수 창고 번호 입력

        for repair_idx, (user_idx, check) in enumerate(using_repair):   # 정비 창구 진행도 갱신
            if check >= 0:
                check -= 1
                if check == 0:
                    finished += 1
                    using_repair[repair_idx] = [-1, -1]
                    continue
                using_repair[repair_idx] = [user_idx, check]

        for repair_idx, (user_idx, check) in enumerate(using_repair):   # 정비 대기열 -> 정비 창구
            if not repair_waiting:
                break
            if check == -1:
                user_idx = repair_waiting.popleft()
                using_repair[repair_idx] = [user_idx, repair_time[repair_idx]]
                user_info[user_idx].append(repair_idx + 1)

        time += 1

    result = 0
    for idx, (a, b) in enumerate(user_info):
        if (a, b) == (A, B):
            result += idx + 1

    if result == 0:
        result = -1

    print(f'#{tc} {result}')



from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    reception = list(map(int, input().split()))
    repair = list(map(int, input().split()))
    arrival = list(map(int, input().split()))

    # 1. 대기열
    waiting_reception = deque()
    waiting_repair = deque()

    # 2. 창구 상태
    using_reception = [None] * N
    using_repair = [None] * M

    # 고객별 이용한 접수 창구
    reception_log = [-1] * K

    time = 0
    next_customer = 0
    completed = 0
    total = 0

    while completed < K:

        # 1. 정비 완료 고객 퇴장.
        for idx in range(M):
            if using_repair[idx] is None:
                continue

            person, end_time = using_repair[idx]

            if end_time == time:
                using_repair[idx] = None
                completed += 1

        # 2. 접수 완료 고객 -> 정비 대기열
        for idx in range(N):
            if using_reception[idx] is None:
                continue

            person, end_time = using_reception[idx]

            if end_time == time:
                waiting_repair.append(person)
                using_reception[idx] = None

        # 3. 현재 시각에 도착한 고객 -> 접수 대기열
        while next_customer < K and arrival[next_customer] == time:
            waiting_reception.append(next_customer)
            next_customer += 1

        # 4. 접수 대기 고객 -> 빈 접수 창구
        for idx in range(N):
            if using_reception[idx] is None and waiting_reception:
                person = waiting_reception.popleft()

                reception_log[person] = idx
                using_reception[idx] = (person, time + reception[idx])

        # 5. 정비 대기 고객 -> 빈 정비 창구
        for idx in range(M):
            if using_repair[idx] is None and waiting_repair:
                person = waiting_repair.popleft()

                using_repair[idx] = (person, time + repair[idx])

                # A번 접수 창구와 B번 정비 창구 이용 확인
                if reception_log[person] == A - 1 and idx == B - 1:
                    total += person + 1

        time += 1

    print(f'#{tc} {total if total > 0 else - 1}')
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




                

        

