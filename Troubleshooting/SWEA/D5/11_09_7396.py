"""
26.11.04. SWEA 7396. 종구의 딸이름 짓기
1차 시도: FAIL(17분) / 단순 greedy가 아니었다
배운 내용: 알파벳 비교, BFS
11.9 복습 필요

목표:
핵심로직:
    1. grid를 숫자로 변환한다
    2. 오른쪽, 아래쪽 중에서 작은 번호를 선택한다. 리스트에 넣는다
    3. 우측 하단에 도착하면 종료한다
    4. 리스트 요소들을 알파벳으로 변환한다.
    5. 알파벳을 문자로 묶어 반환한다.
시간복잡도: O(N)
"""
from collections import deque

dr = [1, 0]
dc = [0, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [[] for _ in range(N)]

    for i in range(N):
        current = input()
        for j in current:
            grid[i].append(ord(j))

    num_total = [grid[0][0]]

    q = deque({(0, 0)})

    while True:
        next_q = set()
        min_num = float('inf')

        for r, c in q:
            for d in range(2):
                nr = r + dr[d]
                nc = c + dc[d]

                if not (0 <= nr < N and 0 <= nc < M):
                    continue

                if grid[nr][nc] < min_num:
                    min_num = grid[nr][nc]
                    next_q.clear()
                    next_q.add((nr, nc))
                elif grid[nr][nc] == min_num:
                    next_q.add((nr, nc))
        if not next_q:
            break

        num_total.append(min_num)
        q = next_q

    result = ''.join(chr(x) for x in num_total)
    print(result)

    T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    result = [grid[0][0]]
    cur = {(0, 0)}

    for _ in range(N + M - 2):
        best = '{'          # 'z'보다 큰 문자
        nxt = set()
        for r, c in cur:
            for nr, nc in ((r + 1, c), (r, c + 1)):
                if nr < N and nc < M:
                    ch = grid[nr][nc]
                    if ch < best:
                        best = ch
                        nxt = {(nr, nc)}
                    elif ch == best:
                        nxt.add((nr, nc))
        result.append(best)
        cur = nxt

    print(f'#{tc} {"".join(result)}')