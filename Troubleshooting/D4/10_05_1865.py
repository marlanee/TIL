# SWEA 1865. 동철이의 일 분배

# 1차 시도: FAIL
# 9. 24. 복습 필요
# 복습: FAIL. 하나 누락(30분)
# 10. 5. 복습 필요

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

def dfs(staff, prob):
    global total

    if prob <= total:
        return
    
    if staff == N:
        total = max(total, prob)
        return

    for work in range(N):
        if not visited[work]:
            visited[work] = True
            dfs(staff + 1, prob * staffs[staff][work] / 100)
            visited[work] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    staffs = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N

    total = 0

    dfs(0, 1)

    print(f'#{tc} {(total * 100):.6f}')