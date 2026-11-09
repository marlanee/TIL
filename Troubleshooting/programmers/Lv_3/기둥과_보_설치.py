# 261106. PGM. 기둥과 보 설치
# 1차 시도: 50분
# 힌트 PASS / 문제를 잘못 읽음

"""
목표: n x n 벽면이 주어진다.
    1. 규칙에 따라 기둥과 보를 설치하고
    2. 구조물의 상태를 return하라.
    3. 규칙에 맞지 않는 작업은 설치가 되지 않는다.
핵심 로직: 시뮬레이션
    1. 2차원 벽면을 두 개 만듦. False으로 가득 채운다. / 보, 기둥 벽면
    2. 보: 우측 아래 대각선에 기둥이 있거나, 바로 아래에 기둥이 있으면 설치 가능
        또한 좌측과 우측에 보가 있으면 설치 가능
    3. 기둥: 바닥이거나 아래에 기둥이 있으면 설치 가능
        또한 왼쪽에 보가 설치되어 있으면 설치 가능
시간복잡도:
"""


def solution(n, build_frame):
    beam = [[False] * (n + 1) for _ in range(n + 1)]
    pillar = [[False] * (n + 1) for _ in range(n + 1)]

    for x, y, a, b in build_frame:
        r, c = n - y, x  # y, x 좌표를 r, c 좌표로 변환

        if b == 1:
            if a == 0:  # 기둥일 경우
                if r == n or pillar[r + 1][c] or beam[r][c - 1] or beam[r][c]:
                    pillar[r][c] = True

            elif a == 1:    # 보일 경우
                if pillar[r + 1][c + 1] or pillar[r + 1][c] or (beam[r][c - 1] and beam[r][c + 1]):
                    beam[r][c] = True

        else:  # 철거
            # 1. 일단 철거
            if a == 0:
                pillar[r][c] = False
            else:
                beam[r][c] = False

            # 2. 남아 있는 모든 구조물의 유효성 검사
            valid = True

            for nr in range(n + 1):
                for nc in range(n + 1):

                    if pillar[nr][nc]:  # 기둥 검사
                        if not (
                            nr == n
                            or (nr < n and pillar[nr + 1][nc])
                            or (nc > 0 and beam[nr][nc - 1])
                            or beam[nr][nc]
                        ):
                            valid = False
                            break

                    if beam[nr][nc]:  # 보 검사
                        if not (
                            (nr < n and pillar[nr + 1][nc])
                            or (nr < n and nc < n and pillar[nr + 1][nc + 1])
                            or (
                                0 < nc < n
                                and beam[nr][nc - 1]
                                and beam[nr][nc + 1]
                            )
                        ):
                            valid = False
                            break

                if not valid:
                    break

            # 3. 유효하지 않다면 철거 취소
            if not valid:
                if a == 0:
                    pillar[r][c] = True
                else:
                    beam[r][c] = True



    total = []

    for r in range(n + 1):
        for c in range(n + 1):
            if pillar[r][c]:
                total.append((c, n - r, 0))
            if beam[r][c]:
                total.append((c, n - r, 1))

    answer = sorted(total)

    return answer


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))