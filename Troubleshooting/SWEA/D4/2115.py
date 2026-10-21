# SWEA 2115. 벌꿀 채취
# 재밌는 한 주의 시작이다. 상황이 뭐같아도 뭐든지 재밌다고 해야된다.
# FAIL(2시간) -> PASS(힌트 참조 후 5분) / 완전 탐색으로 DFS를 썼어야 했음. 하.
# SWEA 2115. 벌꿀 채취
# 복습: PASS(60분) 20분 + 함수 최적화 하려다가 40분 날리고 최적화 실패
# 10.19. 졸업

"""
목표: N x N 개의 벌통이 주어진다.
    1. 일꾼 두 명이 가로로 연속되게 M개의 벌통을 선택한다.
    2. 채취할 때, 꿀의 합이 C를 초과할 수 없다.
    3. 꿀의 제곱의 합이 수익이 된다.
    4. 채취하여 얻을 수 있는 최대 수익을 구하라.
상태: max_profit = 현재까지 찾은 최대 수익
자료구조: DFS
핵심 로직:
    1. grid를 r, c로 순회함
    2. M 범위만큼 1번 일꾼을 수확시킴
    3. 나머지 범위를 2번 일꾼을 수확시킴
    4. 각각의 일꾼들이 수확한 꿀의 최대 수익을 계산함
    5. 최대 수익을 갱신함
종료 조건: grid의 순회가 끝났을 때, 최대 수익을 반환
시간 복잡도: O(N^4 * 2^M)
"""

def dfs_1(idx, count, total, honey): # 최대 수익을 계산하는 dfs 함수
    global work_1
    # 꿀통을 선택하는 case 1, 안 하는 case 2

    if idx == M:
        work_1 = max(work_1, total)
        return

    dfs_1(idx + 1, count, total, honey)  # case 1

    if count + honey[idx] > C:
        work_1 = max(work_1, total)
        return
    
    # case 2
    dfs_1(idx + 1, count + honey[idx], total + honey[idx] ** 2, honey)

    return

def dfs_2(idx, count, total, honey): # 최대 수익을 계산하는 dfs 함수
    global work_2
    # 꿀통을 선택하는 case 1, 안 하는 case 2

    if idx == M:
        work_2 = max(work_2, total)
        return

    dfs_2(idx + 1, count, total, honey)  # case 1

    if count + honey[idx] > C:
        work_2 = max(work_2, total)
        return
    
    # case 2
    dfs_2(idx + 1, count + honey[idx], total + honey[idx] ** 2, honey)


T = int(input())
for tc in range(1, T + 1):
    N, M, C = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    max_profit = 0

    for r in range(N):
        for c in range(N - M + 1):  # M 범위만큼 탐색할 예정이므로 범위 설정
            worker_1 = grid[r][c:c + M] # 1번 일꿀이 수확한 벌통
            work_1 = 0
            dfs_1(0, 0, 0, worker_1)

            for r2 in range(r, N):  # 2번 일꾼 탐색 시작
                for c2 in range(N - M + 1):
                    if r2 == r and c2 < c + M:  # 같은 열 중복 탐색 회피
                        continue

                    worker_2 = grid[r2][c2:c2 + M]
                    work_2 = 0
                    dfs_2(0, 0, 0, worker_2)

                    max_profit = max(max_profit, (work_1 + work_2))

    print(f'#{tc} {max_profit}')

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