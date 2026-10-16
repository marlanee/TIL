# SWEA 4014. 활주로 건설
# 좋은 아침? 긍정긍정
# 10.16. 1차 시도: FAIL(40분)

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
    visited = [[False] * (N * 2) for _ in range(2 * N)]

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
                    if not visited[idx][c]:
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
                    if not visited[idx][c]:
                        visited[idx][c:c + X] = [True] * X
                        c += 1
                        continue
                    else:   
                        break

    print(f'#{tc} {total}')