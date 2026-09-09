# 회문. 1차 시도: PASS(15분)

# 1. 목표: N x N 행렬에서 길이가 M인 회문을 찾아 출력하기
# 2. 상태: grid[r][c:c+M] 가 원본 글자
# 3. 자료구조: 행렬 전치, 리스트 슬라이싱
# 4. 핵심 로직: word = grid[r][c:c+M], if word == word[::-1], print, break
# 5. 종료 조건: 회문을 찾았을 때, print(f'#{tc} {word}')
def find_word(grid, N, M):
    for r in range(2 * N):
        for c in range(N - M + 1):
            word = grid[r][c:c + M]

            if word == word[::-1]:
                return ''.join(word)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    row_grid = [list(input()) for _ in range(N)]
    col_grid = list(zip(*row_grid))
    grid = row_grid + col_grid

    print(f'#{tc} {find_word(grid, N, M)}')