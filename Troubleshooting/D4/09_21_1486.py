# SWEA 1486. 장훈이의 높은 선반

# 1차 시도: PASS(40분)
# 9. 21. 복습 필요. 선택 / 미선택 DFS 방식으로.

# 목표: N개의 숫자 중 일부 또는 전체를 조합하여(combined) B 이상의 숫자를 만드려고 한다. 이 때 combined - B 를 구하시오
# 상태: height = 직원들의 키를 담은 리스트. / candidate = set()
# 자료구조: DFS
# 핵심로직: 
    # 1. idx 이후의 직원을 하나씩 선택하여 새로운 부분집합을 만듦
    # 2. 현재 합이 B 이상이면 해당 가지에서는 추가 선택 중단
# 종료조건: 
    # 1. 현재 키의 합 h >= B 이면 후보값을 갱신하고 return
    # 2. 더 이상 선택할 직원이 없으면 재귀가 자연스럽게 종료

def find_tall(idx, h):
    global best

    if h >= best:
        return

    if h >= B:
        best = min(best, h)
        return

    for i in range(idx + 1, N):
        find_tall(i, h + height[i])

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    best = float('inf')

    for idx in range(N):
        find_tall(idx, height[idx])

    result = best - B

    print(f'#{tc} {result}')