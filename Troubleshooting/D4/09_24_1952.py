# SWEA 1952. 수영장

# 1차 시도: FAIL
# 9. 23. 복습 필요

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

def dfs(month, cost):
    global min_cost

    if cost >= min_cost:
        return

    if month >= 12:
        min_cost = min(min_cost, cost)
        return

    dfs(month + 1, cost + min(D * plan[month], M))

    dfs(month + 3, cost + M3)
    

T = int(input())
for tc in range(1, T + 1):
    D, M, M3, Y = map(int, input().split())

    plan = list(map(int, input().split()))

    min_cost = Y

    dfs(0, 0)

    print(f'#{tc} {min_cost}')