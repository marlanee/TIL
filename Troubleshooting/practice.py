# SWEA 1824. 혁진이의 프로그램 검증
# 10. 15. 복습: 17:35

"""
목표: R x C 격자가 주어진다. 
    1. 최상단 왼쪽 문자에서 시작해서 '@' 문자까지 도달할 수 있는지 판별하라
상태: 
    1. visited = 이미 간 세계선인지 확인하는 세트. 
    2. q = 출발 세계선을 담은 deque
자료구조: BFS, visited, 델타 이동
핵심 로직:
    1. q에 출발 상태를 담는다.
    2. r, c, d, memory = q.popleft로 꺼낸다.
    3. 명령어에 따라 각 값을 변경하고 q와 visited에 넣는다.
    4. 만약 이미 다녀온 세계선이면 continue 한다.
종료 조건: @를 만나면 YES. q가 비면 NO.
시간 복잡도:
"""
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())
    grid = [input() for _ in range(R)]


    visited = {(0, 0, 3, 0)}
    q = deque([(0, 0, 3, 0)])   # 초기 출발지점.
    result = 'NO'

    while q:
        r, c, d, memory = q.popleft()
        current = grid[r][c]

        if current == '?':
            for i in range(4):
                nr = (r + dr[i]) % R
                nc = (c + dc[i]) % C

                next = (nr, nc, i, memory) 

                if next not in visited:
                    visited.add(next)
                    q.append(next)

            continue

        if current == '<':
            d = 2
        elif current == '>':
            d = 3
        elif current == '^':
            d = 0
        elif current == 'v':
            d = 1
        elif current == '_':
            if memory == 0:
                d = 3
            else:
                d = 2
        elif current == '|':
            if memory == 0:
                d = 1
            else:
                d = 0
        elif current == '@':
            result = 'YES'
            break
        elif current.isalpha():
            memory = int(current)
        elif current == '+':
            if memory == 15:
                memory = 0
            else:
                memory += 1
        elif current == '-':
            if memory == 0:
                memory == 15
            else:
                memory -= 1

        nr = (r + dr[d]) % R
        nc = (c + dc[d]) % C

        next = (nr, nc, d, memory)

        if next not in visited:
            visited.add(next)
            q.append(next)

    print(f'#{tc} {result}')