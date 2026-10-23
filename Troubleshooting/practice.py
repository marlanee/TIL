# 26. 10. 23.
# SWEA 1865. 동철이의 일 분배
# 2차 복습: PASS(15분)
# 졸업

"""
목표: N명의 직원에게 N개의 일을 하나씩 배분한다.
    1. i번 직원이 j번 일을 하면 성공할 확률이 Pij이다.
    2. 성공할 확률의 최댓값을 구하시오
상태: selected = 이미 선택된 일
자료구조: dfs/백트래킹
핵심로직: 완전 탐색
종료조건:
    1. 종료 조건 : staff == N: / 다 돌았으니 갱신 후 return
    2. 가지치기 : expect <= max_expect / 더 나아질 기미가 없으니 return
시간복잡도: O(N x N!)
"""

def dfs(staff, expect):
    global max_expect

    if expect <= max_expect:    # 가지치기
        return

    if staff == N:
        max_expect = max(max_expect, expect)
        return

    for work in range(N):
        if not selected[work]:

            selected[work] = True
            dfs(staff + 1, expect * grid[staff][work] / 100)
            selected[work] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    selected = [False] * N
    max_expect = 0

    dfs(0, 1)
    result = max_expect * 100

    print(f'#{tc} {result:.6f}')