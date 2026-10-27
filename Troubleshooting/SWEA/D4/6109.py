# 26. 10. 27.
# SWEA 6109. 추억의 2048 게임
# 1차 시도: 90분(PASS) / 디버깅만 1시간

"""
목표: N x N 격자가 주어진다. 2048 게임이 시작된다.
    1. 충돌하는 벽에 가까이 있는 타일부터 이동시킨다.
    2. 주어진 방향대로 타일을 이동시키고 변화된 격자를 구하라
상태: 
    1. current = 현재 row에 있는 숫자들
자료구조: stack
핵심로직:
    0. 행렬 전치를 사용한다. / down이면 right와 동일 로직, up이면 left와 동일 로직
    1. row를 순회하면서 만약 0보다 크면, current에 넣는다
    2. current를 순회하며 next에 넣는다. / while i < len(current): / i = 0
        1. left, up의 경우: 
            0. next가 비었으면 일단 집어넣는다.
            1. current[i] == next[-1]면 next.pop() + current[i]를 집어넣는다.
            2. i += 1
            3. 아닐 경우 그냥 집어넣는다
            4. i += 1
            5. row[col]을 순회하며 next.leftpop()으로 하나씩 갱신한다
            6. 비었다면 0을 갱신한다.
        2. right, up의 경우
            0. 역방향 순회를 한다. / while i > -len(current): / i = -1
            1. next가 비었으면 일단 집어넣는다.
            2. current[i] == next[-1] 이면 next.pop() + current[i]를 집어넣는다
            3. i -= 2
            4. 아닐 경우 그냥 집어넣는다
            5. i -= 1
            6. row[col]을 역방향 순회하며 next.popleft()로 갱신한다.
            7. 비었다면 0을 갱신한다.
    3. right, up의 경우 모든 과정을 마치고 행렬 전치를 원복한다
        0. 빈 grid를 만든다
        1. for문 두개를 돌린다. 
        2. 빈 grid[r][c] = 원본 grid[c][r]
종료조건: 가장 바깥 for문이 종료되면 grid를 출력한다.
시간복잡도:
"""
from collections import deque

def find_2048(grid, d):
    for r in range(N):
        current = deque()
        next = deque()
        for c in range(N):
            if grid[r][c] > 0:
                current.append(grid[r][c])

        if not current:
            continue

        length = len(current)

        if d == 0:  #left, up
            i = 0

            while i < length:   
                if i == length - 1:
                    next.append(current[i])
                    break
                if current[i] == current[i + 1]:
                    next.append(current[i] * 2)
                    i += 2
                    continue

                next.append(current[i])
                i += 1

            for c in range(N):
                if not next:
                    grid[r][c] = 0
                    continue
                grid[r][c] = next.popleft()

        elif d == 1:
            i = -1

            while i >= - length:
                if i == -length:
                    next.append(current[i])
                    break
                if current[i] == current[i - 1]:
                    next.append(current[i] * 2)
                    i -= 2
                    continue

                next.append(current[i])
                i -= 1

            for c in range(N - 1, -1, -1):
                if not next:
                    grid[r][c] = 0
                    continue
                grid[r][c] = next.popleft()

    return grid

T = int(input())
for tc in range(1, T + 1):
    str_N, S = input().split()
    N = int(str_N)
    up_grid = [list(map(int, input().split())) for _ in range(N)]
    down_grid = list(map(list, zip(*up_grid)))

    if S == 'up':
        current_grid = find_2048(down_grid, 0)
        result_grid = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                result_grid[c][r] = current_grid[r][c]
    elif S == 'down':
        current_grid = find_2048(down_grid, 1)
        result_grid = [[0] * N for _ in range(N)]

        for r in range(N):
            for c in range(N):
                result_grid[c][r] = current_grid[r][c]
    elif S == 'left':
        result_grid = find_2048(up_grid, 0)
    else:
        result_grid = find_2048(up_grid, 1)

    print(f'#{tc}')
    for r in range(N):
        for c in range(N):
            print(result_grid[r][c], end = ' ')
        print()