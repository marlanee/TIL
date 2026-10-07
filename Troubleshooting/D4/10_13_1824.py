# SWEA 1824. 혁진이의 프로그램 검증

# 1차 시도: FAIL(60분)
# 10. 2. 복습 필요
# 1차 복습: N(60분)
# 10. 13. 복습 필요

# 목표: 
#   1. N x M 2차원 격자가 주어진다. 격자판은 다양한 명령의 요소로 이루어져 있다. 
#   2. (0, 0)에서 출발해 '@'에 도착할 수 있는지 판별하라.
# 상태: (r, c, d, memory) / r, c = 현재 위치 / d = 현재 진행 방향 / memory = 0~15의 메모리 값
# 자료구조: deque, set, BFS, 상태 공간 탐색, 델타 이동
# 핵심 로직: 
    # 1. 하나의 상태를 (r, c, d, memory)로 정의한다
    # 2. 동일한 상태를 다시 방문하면 이후 행동도 동일하므로 재탐색하지 않는다.
    # 3. 현재 칸의 명령어에 따라 방향 또는 memory 값을 변경한다
    # 4. '?'를 만나면 상하좌우 4개의 상태로 분기한다.
    # 5. 격자 밖으로 이동하면 반대편으로 이어지므로 % 연산으로 좌표를 순환시킨다.
    # 6. '@'를 만나면 YES, 탐색 가능한 모든 상태를 소진하면 NO.
# 종료 조건: '@'를 만나거나 queue가 빌 때
# 시간복잡도: O(NM)

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input() for _ in range(N)]

    q = deque()
    visited = set()

    q.append((0, 0, 3, 0))

    result = 'NO'

    while q:
        r, c, d, memory = q.popleft()
        random = False

        case = (r, c, d, memory)

        if case in visited:
            continue

        visited.add(case)

        cmd = grid[r][c]

        if cmd == '@':
            result = 'YES'
            break

        nr, nc = r, c

        if cmd == '<':
            d = 1
        elif cmd == '>':
            d = 3
        elif cmd == '^':
            d = 0
        elif cmd == 'v':
            d = 2
        elif cmd == '_':
            if memory == 0:
                d = 3
            else:
                d = 1
        elif cmd == '|':
            if memory == 0:
                d = 2
            else:
                d = 0
        elif cmd.isdigit():
            memory = int(cmd)
        elif cmd == '+':
            memory = (memory + 1) % 16
        elif cmd == '-':
            memory = (memory - 1) % 16
        elif cmd == '?':
            random = True

        if random:
            for i in range(4):
                nr = (r + dr[i]) % N
                nc = (c + dc[i]) % M
                q.append((nr, nc, i, memory))
        else:
            nr = (r + dr[d]) % N
            nc = (c + dc[d]) % M
            q.append((nr, nc, d, memory))

    print(f'#{tc} {result}')