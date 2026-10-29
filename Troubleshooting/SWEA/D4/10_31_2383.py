# SWEA 2383. 점심 식사시간
# 1차 시도: FAIL(60분)
# 10. 16. 복습 필요
# SWEA 2383. 점심 식사시간
# 10.19. 복습 1차: FAIL(1시간) / DFS 백트래킹 구현 부족
# 10. 26. 복습 필요
# 26. 10. 29.
# SWEA 2383. 점심 식사시간
# 2차 복습: 80분(FAIL) + 힌트 참조 3분(PASS)
# 10. 31. 3차 복습 필요
"""
목표: N * N 방에 사람들이 앉아 있다.
    1. 점심을 먹기 위해 계단으로 모든 사람들이 아래 층으로 내려가야 한다
    2. 계단까지 이동하는 시간은 멘헤튼 거리와 동일하다
    3. 계단 입구에 도착하면 1분 후 내려갈 수 있다
    4. 계단에는 3명까지만 입장 가능하다
    5. 3명이 이미 입장해 있으면, 계단 입구에서 대기해야 한다
    6. 계단마다 길이 K가 주어지며, 계단에 입장한 후 K분 뒤 나올 수 있다
    7. 모든 사람들이 두 계단 중 하나를 선택해서 내려갈 때, 모든 사람들이 계단을 내려가 완료되는 최소 시간을 구하라
상태: 
    1. 
자료구조: 
핵심로직: 
    1. 데이터 전처리: grid를 순회하며 A, B계단까지의 도착 시간을 리스트로 만듦.
    2. 그렇다면 len(A_arrival) = 사람 수가 됨.
    3. 0번부터 len(A_arrival)까지 완전탐색을 돌림
        1. A계단에 한 명 ~ len(A_arrival)까지 랜덤으로 선택하는 완전 탐색
        2. B계단에는 나머지가 들어가게 됨
    4. 다 선택했다면 시간을 계산해서 최솟값을 갱신함
    5. 계단 내려가는 시뮬레이션 코드 작성
        1. T = 1부터 시작
        2. 계단에 있는 사람들의 시간을 갱신함
            1. 만약 시간이 K가 되었다면 내보냄
            2. 아니라면 1 더함
        3. 계단 입구에 있는 사람들을 계단에 넣음. 초기값은 0
        4. 도착한 사람들을 계단 입구에 넣음. 초기값은 0 / 여기서 문제의 의도가 보임. 1분 후 내려갈 수 있는 이유.
종료조건: 
시간복잡도: 
"""

def dfs(index, count, target):
    global min_time

    if count == target:  # 완전 탐색할 개수만큼 사람을 계단에 넣었다면
        B_stairs = []
        selected = set(A_stairs)
        for n in range(number): # 나머지를 B 계단에 넣기
            if n not in selected:
                B_stairs.append(n)

        A_time = count_time(A_stairs, A_arrival, grid[Ar][Ac])
        if A_time >= min_time:
            return
        B_time = count_time(B_stairs, B_arrival, grid[Br][Bc])
        min_time = min(min_time, max(A_time, B_time))
        return
    
    if index == number: # 선택이 최대 범위를 넘어가지 못하도록 종료 조건 추가
        return

    dfs(index + 1, count, target)   # 선택 안 하는 재귀호출

    A_stairs.append(index)
    dfs(index + 1, count + 1, target)   # 선택하는 재귀호출
    A_stairs.pop()

def count_time(type_stair, arrival, down_time):

    T = 1
    entrance = []
    stair = []

    while type_stair or entrance or stair:
        next_stair = []
        for s in stair: # 계단 시간 계산
            s += 1
            if s == down_time:
                continue
            next_stair.append(s)

        stair = next_stair

        while len(stair) < 3:   # 입구에서 계단에 집어넣기
            if not entrance:
                break
            entrance.pop()
            stair.append(0)

        next_arrive = []

        if type_stair:
            for a in type_stair: # 도착한 사람 입구에 넣기
                if arrival[a] == T:
                    entrance.append(a)
                    continue
                next_arrive.append(a)

        type_stair = next_arrive

        T += 1

    return T - 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    A_arrival = []
    B_arrival = []
    stairs = [] # A, B 계단의 좌표를 담아두는 리스트.

    for r in range(N):  # A, B 계단의 좌표 구하기
        for c in range(N):
            if grid[r][c] > 1:
                stairs.append([r, c])

    Ar, Ac = stairs[0][0], stairs[0][1]
    Br, Bc = stairs[1][0], stairs[1][1]

    for r in range(N):  # A, B계단까지의 도착시간을 구함
        for c in range(N):
            if grid[r][c] == 1:
                A_arrival.append(abs(Ar - r) + abs(Ac - c))
                B_arrival.append(abs(Br - r) + abs(Bc - c))

    number = len(A_arrival)
    min_time = float('inf')

    for i in range(number + 1):
        A_stairs = []
        dfs(0, 0, i)

    print(f'#{tc} {min_time}')
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
"""
목표: 
    1. N x N 크기의 방에 10명 이하의 사람이 있다. 두 계단이 주어지고, 사람들을 계단으로 이동시켜야 한다.
    2. 계단을 내려가는데 K분이 걸리고, 계단은 최대 3명까지만 수용 가능하다. # 계단은 총 2개이다
    3. 사람들을 계단으로 모두 내려보낼 때, 최소가 되는 시간을 구하라
상태: people = 각 사람이 (A, B, 0)계단으로 가는데 걸리는 시간과 계단에 머무른 시간
자료구조: DFS(greedy 사용 불가)
핵심로직:
    1. 모든 사람이 모든 계단을 이용하는 경우의 수를 완전 탐색한다. / 1번 계단 이용 재귀호출, 2번 계단 이용 재귀호출
        # 그렇다면 구현은?
        1. 사람마다 1번 계단까지 걸리는 시간, 2번 계단까지 걸리는 시간, 계단에 있었던 시간으로 데이터 전처리 한다. people = [(A, B, stay)]
        2. 그 중에서 (짝수일 경우 절반, 홀수일 경우 절반 + 1 and 절반 case로 나눔) 선택하여 1번 계단 리스트에 담는다.
        3. 나머지는 2번 계단 리스트에 담는다. 
        4. 시간을 카운트하며 시간과 일치하는 사람을 사용중 계단 리스트에 넣는다. 리스트는 최대 3까지 허용된다
        5. 시간이 카운트 될 때 계단 시간 == K 인 사람은 사용중 계단 리스트에서 뺀다.
        6. 시간이 카운트 될 때 사용중 계단 리스트가 꽉 차 있다면 다음 카운트로 넘어간다.
        7. 계단 리스트와 사용중 계단 리스트가 모두 비었다면 종료한다. / A_count 가 남는다
        8. 2번 계단도 동일하게 반복한다. / B_count가 남는다.
        9. max(A_count, B_count)를 현재까지 찾은 최솟값과 갱신한다.
종료조건:
시간 복잡도:
"""

from collections import deque

def dfs(index):
    global min_length

    if index == people_number: # 완전 탐색을 성공적으로 했을 경우 시간 계산
        a_finish = calculate_time(A_stair, A_time)
        b_finish = calculate_time(B_stair, B_time)
        min_length = min(min_length, max(a_finish, b_finish))
        return

    A_stair.append(people[index][0])
    dfs(index + 1)
    A_stair.pop()

    B_stair.append(people[index][1])
    dfs(index + 1)
    B_stair.pop()


def calculate_time(stair, length):
    # 도착 후 1분이 지난 시각부터 계단에 들어갈 수 있음
    waiting = deque(sorted(distance + 1 for distance in stair))

    # 계단 사용 중인 사람들의 완료 시각
    using = deque()
    current = 0

    while waiting or using:
        current += 1

        # 1. 이 시각에 내려가기를 완료한 사람부터 제거
        while using and using[0] <= current:
            using.popleft()

        # 2. 자리가 있으면 기다리는 사람 입장
        while waiting and waiting[0] <= current and len(using) < 3:
            waiting.popleft()
            using.append(current + length)

    return current


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    stairs = []

    for r in range(N):
        for c in range(N):
            if grid[r][c] > 1:
                stairs.append((r, c))

    A_time = grid[stairs[0][0]][stairs[0][1]]
    B_time = grid[stairs[1][0]][stairs[1][1]]

    people = []

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1:
                people.append([])
                for sr, sc in stairs:
                    distance = abs(r - sr) + abs(c - sc)
                    people[-1].append(distance)
                people[-1].append(0)

    people_number = len(people)
    min_length = float('inf')
    A_stair = []
    B_stair = []

    dfs(0)

    print(f'#{tc} {min_length}')