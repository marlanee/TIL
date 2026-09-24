# SWEA 1952. 수영장

# 복습: PASS(18분)

# 목표: 1년치 수영장 사용 일수가 달 별로 주어질 때, 적절한 요금제를 사용해서 최저 요금을 구하여라
# 상태: cost = 현재까지의 누적 요금, month = 현재 개월 수
# 자료구조: DFS
# 핵심 로직: 
    # 1. 사용 가능한 1개월, 3개월 요금의 조합을 모두 탐색해서 최저 요금을 구한 후 Y와 비교
    # 2. 1개월 요금의 경우 D * list(month), M과 비교해서 최소값을 선택
# 종료 조건: 현재 누적 비용 > 현재 탐색 최솟값이면 return, month >= 12 일 경우 Y와 cost 비교 후 종료

def dfs(month, cost):
    global result

    if cost >= result:
        return

    if month >= 12:
        result = min(result, cost)
        return

    dfs(month + 1, cost + min(plan[month] * D, M))

    dfs(month + 3, cost + M3)

T = int(input())
for tc in range(1, T + 1):
    D, M, M3, Y = map(int, input().split())
    plan = list(map(int, input().split()))

    result = Y

    dfs(0, 0)

    print(f'#{tc} {result}')