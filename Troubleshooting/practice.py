# SWEA 2383. 점심 식사시간
# 10.19. 복습 1차: FAIL(1시간) / DFS 백트래킹 구현 부족
# 10. 26. 복습 필요

"""
목표: N x N 크기의 방에 사람들이 앉아 있다.
    1. 사람은 1, 계단은 2 이상의 숫자로 주어진다.
    2. 사람들은 맨해튼 거리로 계단으로 이동한다.
    3. 계단은 최대 3명까지 이용 가능하다. / 초과 인원은 입구에서 대기한다
    4. 입구에 도착하면 1분 후 내려갈 수 있다.
    5. 모든 사람들이 완전히 내려갈 때까지 걸리는 최소 시간을 구하라
상태: 
    1. min_time = 현재까지 찾은 최소 시간
    2. arrival = 사람들의 도착시간 분류 세트
자료구조:
핵심로직: 
    0. 사람들을 (A계단 도착시간, B계단 도착시간) 세트로 분류한다.
    1. 사람들을 계단에 보내는 경우를 완전 탐색한다.
        1. 0명부터 N명까지 A 계단에, 나머지는 다른 B 계단에 보낸다
        2. dfs(idx) / 넣고 + dfs(idx + 1) + 백트래킹 
        3. if idx == N / 반복문으로 B 계단에 A계단에 없는 사람들 넣는다
    2. 보내는 경우가 선택되면 시간을 계산해서 갱신한다.
        1. A 계단 소요시간과 B 소요시간중 최대 시간
        2. 시간을 1시간씩 흐르게 만듦
        3. 도착하면 입구에 위치시킴 / 대기시간 1시간
        4. 대기시간이 지나고 계단에 사람이 3명 미만이면 투입
        5. 이동을 완료하면 계단에서 제거 / 다음 사람 투입
종료조건: 
    1. 가지치기: A만 계산해도 이미 최솟값을 넘었을 때
    2. dfs로 완전 탐색이 끝났을 때
    3. 출력값: 최소 시간
"""

def dfs(idx):
    global min_time

    if idx == len(arrival):
        A_time = cal_time(stair_A, 0)

        if A_time >= min_time:
            return
        
        B_time = cal_time(stair_B, 1)

        min_time = min(min_time, max(A_time, B_time))
        return

    stair_A.append(arrival[idx])
    dfs(idx + 1)    # idx 사람을 A 계단에 선택
    stair_A.pop()

    stair_B.append(arrival[idx])
    dfs(idx + 1)
    stair_B.pop()


def cal_time(stair, kind):

    people = list(stair)
    entrance = []
    going_down = []
    down_time = stairs_long[kind]
    t = 0

    while people or entrance or going_down:  # 사람이 있을 때까지 반복
        next_people = []
        next_going_down = []
        next_entrance = []

        for gd in going_down:
            ngd = gd - 1
            if ngd == 0:
                continue
            next_going_down.append(ngd)

        going_down = next_going_down

        for e in entrance:  # 입구에서 계단으로
            if len(going_down) < 3:
                going_down.append(e)
                continue
            next_entrance.append(e)

        entrance = next_entrance

        for p in people:    # 1칸식 계단으로 전진. 온 사람은 입구로.
            next_p = p[kind] - 1
            if next_p == 0:
                entrance.append(down_time)
                continue
            if kind == 0:
                next_people.append((p[kind] - 1, 10))
            else:
                next_people.append((10, p[kind] - 1))

        people = next_people

        t += 1

    return t


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_time = float('inf')
    arrival = []
    stairs = []
    stairs_long = []

    for r in range(N):  # 계단 좌표 찾기
        for c in range(N):
            if grid[r][c] >= 2:
                stairs.append((r, c))
                stairs_long.append(grid[r][c])

    for r in range(N):  # A, B 계단과 각 사람들의 거리 탐색
        for c in range(N):
            if grid[r][c] == 1:
                ar, ac = stairs[0]
                time_A = abs(r - ar) + abs(c - ac)
                br, bc = stairs[1]
                time_B = abs(r - br) + abs(c - bc)
                arrival.append((time_A, time_B))

    stair_A = []
    stair_B = []

    dfs(0)

    print(f'#{tc} {min_time}')