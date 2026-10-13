# SWEA 2117. 홈 방범 서비스
# 1차 시도: FAIL(1시간) 마름모 구현 실패
# 10. 19. 복습 필요

"""
목표: 
    1. N x N 크기의 도시가 주어진다.
    2. 비용 손해를 보지 않으며 가장 많은 집에 홈 방법 서비스를 제공하고
    3. 그 때 서비스를 받는 집의 개수를 구하여라.
상태: 상태랄 것도 없음
자료구조: 단순 반복문 / 델타 탐색
핵심 로직:
    # 마름모의 중심 위치만 이동시키며 확인하면 되는 것 아닌가?
    1. 마름모의 크기를 1부터 시작해서 1씩 증가시키며 grid 순회
    2. 집이 범위 내에 있고, 운영 비용보다 수익이 많으면 max값 갱신
종료 조건: 서비스의 크기가 N + 1가 될 때 반복문 종료 후 max값 출력
시간 복잡도:
"""

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0 # 0보다 작을수는 없다.

    for i in range(1, N + 2):   # 마름모의 범위
        cost = i * i + (i - 1) * (i - 1)    # 비용

        for r in range(N):
            for c in range(N):

                count = 0    # 범위 내에 있는 집의 개수

                for xr in range(-i + 1, i):
                    width = i - 1 - abs(xr)

                    for xc in range(-width, width + 1):
                        nr = r + xr
                        nc = c + xc

                        if not (0 <= nr < N and 0 <= nc < N):
                            continue

                        if grid[nr][nc] == 1:
                            count += 1

                if count * M >= cost:
                    max_num = max(count, max_num)

    print(f'#{tc} {max_num}')