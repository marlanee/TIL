# SWEA 5653. 줄기세포배양
# 뭔놈의 줄기세포를 배양하냐.
# 1차 시도: Neutral(구현 60분 PASS + 디버깅 30분 FAIL) + 최종 힌트 PASS
# 26. 10. 22
# SWEA 5653. 줄기세포 배양
# 1차 복습: PASS(45분)
# 졸업

"""
목표: 줄기 세포가 담긴 N x M 용기가 주어진다.
    1. 생명력이 X인 줄기세포는 X시간 후 활성 상태가 된다
    2. 활성 상태가 되면 X 시간동안 생존하며, 첫 1시간동안 상하좌우로 번식한다
    3. 만약 동시에 같은 칸에 번식하게 된다면 생명력 수치가 높은 줄기 세포가 차지하여 번식한다
    4. K시간이 지난 후 비활성 상태 + 활성 상태의 줄기 세포의 총 개수를 구하라
상태:
    1. live_cell = 활성 상태 줄기세포
    2. wait_cell = 비활성 상태 줄기세포
    3. visited = 세포가 있는, 있었던 자리. set.
    4. wait_dict = 동시 번식을 확인하기 위한 딕셔너리
    5. next_live_cell = 다음 활성 상태 줄기세포
    6. next_wait_cell = 다음 비활성 상태 줄기세포
자료구조: 딕셔너리, visited, 델타 탐색
핵심로직:
    1. 활성 상태, 비활성 상태 줄기세포를 담는 리스트를 만든다
    2. while t < K: 반복문 돌린다.
    3. 초기 활성 상태인 줄기세포를 상하좌우로 번식시킨다
        0. 생명력과 대기시간이 일치하는 세포만 번식시킨다.
        1. visited에 그 칸이 있으면 번식하지 않는다.
        2. 동시 번식을 확인하기 위해 우선 딕셔너리에 담는다.
            1. 최대 생명력만 담으면 된다
        3. 모든 활성 줄기세포의 대기시간을 1 줄인다.
            1. 만약 대기시간이 0이 되었다면, 딕셔너리에 담지 않는다.
    4. 비활성화 세포들의 대기시간을 1 줄인다.
        1. 만약 대기시간이 0이 되었다면, next_live_cell 에 넣는다
        2. 다음 비활성화 세포 리스트에는 넣지 않는다.
    5. wait_dict를 순회하며 next_lice_cell에 넣는다
        1. visited에 좌표를 추가한다.
종료조건: t == K일때 종료. live_cell과 wait_cell의 길이를 더한 값을 출력한다.
시간복잡도: O(NM + KS)
"""

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 초기 변수 설정
    live_cell = []
    wait_cell = []
    visited = set()
    t = 0

    for r in range(N):
        for c in range(M):
            life = grid[r][c]
            if life >= 1:
                wait_cell.append((r, c, life, life))
                visited.add((r, c))

    while t < K:
        next_live_cell = []
        next_wait_cell = []
        wait_dict = {}

        for r, c, life, count in live_cell:
            if life == count:
                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]
                    point = (nr, nc)

                    if point in visited:
                        continue

                    wait_dict.setdefault(point, life)
                    if wait_dict[point] < life: # 동시 번식 해결
                        wait_dict[point] = life

            count -= 1

            if count == 0:  # 죽은 세포 처리
                continue

            next_live_cell.append((r, c, life, count))

        for point in wait_dict: # 번식한 얘들을 다음 비활성화 리스트로 이동
            (r, c) = point
            next_wait_cell.append((r, c, wait_dict[point], wait_dict[point]))
            visited.add(point)  # 방문 처리

        for r, c, life, count in wait_cell: # 비활성화 세포의 대기시간을 1 줄임
            count -= 1

            if count == 0:
                next_live_cell.append((r, c, life, life))
                continue

            next_wait_cell.append((r, c, life, count))

        # 1시간이 지남
        t += 1
        live_cell = next_live_cell
        wait_cell = next_wait_cell

    total_alive = len(live_cell) + len(wait_cell)

    print(f'#{tc} {total_alive}')
    
"""
목표: N x M 격자 내부에 줄기세포들이 주어진다. K 시간이 지난 후 살아있는 줄기세포의 수를 구하시오
상태: 
    1. time = 현재까지 지난 시간
    2. x, y, life, count = 좌표, 생명력, 목숨
자료구조: BFS, visited(세트 처리)
핵심 로직:
    1. 줄기세포들의 좌표와 생명력, 목숨을 unactivate 리스트에 담음
    2. activate 된 줄기세포를 순회하며 네 방향으로 번식함
        0. 이미 방문했다면 continue
        1. next_unactivate 딕셔너리에 번식할 줄기세포의 좌표와 생명력을 넣음
        2. activate 줄기세포들의 목숨을 1 감소시킴. 만약 0이 된다면 제거함
    3. unactivate 리스트에 있는 줄기세포들의 목숨(부화시간)을 1감소시킴. 만약 0이 된다면 activate로 이동함. 목숨도 초기화됨
    4. unactivate 리스트에 next_unactivate 딕셔너리에 있는 줄기세포들을 추가함. 만약 길이가 1보다 크다면, 생명력이 높은 줄기세포를 집어넣음
종료 조건: if time == K / 살아있는 줄기세포들의 수를 출력
"""

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    visited = set()
    time = 0
    unactivate = deque()
    activate = deque()

    for r in range(N):
        for c in range(M):
            life = grid[r][c]
            if life >= 1:
                unactivate.append((r, c, life, life))
                visited.add((r, c))

    while time < K:
        next_activate = deque()
        check_unactivate = {}
        for x, y, life, count in activate:

            if life == count:

                for i in range(4):  # 상하좌우 4방향으로 번식
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if (nx, ny) not in visited: # 동시 번식 확인 코드
                        check_unactivate.setdefault((nx, ny), [])
                        check_unactivate[(nx, ny)].append((nx, ny, life, life))

            count -= 1
            if count == 0:
                continue

            next_activate.append((x, y, life, count))

        next_unactivate = deque()

        for x, y, life, count in unactivate:    # 비활성화 세포들의 부화시간 1 감소
            count -= 1

            if count == 0:  # 부화 시간이 된 세포들을 부화시켜서 이동시킴
                next_activate.append((x, y, life, life))
                continue

            next_unactivate.append((x, y, life, count))

        for n in check_unactivate:  # 동시 번식 처리 코드
            if len(check_unactivate[n]) > 1:
                max_life = 0
                for x, y, life, count in check_unactivate[n]:
                    max_life = max(max_life, life)

                next_unactivate.append((x, y, max_life, max_life))
                visited.add((x, y))
                continue

            next_unactivate.append(check_unactivate[n][0])
            visited.add((n[0], n[1]))   # 방문 처리

        time += 1
        activate = next_activate
        unactivate = next_unactivate

    result = len(activate) + len(unactivate)
    print(f'#{tc} {result}')