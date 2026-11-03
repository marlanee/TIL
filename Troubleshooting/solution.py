"""
261102 / SWEA 4014 활주로 건설
3차 시도: PASS(30분) / 졸업

목표: N * N 절벽지대에 활주로를 건설하자.
    1. 가로 또는 세로 방향으로 활주로를 건설하자
    2. 활주로는 동일한 높이에서 건설하다.
    3. 높이가 다를 경우 경사로를 설치하면 건설 가능하다
    4. 낮은 지형의 높이가 X만큼 연속되는 곳에 설치 가능하다
    5. 경사로를 설치할 수 있는 경우의 수를 구하라.
상태:
자료구조:
핵심로직:
    1. 행렬 전치로 하나의 로직으로 검사하게 만들자.
    2. 한 행씩 검사한다. 
        1. for c in range(N - 1):
        2. 현재 발판과 다음 발판의 크기가 2 이상이면 break. 다음 행 검사
        3. 다음 발판이 1 높으면 [현재 발판 + 1 - X:현재 발판 +1]이 평탄한지 확인
            1. visited로 경사로가 이미 설치되어 있는지도 확인
            2. [현재 발판 + 1 - X] < 0 이면 범위 초과 불충족
        4. 다음 발판이 1 낮으면 [다음 발판: 다음 발판 + X]이 평탄한지 확인
            1. 다음 발판 + X > N 이면 범위를 초과했으므로 불충족
        5. 무사히 마쳤다면 total += 1 / for - else구문 활용
종료조건:
시간복잡도:
"""

def find_path(row, N, X):
    visited = [False] * N
    for c in range(N - 1):
        cur, nxt = row[c], row[c + 1]
        if cur == nxt:
            continue
        if abs(cur - nxt) >= 2:
            return 0
        if nxt == cur + 1:
            s = c + 1 - X
            if s < 0 or any(visited[s:c + 1]):
                return 0
            if any(row[i] != cur for i in range(s, c + 1)):
                return 0
        else:
            e = c + 1 + X
            if e > N:
                return 0
            if any(row[i] != nxt for i in range(c + 1, e)):
                return 0
            visited[c + 1:e] = [True] * X
    return 1


T = int(input())
for tc in range(1, T + 1):
    N, X = map(int, input().split())
    row_grid = [list(map(int, input().split())) for _ in range(N)]
    col_grid = list(zip(*row_grid))

    total = 0

    for row in row_grid:
        total += find_path(row, N, X)

    for row in col_grid:
        total += find_path(row, N, X)

    print(f'#{tc} {total}')