# SWEA 5201. 컨테이너 운반
# 재밌겠다! 자기 암시, 자기 최면을 걸어야 한다. 끊임없이!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 1차 시도: PASS(15분)

# 목표: 
    # 1. N개의 컨테이너와 M개의 트럭이 주어진다. 트럭의 적재용량을 초과하는 컨테이너는 운반 할 수 없다.
    # 2. 중량이 최대가 되도록 컨테이너를 옮길 때, 화물의 전체 무게가 얼마인지 구하라.
# 상태: selected = 이미 선택된 화물
# 자료구조: greedy
# 핵심로직: 
    # 1. 트럭을 적재용량 오름차순으로 정렬함
    # 2. 가장 약한 트럭부터 선택되지 않은 컨테이너 중에서 적재 가능한 가장 무거운 컨테이너를 선택함
    # 3. 선택한 컨테이너는 선택 처리함
# 종료조건: 반복문이 종료되었을 때 total 출력
# 시간복잡도: O(NM)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    container = list(map(int, input().split()))
    trucks = sorted(map(int, input().split()))

    selected = [False] * N
    total = 0

    for t in trucks:
        current_max = 0
        for c in range(N):
            if not selected[c] and container[c] <= t:
                if current_max < container[c]:
                    current_max = container[c]
                    count = c

        if current_max == 0:
            continue

        total += container[count]
        selected[count] = True

    print(f'#{tc} {total}')