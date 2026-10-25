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