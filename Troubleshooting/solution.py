<<<<<<< HEAD
"""
26. 11. 04. SWEA 1259. 금속 막대
1차 시도: 19:49

목표:
핵심로직:
시간복잡도:
"""

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
=======
# 261105. SWEA 2383
# 4차 시도: 16:46

"""
목표: N * N 크기의 방에 사람들이 있다.
    1. 모든 사람들이 두 계단 중 하나를 선택해 내려가야 한다
    2. 이동 시간은 멘헤튼 거리와 같다
    3. 계단 좌표에 도착하면 1분 후 아래칸으로 내려갈 수 있다.
    4. 계단에는 동시에 최대 3명까지만 입장 가능하다
    5. 계단 정원이 꽉 찼으면 입구에서 대기한다.
    6. 모든 사람들이 계단을 내려가 이동이 완료되는 최소 시간을 구하라
핵심로직: DFS
    1. 사람마다 A, B계단으로 내려가는 시간을 담은 리스트를 만든다
    2. A계단에 0명~people_num 명까지 완전 탐색으로 넣어본다
    3. 나머지는 B 계단에 넣는다
    4. A계단과 B계단의 시간을 계산한다.
    5. 둘 중에 긴 시간이 내려가는데 걸리는 총 시간이다.
    6. 갱신한다.
시간복잡도:
"""

def dfs(number, stair_A, people_num, start, A_time, B_time):
    global min_time

    if len(stair_A) == number: # 다 골랐으면 시간 계산하고 갱신하자.
        check_A = set(stair_A)
        stair_B = []

        for i in range(people_num):
            if i not in check_A:
                stair_B.append(i)

        # 계단 내려가는 시간 계산
        A_reuslt = down_stairs(stair_A, down_A, A_time)
        if A_reuslt >= min_time:
            return
        B_reuslt = down_stairs(stair_B, down_B, B_time)  

        result = max(A_reuslt, B_reuslt)

        min_time = min(min_time, result)

        return

    for j in range(start, people_num): # 완전 탐색 / 중복 제거 필요
        stair_A.append(j)
        dfs(number, stair_A, people_num, j, A_time, B_time)
        stair_A.pop()


def down_stairs(stair, down, time):

    t = 1
    entrance = []
    in_stair = []

    while stair or entrance or in_stair:
        next_stair = []
        next_in_stair = []

        for s in in_stair:
            s += 1
            if s == time:
                continue
            next_in_stair.append(s)

        in_stair = next_in_stair

        while len(in_stair) < 3:
            entrance.pop()  # 이 부분 수정하자.
            in_stair.append(0)
            
        for s in stair:
            if t == down[s]:
                entrance.append(1)
                continue
            next_stair.append(down[s])

        stair = next_stair

        t += 1

    return t

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    people = []
    stair = []

    for r in range(N):  # 계단과 사람 좌표 찾기
        for c in range(N):
            current = grid[r][c]
            if current == 1:
                people.append((r, c))
            elif current >= 2:
                stair.append((r, c))

    people_num = len(people)    # 사람 수 측정하기

    down_A = []
    down_B = []

    Ar, Ac = stair[0][0], stair[0][1]
    Br, Bc = stair[1][0], stair[1][1]

    A_time = grid[Ar][Ac]
    B_time = grid[Br][Bc]

    for r, c in people:
        a = abs(r - Ar) + abs(c - Ac)
        b = abs(r - Br) + abs(c - Bc)
        down_A.append(a)
        down_B.append(b)

    min_time = float('inf')

    for number in range(people_num + 1):
        dfs(number, [], people_num, 0, A_time, B_time)

    print(f'#{tc} {min_time}')
>>>>>>> e878e5d3996c8a35183726f0c6d714ab1870080b
