# 261110. SWEA 3421. 수제 버거 장인
# 1차 시도: RuntimeError(60분) / 최적화 + isdisjoint()
# 11. 12 복습 필요
"""
목표: N개의 재료가 주어진다.
    1. N까지의 숫자를 이용해 가능한 조합을 만들어라
    2. 다만 grid에 속한 조합은 만들 수 없다.
    3. 만들 수 있는 조합의 개수가 몇 개인지 구하라
핵심 로직: frozenset
    1. 1부터 N개까지 만들 수 있는 조합을 frozenset으로 만든다
    2. grid에 이미 있다면 만들지 않는다.
    3. 없다면 total에 넣는다
    4. total의 길이를 출력한다.
시간복잡도:
"""
def dfs(idx, current_set):
    global answer

    answer += 1

    for j in range(idx + 1, N + 1):

        if not forbidden[j].isdisjoint(current_set):
            continue

        current_set.add(j)
        dfs(j, current_set)
        current_set.remove(j)

    
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    forbidden = [set() for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, input().split())
        forbidden[a].add(b)
        forbidden[b].add(a)

    answer = 0

    dfs(0, set())

    print(f'#{tc} {answer}')