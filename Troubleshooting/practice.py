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