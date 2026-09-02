# 색칠하기. 1차 시도: PASS(20분)

# 1. 상태: 빨간색, 파란색을 가진 직사각형 N개가 구해진다.
# 2. 행동: 빨간색, 파란색 직사각형이 겹치는 부분을 구한다.
# 3. 종료 조건: 겹치는 부분이 구해졌을 때.
# 4. Keyword: 빨강을 1, 파랑을 2로 해서 grid에 더하고, 3 요소의 합을 구한다.

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)]
    color = [list(map(int, input().split())) for _ in range(N)] # 직사각형 정보들을 리스트로 담음
    for i in range(N):
        for r in range(color[i][0], color[i][2] + 1):
            for c in range(color[i][1], color[i][3] + 1):
                grid[r][c] = grid[r][c] + color[i][4]

    count = 0

    for row in grid:
        count += row.count(3)

    print(f'#{tc} {count}')