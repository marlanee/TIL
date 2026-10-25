# SWEA 4014. 활주로 건설
# 좋은 아침? 긍정긍정
# 10.16. 1차 시도: FAIL(40분) 
# 10. 23. 복습 필요
# 26. 10. 23.
# SWEA 4014. 활주로 건설
# 1차 복습: FAIL(1시간)
# 10. 30. 복습 필요

"""
목표: N x N 절벽지대가 주어진다.
    1. 이 곳에 행 또는 열로 활주로를 건설하자.
    2. 높이가 1만큼 다르다면 경사로를 설치해서 활주로 건설이 가능하다
        1. 경사로의 길이는 X이다. 높이는 1로 고정
    3. 활주로를 건설할 수 있는 경우의 수를 구하여라
상태: 
자료구조:
핵심로직:
    1. 행렬 전치로 같은 행과 열을 계산할 때 로직을 적용하자.
    2. grid를 row로 순회한다
    3. while idx < N - 1: 로 col을 순회한다.
        1. 다음 idx의 높이가 같으면 넘어간다. continue
        2. 다음 idx의 높이가 1보다 크면 break
        3. 높이가 1 낮다면 경사로 설치 가능한지 확인한다
            0. grid[row][idx + 1: idx + 2 + X] != (grid[row][idx] - 1) * X / break
            1. idx + X + 1 >= N 이면 break
            2. check[row][idx + 1:idx + 2 + X] = [True] * X
        4. 높이가 1 높다면 경사로 설치 가능한지 확인한다
            1. idx - X + 1 < 0이면 break
            2. check[row][idx - X + 1:idx + 1].count(False) >= X면 ok
        5. break가 발동되지 않았다면 total += 1
종료조건:
시간복잡도:
"""
def path(grid, check):
    
    total = 0

    for r in range(N):
        idx = 0
        while idx < N - 1:
            if grid[r][idx] == grid[r][idx + 1]:
                idx += 1
                continue
            elif abs(grid[r][idx] - grid[r][idx + 1]) > 1:
                break

            # 높이가 1 낮을 경우
            if grid[r][idx] == grid[r][idx + 1] + 1:    # X만큼 평지가 아닐 경우
                if idx + X + 1 > N:  # 경사로를 설치할 땅이 없을 경우
                    break
                if grid[r][idx + 1: idx + 1 + X].count(grid[r][idx + 1]) < X:
                    break

                # 경사로 설치
                check[r][idx + 1:idx + 1 + X] = [True] * X
                idx += X
                continue

            # 높이가 1 높을 경우
            if grid[r][idx] + 1 == grid[r][idx + 1]:
                if idx - X + 1 < 0: # 경사로를 설치할 땅이 없을 경우
                    break
                if check[r][idx - X + 1:idx + 1].count(False) < X:  # 경사로를 이미 설치했으면
                    break
                if grid[r][idx - X + 1:idx + 1].count(grid[r][idx]) < X:
                    break
                idx += 1    # 경사로 설치 후 위로 이동

        else:   # break가 발동하지 않았다면
            total += 1

    return total

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    col_grid = [list(map(int, input().split())) for _ in range(N)]
    row_grid = list(map(list, zip(*col_grid)))
    col_check = [[False] * N for _ in range(N)]
    row_check = [[False] * N for _ in range(N)]

    col_total = path(col_grid, col_check)
    row_total = path(row_grid, row_check)

    result = col_total + row_total

    print(f'#{tc} {result}')
    
"""
목표: N * N 절벽지대가 주어진다. 이 곳에 활주로를 건설하려고 한다.
    1. 조건을 만족하는 행 또는 열에 활주로를 건설할 수 있다.
    2. 조건은 다음과 같다.
        1. 동일한 높이면 활주로 설치 가능
        2. 높이가 1 차이일 경우 길이가 X인 경사로를 설치하면 가능
            1. 경사로는 지형의 높이가 동일해야 설치 가능
            2. 경사로를 설치하고 나면 높이가 1 줄어듦
        3. 행과 열에서 활주로를 설치하고, 활주로의 총 개수를 구하라
상태: 
자료구조: 행렬 전치
핵심 로직: 
    1. 열을 행으로 전치시킨 후 합침 
    2. 합친 grid를 row로 순회함
    3. 활주로 설치가 가능하면 total += 1
        1. grid[row]를 순회함
        2. grid[row][c] == grid[row][c + 1]일 경우 ok
        3. grid[row][c] - 1 == grid[row][c + 1]일 경우 아래 조건 확인
            1. 경사로 설치가 가능한지 확인해야함
            2. for i in range(X):
                if grid[row]
    4. 활주로 설치가 불가하면 continue
종료 조건: grid 순회가 끝나면 total 출력
시간복잡도: 
"""

T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    col_grid = [list(map(int, input().split())) for _ in range(N)]
    row_grid = list(map(list, zip(*col_grid)))
    grid = col_grid + row_grid
    visited = [[False] * N for _ in range(2 * N)]

    total = 0

    for idx, row in enumerate(grid):
        c = 0
        while True:
            if c == N - 1:  # 끝까지 무사히 도착하면 활주로 설치
                total += 1 
                break

            if abs(row[c + 1] - row[c]) > 1:
                break

            if row[c] == row[c + 1]:    # 평탄하면 조건 만족. 다음 열 검색
                c += 1
                continue

            check = 0

            if row[c] - 1 == row[c + 1]: # 높이가 1 낮을 때, 경사로 설치 가능여부 확인
                c = c + 1
                for x in range(1, X):
                    if c + x >= N:  # 범위를 벗어나면 경사로 설치 불가
                        break
                    if row[c + x] != row[c]:    # 경사로 설치 도중 높이가 달라지면 설치 불가
                        break
                    check = c + x
                if check != c + X - 1:
                    break
                else:
                    if not any(visited[idx][c:c + X]):
                        visited[idx][c:c + X] = [True] * X
                        c = check   # for문에 문제가 없었으면 다음으로.
                        continue
                    else:
                        break

            if row[c] + 1 == row[c + 1]: # 높이가 1 높을 때, 경사로 설치 가능여부 확인
                for x in range(1, X):
                    if c - x < 0:   # 범위 벗어나면 설치 불가
                        break
                    if row[c] != row[c - x]:    # 높이 달라지면 경사로 설치 불가 
                        break
                    check = c + x
                if check != c + X - 1:
                    break
                else:
                    if not any(visited[idx][c - X + 1:c + 1]):
                        visited[idx][c - X + 1:c + 1] = [True] * X
                        c += 1
                        continue
                    else:   
                        break

    print(f'#{tc} {total}')