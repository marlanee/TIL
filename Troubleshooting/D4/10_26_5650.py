# SWEA 5650. 핀볼 게임
# 1차 시도 10. 19: FAIL(90분) / 구현 완성도 부족
# 10. 26 1차 복습 필요

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