# SWEA 1865. 동철이의 일 분배

# 1차 시도: FAIL
# 9. 24. 복습 필요
# 복습: FAIL. 하나 누락(30분)
# 10. 5. 복습 필요
# 10. 12. 복습: PASS(45분)
# 10. 19. 복습 필요
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
# 목표: N명의 직원들에게 N개의 일을 중복 없이 시킬 때, 가장 높은 성공률을 구하여라.
# 상태: Tree = N개의 직원마다 N개의 일을 성공할 확률을 담는 리스트. visited = 직원에게 일이 주어졌는지 확인하는 리스트
# 자료구조: Tree, visited, dfs
# 핵심로직: dfs로 모든 경우의 수를 탐색
# 종료 조건: 순회문이 종료되었을 때

# def dfs(staff, prob):
#     global result

#     if prob <= result:
#         return

#     if staff == N:
#         result = max(result, prob)
#         return

#     for task in range(N):
#         if not visited[task]:
#             visited[task] = True
#             dfs(staff + 1, prob * tree[staff][task] / 100)
#             visited[task] = False

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())

#     tree = [[] for _ in range(N)]
#     visited = [False] * (N)
#     result = 0

#     for i in range(N):
#         tree[i] = list(map(int, input().split()))

#     dfs(0, 1)

#     print(f'#{tc} {result * 100:.6f}')

    # SWEA 1865. 동철이의 일 분배

# 복습: FAIL. 하나 누락(30분)
# 10. 5. 복습 필요

# 목표: N명의 직원들에게 N개의 일을 분배할 때, 가장 높은 성공률을 구하여라.
# 상태: visited = 이미 분배된 일인지 확인. total = 전체 성공률
# 자료구조: DFS, visited
# 핵심 로직: 모든 경우의 수를 탐색하며 가장 높은 확률로 total을 갱신
# 종료 조건: dfs가 끝났을 때 total을 반환

# def dfs(staff, prob):
#     global total

#     if prob <= total:
#         return
    
#     if staff == N:
#         total = max(total, prob)
#         return

#     for work in range(N):
#         if not visited[work]:
#             visited[work] = True
#             dfs(staff + 1, prob * staffs[staff][work] / 100)
#             visited[work] = False


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())

#     staffs = [list(map(int, input().split())) for _ in range(N)]

#     visited = [False] * N

#     total = 0

#     dfs(0, 1)

#     print(f'#{tc} {(total * 100):.6f}')

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