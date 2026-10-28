# 26. 10. 28.
# SWEA 9280. 진용이네 주차타워.
# 1차 시도: 55분(PASS)
# 오랜만에 푸는 D3네? Gpt가 추천해줬다.

"""
목표: N개의 주차 공간이 주어진다.
    1. 차가 오면 번호가 비어있는, 가장 작은 주차 공간에 주차시킨다
    2. 빈 공간이 없으면 입구에서 대기시킨다.
    3. 도착한 순서대로 입구에서 대기한다.
    4. 주차요금은 (차량 무게 * 공간 금액) 이다.
    5. m대의 차량들이 들어오고 나가는 순서가 주어진다.
    6. 하루 벌어들일 총 수입을 구하라.
상태: 
    1. entrance = 입구에서 대기하는 차량들
    2. profit = 하루 총 수입
자료구조: 시뮬레이션, deque
핵심 로직:
    1. order을 순회.
    2. 도착한 차들을 entrance에 넣음
    3. 빈 칸이 있는지 확인 후 visited에 넣음 / popleft()
    4. 넣는 동시에 profit += car_weight[idx] * parking_fee[i]
    5. 만약 음수라면, visited를 돌아서 차를 방출함
종료 조건: entrance가 비었다면 종료
시간 복잡도: O(2MN)
"""

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    parking_fee = [int(input()) for _ in range(N)]
    car_weight = [0]
    for _ in range(M):  # 번호 맞추기.
        current = int(input())
        car_weight.append(current)
    order = [int(input()) for _ in range(2 * M)]

    profit = 0
    entrance = deque()
    visited = [0] * N   # 0이 빈 칸임

    for car in order:

        if car < 0:   # 차가 나갈 때
            for i in range(N):
                if visited[i] == - car: # 주차장에 있는 차와 일치하면
                    visited[i] = 0  # 차를 뺀다.
                    break
        else:
            entrance.append(car)

        for i in range(N):
            if visited[i] == 0 and entrance:
                current_car = entrance.popleft()
                visited[i] = current_car    # 다음 차 채우고.
                profit += parking_fee[i] * car_weight[current_car]  # 요금 받고.

    print(f'#{tc} {profit}')