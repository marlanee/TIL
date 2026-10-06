# SWEA 2115. 벌꿀 채취
# 재밌는 한 주의 시작이다. 상황이 뭐같아도 뭐든지 재밌다고 해야된다.
# FAIL(2시간) -> PASS(힌트 참조 후 5분) / 완전 탐색으로 DFS를 썼어야 했음. 하.


"""
목표: N x N 벌통이 주어짐. 두 명의 일꾼이 가로로 M 길이로 꿀을 채취함. 이 때 총 채취양은 C를 초과할 수 없음. 
하나를 담았을 때 초과한다면 다시 내려놓아야 함. 채취를 마친 뒤 판매를 시작함. 판매금은 각 꿀의 양의 제곱의 합임
이 때 최대 수익을 내도록 꿀을 채취하는 프로그램을 작성하라.
상태: expect = grid[r][c:c+M]을 채취했을 때 얻을 수 있는 최대 기대값, visited = 이미 방문한 expect
자료구조: 완전 탐색?
핵심 로직:
1. 벌통을 순회 / 1번 일꾼이 지정된 범위 내에서 가장 높은 기대값의 꿀만 채취 / 방문 처리
for r in range(N)
    for c in range(N - M + 1)
        current = reversed(grid[r][c:c + M])
        visited[r][c:c + M] = [True] * M
        selected = []
        for honey in current:
            if honey <= C and sum(selected) + honey <= C:
                selected.append(honey)
            if sum(selected) == C:
                break
                
2. dfs로 방문하지 않은 벌통 방문, 가장 높은 기댓값의 벌통 선택
dfs(r, c)

1-2번 접근로 폐기. 시간복잡도가 너무 큼

New 1. 벌통을 순회하여 expect라는 리스트를 채움. grid[r][c] 자리에 grid[r][c:c + M]으로 얻을 수 있는 기대값을 입력하는 것임
New 2. expect를 순회하며 방문 처리되지 않는 벌통 중 최대값을 선택함
New 3. 그 최대값을 갱신함.
                
            
종료 조건: 반복문의 순회가 종료되었을 때
시간 복잡도: 계산중
"""

def dfs(idx, honey_sum, profit):
    global current_max

    if idx == M:
        current_max = max(current_max, profit)
        return

    dfs(idx + 1, honey_sum, profit)

    if honey_sum + current[idx] > C:
        return

    dfs(idx + 1, honey_sum + current[idx], profit + current[idx] ** 2)

T = int(input())

for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    expect = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    max_expect = 0

    for r in range(N):
        for c in range(N - M + 1):
            current = grid[r][c:c + M]
            current_max = 0

            dfs(0, 0, 0)

            expect[r][c] = current_max

    for r in range(N):  
        for c in range(N - M + 1):
            visited[r][c:c + M] = [True] * M

            for i in range(N):
                for j in range(N - M + 1):
                    if visited[i][j] == True:
                        continue
                    max_expect = max(max_expect, expect[r][c] + expect[i][j])

            visited[r][c + 1:c + M] = [False] * (M - 1)

    print(f'#{tc} {max_expect}')