"""
DFS
1. 뭘 구해야되는지 / 문자열
2. 다음 재귀호출에 뭘 건네줄지 / 이게 DFS의 매개변수
상태: 
    1. count = 현재까지 선택한 문자의 수
    2. current_strs = 지금까지 만든 문자열
"""

def dfs(next_r, next_c, count, current_strs):
    if count == 7:
        total_strs.add(current_strs)
        return

    for d in range(4):
        nr = next_r + dr[d]
        nc = next_c + dc[d]

        if not (0 <= nr < 4 and 0 <= nc < 4):
            continue

        dfs(nr, nc, count + 1, current_strs + grid[nr][nc])
        

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    grid = [input().split() for _ in range(4)]
    total_strs = set()

    for r in range(4):
        for c in range(4):
            dfs(r, c, 1, grid[r][c])

    print(f'#{tc} {len(total_strs)}')