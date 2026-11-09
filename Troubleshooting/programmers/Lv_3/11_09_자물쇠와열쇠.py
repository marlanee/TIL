# 261106. Programmers 자물쇠와 열쇠
# 1차 시도: FAIL(1시간)
# 좌표 변환 FAIL
"""
목표: N x N 자물쇠와 M x M 열쇠가 주어진다.
    1. 자물쇠와 열쇠에는 홈(0)과 돌기(1)가 있다.
    2. 열쇠를 회전, 이동시켜서 자물쇠를 열 수 있으면 true, 없으면 false를 return하라
    3. 자물쇠의 모든 홈을 채우면 자물쇠를 열 수 있다
핵심로직: 시뮬레이션
    1. 우선 열쇠의 회전한 형태를 3개 만든다.(4번 회전시 원본과 동일)
    2. 왼쪽 상단부터 우측 하단까지 통과시키며 조건을 만족하는지 확인한다.
    3. 어떻게 통과시키며 더하지?
    4. 아니다. 0이 있는 좌표만 구하면 되는거 아닌가?
시간복잡도
"""

def solution(key, lock):
    N = len(lock)
    M = len(key)

    if all(v == 1 for row in lock for v in row):
        return True

    for _ in range(4):

        for offset_r in range(-M + 1, N):
            for offset_c in range(-M + 1, N):

                if check(key, lock, offset_r, offset_c):
                    return True

        key = [list(row) for row in zip(*key[::-1])]

    return False
        

def check(key, lock, offset_r, offset_c):
    N = len(lock)
    M = len(key)

    for r in range(N):
        for c in range(N):
            kr = r - offset_r
            kc = c - offset_c

            if 0 <= kr < M and 0 <= kc < M:
                value = key[kr][kc]
            else:
                value = 0

            if lock[r][c] + value != 1:
                return False

    return True

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
print(solution(key, lock))