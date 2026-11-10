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
# 261109. SWEA 2383. 점심 식사시간
# 4차 시도: PASS(38분)
# 졸업

"""
목표: N x N 방이 있다.
    1. 모든 사람들이 두 개의 계단 중 하나로 내려가야 한다.
    2. 계단 입구까지 이동 시간은 멘헤튼 거리와 같다.
    3. 계단은 동시에 최대 3명까지 사용 가능하다
    4. 계단 입구에 도착하면 1분 후 아래칸으로 이동 가능하다
    5. 모든 사람들이 계단까지 내려가는 최소 시간을 구하라
핵심로직:
    1. 계단의 좌표를 구한다.
    2. 각 사람들이 A, B 계단으로 내려가는 시간을 리스트로 만든다
    3. dfs로 사람들을 A 또는 B 계단으로 완전 탐색으로 담는다.
    4. 다 담으면 시간을 계산한다.
    5. 시간을 갱신한다.
시간복잡도:
"""

def dfs(count):
    global min_time

    if count == len(people):
        # 시간 계산하는 코드
        A_result = cal_time(A_stair, grid[Ar][Ac])
        if A_result >= min_time:
            return
        B_result = cal_time(B_stair, grid[Br][Bc])
        min_time = min(min_time, max(A_result, B_result))
        return

    A_stair.append(A_time[count])
    dfs(count + 1)
    A_stair.pop()

    B_stair.append(B_time[count])
    dfs(count + 1)
    B_stair.pop()

def cal_time(stair, time):
    if not stair:
        return 0
    stair = sorted(stair)

    current = []

    for s in range(len(stair)):
        if s < 3:
            start = stair[s] + 1
        else:
            start = max(stair[s] + 1, current[s - 3])
        current.append(start + time)

    return current[-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    stairs = []
    people = []

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1:
                people.append((r, c))
            elif grid[r][c] >= 2:
                stairs.append((r, c))

    Ar, Ac = stairs[0][0], stairs[0][1]
    Br, Bc = stairs[1][0], stairs[1][1]

    A_time = []
    B_time = []

    for r, c in people:
        A_time.append(abs(Ar - r) + abs(Ac - c))
        B_time.append(abs(Br - r) + abs(Bc - c))

    min_time = float('inf')
    A_stair = []
    B_stair = []

    dfs(0)

    print(f'#{tc} {min_time}')