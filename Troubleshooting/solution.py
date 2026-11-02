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

    using_recept = [[False, False] for _ in range(N)]
    using_repair = [[False, False] for _ in range(M)]

    user_info = [[] for _ in range(K)] 

    finished = 0
    time = 0
    recept_waiting = deque()
    repair_waiting = deque()

    while finished != K:

        for user_idx, u in enumerate(arrvie_time):   # 접수 대기열에 도착한 손님 넣기
            if u == time:
                recept_waiting.append([user_idx, 0])

        for recept_idx, (user_idx, check) in enumerate(using_recept): # 접수 창구 진행도 갱신
            add_waiting = []
            if check >= 0:
                check += 1
                if check == recept_time[recept_idx]:
                    add_waiting.append([recept_idx, user_idx])
                    using_recept[recept_idx] = [False, False]
                    continue
                using_recept[recept_idx] = [user_idx, check]

        # 정비 창구 대기열에 넣기
        add_waiting.sort()
        for recept_idx, user_idx in add_waiting:
            repair_waiting.append((user_idx, 0))

        for recept_idx, (user_idx, check) in enumerate(using_recept):   # 접수 대기열 -> 접수
            if not recept_waiting:
                break
            if not check:
                print(recept_waiting)
                using_recept[recept_idx] = recept_waiting.popleft()
                user_info[using_recept[recept_idx][0]].append(recept_idx + 1)  # 접수 창고 번호 입력

        for repair_idx, (user_idx, check) in enumerate(using_repair):   # 정비 창구 진행도 갱신
            if check >= 0:
                check += 1
                if check == repair_time[repair_idx]:
                    finished += 1
                    using_repair[repair_idx] = [False, False]
                    continue
                using_repair[repair_idx] = [user_idx, check]

        for repair_idx, (user_idx, check) in enumerate(using_repair):   # 정비 대기열 -> 정비 창구
            if not repair_waiting:
                break
            if not check:
                using_repair[repair_idx] = repair_waiting.popleft()
                user_info[using_repair[repair_idx][0]].append(repair_idx + 1)

        time += 1

    print(user_info)



        

        



        


