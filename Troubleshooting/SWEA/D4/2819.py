# SWEA 2819. 격차판 숫자 이어 붙이기

# 1차 시도: FAIL
# 9. 17. 복습 필요

# 복습: PASS(19분)
# 졸업

# 목표: 4 x 4 2차원 행렬에서 임의 위치에서 시작하여, 상하좌우로 6 번 이동하며 만들 수 있는 수의 개수를 구하여라.
# 상태: numbers = set() 만든 수 관리.
# 자료구조: DFS / 백트래킹
# 핵심 로직
    # 1. if move == 6:
    #     return number
# 종료 조건: 재귀 함수 호출이 종료되었을 때.

# def find_num(r, c, move, number):
#     if move == 6:
#         numbers.add(tuple(number))
#         return

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]

#         if 0 <= nr < 4 and 0 <= nc < 4:
#             number.append(grid[nr][nc])
#             find_num(nr, nc, move + 1, number)
#             number.pop()

# dr = [1, -1, 0, 0]
# dc = [0, 0, 1, -1]

# T = int(input())
# for tc in range(1, T + 1):
#     grid = [input().split() for _ in range(4)]

#     numbers = set()

#     for r in range(4):
#         for c in range(4):
#             number = [grid[r][c]]
#             find_num(r, c, 0, number)

#     result = len(numbers)

#     print(f'#{tc} {result}')

# SWEA 2819. 격자판의 숫자 이어 붙이기

# 복습: PASS(19분)
# 졸업

# 목표: 4 x 4 격자판에서 임의의 r, c 좌표에서 시작해 동서남북 방향으로 여섯 번 이동하며 만들 수 있는 경로의 개수를 구하여라
# 상태: total = 현재까지 만든 문자열을 담는 세트. 
# 자료구조: DFS, 델타 이동
# 핵심 로직: 
    # 1. DFS 요소는 r, c, length
    # 2. 격자판을 모두 순회
    # 3. 겹치지 않도록 세트 사용
    # 4. if length >= 7 일 경우 순회 종료
# 종료 조건: 반복문의 순회가 끝났을 때, len(total) 출력

def dfs(r, c, length, current_str):

    if length == 7:
        total.add(current_str)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, length + 1, current_str + grid[nr][nc])

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    grid = [list(input().split()) for _ in range(4)]

    total = set()

    for r in range(4):
        for c in range(4):
            dfs(r, c, 1, grid[r][c])

    result = len(total)

    print(f'#{tc} {result}')