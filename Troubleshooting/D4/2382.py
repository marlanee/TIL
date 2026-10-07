# SWEA 2382. 미생물 격리
# 1차 시도: PASS(70분)
# 졸업. 와 드디어 내 스스로 통과했다.

"""
목표: 
    1. N x N 정사각형 셀이 주어진다
    2. 그 안에 미생물 군집이 들어있다.
    3. 미생물 군집은 1시간마다 이동방향 기준 다음칸으로 이동한다
    4. 미생물의 군집이 부딪히면 합체한다. 이 때, 합체한 군집의 방향은 합체 전 가장 큰 군집의 방향이다.
    5. 셀의 가장자리에는 약품이 칠해져 있다. 약품에 미생물이 부딪히면 미생물 수가 절반으로 줄어든다.
    6. M 시간 후 남아 있는 미생물 수의 총합을 구하라
상태: 
    1. current = 미생물들의 현재 위치와 상태
    2. check_dict = 미생물들의 다음 상태를 체크하기 위한 대기열 딕셔너리
    3. next = 미생물들의 다음 위치
    4. m = M을 2로 나눈 만큼의 시간
자료구조: dictionary, 델타 이동
핵심 로직:
    1. current에 좌표를 2배 확장시킨 미생물들의 위치와 상태를 담음
    2. m * 2 = M 이 될 때까지 미생물들을 한 칸씩 이동시킴
    3. 이동한 미생물들을 좌표에 따라 check_dict에 담음
    4. 만약 겹쳤다면 미생물 수를 합치고 방향을 정한 후 next에 담음
    5. 약품에 겹쳤다면 미생물 수를 절반으로 줄이고 방향을 반대로 바꿈. next에 집어넣음
    6. 아무것도 해당되지 않는다면 고대로 next에 집어넣음
종료 조건: while m * 2 < M: / current의 미생물 수를 합친 후 출력
시간 복잡도:
"""

dr = [0, -1, 1, 0, 0]
dc = [0, 0, 0, -1, 1]

reverse = [0, 2, 1, 4, 3]

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    current = []
    for _ in range(K):
        r, c, n, d = map(int, input().split())  
        current.append((r, c, n, d))

    count = 0

    while count < M:
        check_dict = {}
        next = []

        for r, c, n, d in current:  # 일단 모든 미생물들을 한 칸 이동시킴
            nr = r + dr[d]
            nc = c + dc[d]

            if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:    # 벽에 부딪히면서 합체할 수는 없으므로 바로 next로 직행
                nn = int(n / 2)

                if nn == 0:
                    continue

                nd = reverse[d]

                next.append((nr, nc, nn, nd))

                continue

            check_dict.setdefault((nr, nc), [])
            check_dict[(nr, nc)].append((nr, nc, n, d))

        for key in check_dict:
            if len(check_dict[key]) > 1:    # 미생물이 부딪힐 때를 처리하는 코드
                merge_n = 0
                check_d = 0
                merge_d = 0

                for nr, nc, n, d in check_dict[key]:
                    merge_n += n
                    if n > check_d:
                        check_d = n
                        merge_d = d

                next.append((nr, nc, merge_n, merge_d))

                continue

            next.append(check_dict[key][0])    # 아무 이벤트도 일어나지 않았을 경우

        count += 1  # 모든 미생물들을 한 칸 이동시키고 충돌 처리 했으므로 1초가 지남
        current = next  # next가 현재 위치로 바뀌는 순간. 

    result = 0

    for r, c, n, d in current:  # 살아남은 미생물들의 숫자 총합을 구하는 코드
        result += n

    print(f'#{tc} {result}')