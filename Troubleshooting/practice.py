# SWEA 2383. 점심 식사시간
# 1차 시도: 11:28

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