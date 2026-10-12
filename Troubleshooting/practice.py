# SWEA 1865. 동철이의 일 분배
# 복습: PASS(45분)

"""
목표: N명의 직원이 있는 회사에 N개의 일이 주어짐. 직원별로 n의 일 성공률이 다름. 
하나의 일은 하나의 직원에게만 배분 가능함. 모든 일을 처리할 최고 성공률을 구하라
상태: selected = 선택된 일, max_result = 가능한 최대값, staffs = 일을 선택한 직원의 수, percent = 현재까지의 누적 성공률
자료구조: DFS / 백트래킹
핵심로직: 감이 잡히지 않아 코드를 작성하며 로직 구현함
종료조건: 감이 잡히지 않아 코드를 작성하며 로직 구현함
시간 복잡도: 계산중
"""

def dfs(staffs, percent):
    global max_result

    if percent <= max_result:   # 가지치기. 성공률이 이미 더 낮다면 진행할 필요가 없다
        return

    if staffs == N:  # 종료 조건
        max_result = max(max_result, percent)
        return

    for i in range(N):
        if not selected[i]:
            selected[i] = True
            dfs(staffs + 1, percent * grid[staffs][i] / 100) # i 번째 일을 선택함
            selected[i] = False
    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_result = 0  # 0보다 낮을 확률은 없다.
    selected = [False] * N

    dfs(0, 1)

    total = max_result * 100

    print(f'#{tc} {total:.6f}')