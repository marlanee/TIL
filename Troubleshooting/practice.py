# SWEA 1824. 혁진잉의 프로그램 검증
# 복습: N(1시간)

"""
목표: 
    1. R x C 2차원 배열이 주어진다. 
    2. (0, 0)에서 시작해서 @가 입력된 좌표까지 도달할 수 있는지 판정하라.
상태: 
    1. check_dimention = 이미 간 좌표와 메모리, 방향인지 확인
    2. q = 현재 출발 위치
    3. next_q = 다음 출발 위치
자료구조: BFS
핵심로직:
    1. queue에 (0, 0) 출발지를 넣고 시작함. / 출발지도 check_dimention에 넣음
    2. while q:, next_queue에 다음 좌표, 방향, 메모리를 넣음, check_dimention에 없으면 넣음
    3. 이미 check_dimention에 있는 좌표, 방향, 메모리일 경우 continue로 스킵함
종료 조건: queue가 비거나, @에 도달했을 경우
시간 복잡도: 계산중
"""
from collections import deque

cmd = {
    '<': 0,
    '>': 1,
    '^': 2,
    'v': 3
    }

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [input() for _ in range(R)]

    check_dimention = {(0, 0, 1, 0)}
    q = deque([(0, 0, 1, 0)])
    result = 'NO'

    while q:
        next_q = deque()
        r, c, d, memory = q.popleft()

        word = grid[r][c]

        if word == '@':
            result = 'YES'
            break

        if word in cmd:
            d = cmd[word]
        elif word == '_':
            if memory == 0:
                d = 1
            else:
                d = 0
        elif word == '|':
            if memory == 0:
                d = 3
            else:
                d = 2
        elif word.isdigit():
            memory = int(word)
        elif word == '+':
            memory = (memory + 1) % 16
        elif word == '-':
            if memory == 0:
                memory = 15
            else:
                memory -= 1

        if word == '?':
            for i in range(4):
                d = i
                nr = (r + dr[d]) % R
                nc = (c + dc[d]) % C

                if (nr, nc, d, memory) in check_dimention:
                    continue

                q.append((nr, nc, d, memory))
                check_dimention.add((nr, nc, d, memory))

            continue

        nr = (r + dr[d]) % R
        nc = (c + dc[d]) % C

        if (nr, nc, d, memory) in check_dimention:
            continue

        q.append((nr, nc, d, memory))
        check_dimention.add((nr, nc, d, memory))

    print(f'#{tc} {result}')