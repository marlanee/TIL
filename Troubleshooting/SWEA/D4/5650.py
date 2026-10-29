# SWEA 5650. 핀볼 게임
# 1차 시도 10. 19: FAIL(90분) / 구현 완성도 부족
# 10. 26 1차 복습 필요
# 26. 10. 29.
# SWEA 5650. 핀볼 게임
# 2차 시도: 47분(PASS) / 24분(분석) 23분(코드 작성)
# 졸업
"""
목표: N x N 핀볼 게임판이 주어진다.
    1. 핀볼이 출발 위치로 돌아오거나, 블랙홀에 빠질 때 게임은 끝난다.
    2. 벽이나 블록에 부딪히면 점수가 1점 오른다.
    3. 출발 위치와 진행 방향을 임의로 선정하여, 게임에서 얻을 수 있는 점수의 최댓값을 구하라.
상태:
    1. max_score = 현재 찾은 최대 점수
    2. wormhole = 웜홀의 좌표를 담은 딕셔너리. 크기: [좌표, 좌표]
자료구조: 시뮬레이션, 델타 이동, 딕셔너리
핵심로직:
    1. 공의 시작 지점, 방향 설정
    2. play_game 함수로 점수 갱신
    3. 여러 블록들 처리 필요
종료조건:
시간복잡도:
"""

''' 메모장
1. 시뮬레이션인 것 같다.
2. 공의 시작과 방향은 다음과 같이.
    1. for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                for d in range(4):
                    play_game(row, col, d)
3. play_game 함수에서 동작하는 코드들
    0. 극한 반복. while True:
    1. nr = r + dr[d] / nc = c + dc[d]
    2. 여기서부터 다양한 블록들 처리.
        0. current = grid[nr][nc]
        1. if grid[nr][nc] == -1:   # 블랙홀
            return score
        2. if nr, nc == row, col:   # 출발 지점
            return score
        3. 웜홀이면 딕셔너리에서 nr, nc와 같지 않는 것이 nr, nc가 됨
        4. 5 또는 벽이면 d를 반대 방향으로 바꿈 / reverse_d 필요
        5. 삼각 블록이면, d가 딕셔너리에 있는지 확인 후 방향을 바꿈 / 어떻게?
            1. 이게 문제네 그냥 하드코딩 해버릴까. 그러자.
'''

def play_game(r, c, d):
    score = 0
    nr, nc = r, c

    while True:
        nr = nr + dr[d]
        nc = nc + dc[d]

        if not (0 <= nr < N and 0 <= nc < N) or grid[nr][nc] == 5:  # 벽과 정사각형 블록 처리
            d = reverse_d[d]
            score += 1
            continue

        current = grid[nr][nc]

        if current == -1:   #블랙홀 처리
            return score

        if (nr, nc) == (r, c):  #출발지점 처리
            return score

        if 6 <= current <= 10:  #웜홀 처리
            for cr, cc in wormhole[current]:
                if (cr, cc) != (nr, nc):
                    nr, nc = cr, cc
                    break
            continue

        if current == 1:
            if d not in (1, 2):
                d = reverse_d[d]
                score += 1
                continue
            if d == 1:
                d = 3
            elif d == 2:
                d = 0
            score += 1
        elif current == 2:
            if d not in (0, 2):
                d = reverse_d[d]
                score += 1
                continue
            if d == 0:
                d = 3
            elif d == 2:
                d = 1
            score += 1
        elif current == 3:
            if d not in (3, 0):
                d = reverse_d[d]
                score += 1
                continue
            if d == 3:
                d = 1
            elif d == 0:
                d = 2
            score += 1
        elif current == 4:
            if d not in (1, 3):
                d = reverse_d[d]
                score += 1
                continue
            if d == 1:
                d = 2
            elif d == 3:
                d = 0
            score += 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
reverse_d = [1, 0, 3, 2]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_score = 0
    wormhole = {}

    for r in range(N):  # 웜홀 좌표 찾기
        for c in range(N):
            current = grid[r][c]
            if 6 <= current <= 10:
                wormhole.setdefault(current, [])
                wormhole[current].append((r, c))

    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:    
                for direction in range(4):
                    result = play_game(row, col, direction)
                    max_score = max(max_score, result)

    print(f'#{tc} {max_score}')
"""
목표: N x N 크기의 핀볼 게임판이 주어진다.
    1. 출발지, 블랙홀을 만나면 게임은 종료된다.
    2. 벽이나 블록에 부딪히면 점수가 1 오른다.
    3. 공의 출발 위치와 진행 방향을 임의로 선정할 때, 
    4. 게임에서 얻을 수 있는 점수의 최대값을 구하라
상태: max_count = 현재까지 획득한 최대 점수
자료구조: 델타 이동, 시뮬레이션
핵심로직:
    1. grid를 순회함
    2. grid[r][c] == 0 이라면 공을 4방향으로 쏨
    3. 게임판을 돌다가 아래 조건에서 멈춤
        1. 출발 지점에 도착했을 때
        2. 블랙홀에 도착했을 때
    4. 벽이나 블록에 튕긴 횟수를 최대값 갱신함
종료조건: 반복문이 종료되었을 때
시간 복잡도: O(N^4)
"""

blocks = {
    1: [1, 2],
    2: [0, 2],
    3: [3, 0],
    4: [3, 1],
    5: [1, 0, 3, 2]
}
# 하 상 우 좌
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

reverse_d = [1, 0, 3, 2]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_count = 0
    wormhole = {}   # 웜홀의 좌표를 저장하는 딕셔너리

    for r in range(N):  # 웜홀의 좌표를 구해야한다.
        for c in range(N):
            if grid[r][c] >= 6:
                wormhole.setdefault(grid[r][c], [])
                wormhole[grid[r][c]].append((r, c))

    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                for d in range(4):
                    current_count = 0
                    nr, nc = r, c

                    while True: # 출발
                        nr = nr + dr[d]
                        nc = nc + dc[d]

                        # 공이 출발점에 온 경우
                        if (nr, nc) == (r, c):
                            break

                        # 공이 벽에 튀기는 경우
                        if not (0 <= nr < N and 0 <= nc < N) or grid[nr][nc] == 5:
                            d = reverse_d[d]
                            current_count += 1
                            continue

                        # 공이 블랙홀에 온 경우
                        if grid[nr][nc] == -1:
                            break

                        # 공이 웜홀에 온 경우 / 다른 웜홀을 출발지로 바꾸면 된다
                        if grid[nr][nc] >= 6:
                            for wr, wc in wormhole[grid[nr][nc]]:
                                if (nr, nc) != (wr, wc):
                                    nr, nc = wr, wc
                                    break

                        # 공이 블록에 튕기는 경우 / 블록이 출발지가 된다
                        if 0 < grid[nr][nc] <= 4:
                            if d in blocks[grid[nr][nc]]:
                                d = reverse_d[d]
                            else:
                                for b in blocks[grid[nr][nc]]:
                                    if reverse_d[d] != b:
                                        d = b
                                        break

                            current_count += 1

                    max_count = max(current_count, max_count)

    print(f'#{tc} {max_count}')