"""
26.11.04. SWEA 7396. 종구의 딸이름 짓기
1차 시도: 17분

목표:
핵심로직:
    1. grid를 숫자로 변환한다
    2. 오른쪽, 아래쪽 중에서 작은 번호를 선택한다. 리스트에 넣는다
    3. 우측 하단에 도착하면 종료한다
    4. 리스트 요소들을 알파벳으로 변환한다.
    5. 알파벳을 문자로 묶어 반환한다.
시간복잡도: O(N)
"""

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

    r, c = 0, 0

    while (r, c) != (N - 1, M - 1):
        min_num = float('inf')
        for d in range(2):
            nr = r +dr[d]
            nc = c +dc[d]

            if not (0 <= nr < N and 0 <= nc < M):
                continue

            if min_num > grid[nr][nc]:
                min_num = grid[nr][nc]
                tr, tc = nr, nc

        num_total.append(grid[tr][tc])

        r, c = tr, tc

    result = ''.join(chr(x) for x in num_total)
    print(result)