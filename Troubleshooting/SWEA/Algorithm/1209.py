# Sum. 1차 시도: PASS(25분)

# 1. 상태: 숫자로 가득 찬 100 x 100 행렬이 주어짐.
# 2. 행동: 각 행, 열, 대각선의 합을 구해야 함
# 3. 종료: 각 행, 열, 대각선의 합 중 최댓값을 구하면 종료.

for _ in range(10):
    tc = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]

    # 열과 행의 합을 구하자.
    # 행을 열로 전치한다.
    col_grid = list(zip(*grid))
    # 이제 열과 행을 합친 total_grid 를 생성한다.
    total_grid = grid + col_grid
    current_max = max(map(sum, total_grid))

    # 이제 대각선의 합을 구한다.
    diag1 = sum(grid[i][i] for i in range(100))  # 우하단 대각선의 총합을 담는 변수
    diag2 = sum(grid[i][99 - i] for i in range(100))
    
    print(f'#{tc} {max(current_max, diag1, diag2)}')