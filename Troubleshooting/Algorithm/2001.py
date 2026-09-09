#. 파리채 문제. 1차 시도:

# 1. 목표: N x N 행렬에 있는 숫자들을 M x M 범위만큼 잘랐을 때 가장 큰 값은 무엇이 될 수 있는가?
# 2. 상태: total = sum(grid[r + i][c:c+M]) 을 파리채의 값으로 관리
# 3. 자료구조: 3중 반복문 r / c / i
# 4. 핵심로직: if sum(fly_map) > total, 갱신
# 5. 종료 조건: r 반복문이 N - M + 1 범위까지 반복문을 순회했을 때


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    total = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            current_total = 0
            for i in range(M):
                current_total += sum(grid[r + i][c:c + M])

            if total < current_total:
                total = current_total

    print(f'#{tc} {total}')