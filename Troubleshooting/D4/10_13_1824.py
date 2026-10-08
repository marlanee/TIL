# SWEA 1824. 혁진이의 프로그램 검증

# 1차 시도: FAIL(60분)
# 10. 2. 복습 필요
# 10. 13. 복습 필요
# 1차 복습: N(60분)

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

# from collections import deque

# dr = [-1, 0, 1, 0]
# dc = [0, -1, 0, 1]

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     grid = [input() for _ in range(N)]

#     q = deque()
#     visited = set()

#     q.append((0, 0, 3, 0))

#     result = 'NO'

#     while q:
#         r, c, d, memory = q.popleft()
#         random = False

#         case = (r, c, d, memory)

#         if case in visited:
#             continue

#         visited.add(case)

#         cmd = grid[r][c]

#         if cmd == '@':
#             result = 'YES'
#             break

#         nr, nc = r, c

#         if cmd == '<':
#             d = 1
#         elif cmd == '>':
#             d = 3
#         elif cmd == '^':
#             d = 0
#         elif cmd == 'v':
#             d = 2
#         elif cmd == '_':
#             if memory == 0:
#                 d = 3
#             else:
#                 d = 1
#         elif cmd == '|':
#             if memory == 0:
#                 d = 2
#             else:
#                 d = 0
#         elif cmd.isdigit():
#             memory = int(cmd)
#         elif cmd == '+':
#             memory = (memory + 1) % 16
#         elif cmd == '-':
#             memory = (memory - 1) % 16
#         elif cmd == '?':
#             random = True

#         if random:
#             for i in range(4):
#                 nr = (r + dr[i]) % N
#                 nc = (c + dc[i]) % M
#                 q.append((nr, nc, i, memory))
#         else:
#             nr = (r + dr[d]) % N
#             nc = (c + dc[d]) % M
#             q.append((nr, nc, d, memory))

#     print(f'#{tc} {result}')

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