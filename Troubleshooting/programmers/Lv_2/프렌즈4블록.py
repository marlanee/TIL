# 261106. 프로그래머스. 프렌즈 4블록
# 1차 시도: PASS(24분)
# 졸업
"""
핵심로직: m * n 판이 주어진다.
    1. 판을 2 x 2 격자로 탐색하며 모든 칸이 동일하다면 delete 세트에 넣는다
    2. delete 세트를 반복문으로 꺼내서 해당 좌표들을 모두 0 으로 바꾼다
    3. 중력 처리한다.
    4. 1번을 반복한다.
    5. 만약 delete 세트가 비었다면 종료한다.
    6. 종료 후 0의 개수를 출력한다
시간복잡도: O(NM)
"""

def solution(m, n, board):

    board = [list(row) for row in board]

    while True:
        delete = set()

        for r in range(m - 1):
            for c in range(n - 1):
                block = board[r][c]
                if block == '0':
                    continue
                if block == board[r][c + 1] == board[r + 1][c] == board[r + 1][c + 1]:
                    for i in range(2):
                        for j in range(2):
                            delete.add((r + i, c + j))

        if not delete:
            break

        for r, c in delete:
            board[r][c] = '0'

        # 중력 처리
        for c in range(n):
            next_col = []
            for r in range(m):
                current = board[r][c]
                if current != '0':
                    next_col.append(current)

            for r in range(m - 1, -1, -1):
                if not next_col:
                    board[r][c] = '0'
                    continue
                board[r][c] = next_col.pop()

    answer = 0

    for row in board:
        answer += row.count('0')

    return answer