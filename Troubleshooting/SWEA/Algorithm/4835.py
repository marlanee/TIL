# 구간합. 1차 시도: PASS(20분)

# 1. 목표: 리스트 배열에서 M개의 합 중 가장 큰 값에서 가장 작은 값을 빼면 됨
# 2. 구조: 리스트 슬라이싱, M개씩 / list[i:i+M]
# 3. 종료: i가 N - M + 1에 도달했을 때

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    n = list(map(int, input().split()))
    t_max = t_min = sum(n[0:M]) # 최대/최소 초기화는 가능하면 실제 데이터로.
    for i in range(1, N - M + 1):
        c_sum = sum(n[i:i + M])
        if c_sum > t_max:
            t_max = c_sum
        if c_sum < t_min:
            t_min = c_sum

    total = t_max - t_min

    print(f'#{tc} {total}')