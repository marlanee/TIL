# SWEA 4012. 요리사.

# 1차 시도: FAIL(문제를 잘못 봄) / PASS(30분)

# 목표: 
    # 1. 양의 정수로 가득찬 N x N 2차원 격자가 주어진다.
    # 2. 재료가 겹치지 않게 N / 2 개를 선택하여 두 개의 음식을 만들어라
    # 3. 결론은 r, c 가 하나도 겹치지 않게 선택하여 grid[r][c] + grid[c][r]를 더한 두 개의 합의 차의 최소를 구하는 것
# 상태: grid = 오리지널 음식판, synergy = 음식마다 주어진 점수, used_row, used_col = 이미 사용된 음식
# 자료구조: DFS, visited
# 핵심 로직: 
    # 1. dfs로 synergy를 이용해 만들 수 있는 N / 2개의 조합을 모두 탐색.
    # 2. N / 2개의 조합과 나머지 조합의 차를 계속 갱신함
# 종료 조건: 함수 내부: food == N / 2 일 때, 최종: 반복문이 종료되었을 떄

def dfs(start, count):
    global result

    if count == N // 2:
        food_1 = []
        food_2 = []
        for idx, x in enumerate(selected):
            if x:
                food_1.append(idx)
            else:
                food_2.append(idx)

        f1, f2 = 0, 0

        for i in range(N // 2 - 1):
            for j in range(i + 1, N // 2):
                f1 += grid[food_1[i]][food_1[j]] + grid[food_1[j]][food_1[i]]
                f2 += grid[food_2[i]][food_2[j]] + grid[food_2[j]][food_2[i]]

        result = min(result, abs(f1 - f2))
        return

    for i in range(start, N):
        selected[i] = True
        dfs(i + 1, count + 1)
        selected[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    selected = [False] * N
    result = float('inf')

    selected[0] = True
    dfs(1, 1)

    print(f'#{tc} {result}')