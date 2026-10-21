# SWEA 1952. 수영장

# 1차 시도: FAIL
# 복습: PASS(18분)
# 졸업

# 목표: 1년치 수영장 사용 계획이 있다. 4가지 요금제를 적절히 사용하여 가장 저렴한 비용을 구하여라
# 상태: 
# 자료구조:
# 핵심로직:
    # 1. D의 조건: 1달에 이용날짜가 현저히 적을 때 사용 고려
    # 2. M의 조건: 1달에 이용날짜가 현저히 많을 때 사용 고려
    # 3. M3의 조건: 2~3달에 걸쳐 이용날짜가 현저히 많을 때 사용 고려
    # 4. Y의 조건: 모든 조건을 고려해도 Y가 가장 작을 때 사용
    # case 1: 모든 이용을 D로 이용
    # case 2: 모든 이용을 M으로 이용
    # case 3: 모든 이용을 M3로 이용
    # case 4: Y를 이용
    # 반복문을 돌리며 3달씩 순회.
    # 1달치 이용에서, D, M 중 저렴한 것을 선택 / 3개월만큼의 비용을 M3와 비교. 
    # 만약 M3보다 3개월 비용이 저렴하면 첫 1달치를 total에 더함
# 종료조건:

# def dfs(month, cost):
#     global min_cost

#     if cost >= min_cost:
#         return

#     if month >= 12:
#         min_cost = min(min_cost, cost)
#         return

#     dfs(month + 1, cost + min(D * plan[month], M))

#     dfs(month + 3, cost + M3)
    

# T = int(input())
# for tc in range(1, T + 1):
#     D, M, M3, Y = map(int, input().split())

#     plan = list(map(int, input().split()))

#     min_cost = Y

#     dfs(0, 0)

#     print(f'#{tc} {min_cost}')

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