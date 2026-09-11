# SWEA 3307. 최장 증가 부분 수열
# 1차 시도: FAIL(30분)
# 09. 14. 복습 필요

# Pycharm을 처음 써본다. 이거 좋나? 좀 구린 것 같은데. 흠. 아무튼 좋다.

# 1. 목표: 길이 N의 전체 수열에서 오름차순으로 가능한 가장 긴 부분 수열의 길이.
# 2. 상태: dp[i] = numbers[i]를 마지막 원소로 하는 최장 증가 부분 수열의 길이.
# 3. 자료구조: DP
# 4. 핵심 로직
#     1. 점화식, DP
# 5. 종료 조건: 반복문이 완전히 종료된 후 max_len 출력
T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    dp = [1] * N

    for i in range(N):
        for j in range(i):
            if numbers[j] < numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f'#{tc} {max(dp)}')

# Greedy로는 택도 없음. 1 5 2 3 4 에서 막힘.