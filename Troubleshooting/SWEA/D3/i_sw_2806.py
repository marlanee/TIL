# 2026-08-19. 1차 시도: FAIL 피드백: None
# 2026-08-25. 2차 시도: FAIL
# N-Queen
# 희한한 문제네. 퀸의 이동 방식을 모두가 알고 있다고 생각하는건가?
# N * N 체스판에서 N개의 퀸을 배치했을 때, 퀸들끼리 공격이 안되게 놓는 경우의 수를 구하시오
# 2차원 행렬을 그린다. (N * N) 그곳 퀸을 배치한다.
# 이 때, 각 퀸의 대각선, 열, 행에 다른 퀸이 있어서는 안된다.
# 퀸들끼리 구분하지는 않겠지. 구분하게 된다면 결과에 N!을 곱해야 될 것이다.
# 빈 칸을 0으로, 퀸을 1로 만들자.
# 이 서늘한 완전 탐색의 기운은 뭐지? 아니겠지.

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     # 한 가지 자명한 사실은, 한 행, 한 열에는 하나의 퀸만 들어간다는 사실이다.
#     # 일단 행렬 체스판 하나를 그려보자.
#     grid = [[0] * N for _ in range(N)]
#     # 조건 1 `1 not in row`
#     # 조건 2 `1 not in column`
#     # 조건 3 `1 not 대각선`
#     # 첫 번째 퀸이 첫 행에 들어갈 수 있는 경우의 수 = N
#     # 두 번째 퀸이 둘째 행에 들어갈 수 있는 경우의 수 = N - 2(N- 3의 경우는 모서리. 그러나 이 경우 다음번 경우의 수가 N - 4로 바뀜.)
#     # 세 번째 퀸이 셋째 행에 들어갈 수 있는 경우의 수 = N - 4

# 짜증나. 분노가 차오른다. 이런 문제도 못 풀다니.
# 아래는 Gemini의 코드다
# def solve_n_queen(row, n, used_col, used_diag1, used_diag2):
#     if row == n:
#         return 1

#     count = 0
#     for col in range(n):
#         d1 = row + col
#         d2 = row - col + (N - 1)   # 이건 뭐지? 뒤로부터 세는 변수? 

#         if not used_col[col] and not used_diag1[d1] and not used_diag2[d2]:   # 세 리스트에 전부 True가 없을 경우
#             used_col[col] = used_diag1[d1] = used_diag2[d2] = True   # 이건 뭐지? 세 리스트 요소를 한 번에 True로 바꾸는거야? 맞네. 이런게 가능하다니.
#             count += solve_n_queen(row + 1, n, used_col, used_diag1, used_diag2)
#             used_col[col] = used_diag1[d1] = used_diag2[d2] = False

#     return count

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     used_col = [False] * N
#     used_diag1 = [False] * (2 * N - 1)   # 왜 2*N -1이지? 왜 False로 가득한 리스트를 만들었지?
#     used_diag2 = [False] * (2 * N - 1)

#     ans = solve_n_queen(0, N, used_col, used_diag1, used_diag2)
#     print(f'#{tc} {ans}')

# 미루고 미루던 체스 문제다.
# 완전 탐색이 최선의 풀이 방법인 그 녀석 말이다.
# 마음의 짐이 된 녀석을 내려놓을 때가 되었다.

# def chess(r, n, row, test1, test2):
#     if r == n:
#         return 1

#     count = 0

#     for i in range(n):
#         d1 = r + i
#         d2 = r - i + (N - 1)   # d1, d2변수가 왜 필요한지 모르겠다.

#         if not row[i] and not test1[d1] and not test2[d2]:
#             row[i] = test1[d1] = test2[d2] = True
#             count += chess(r + 1, n, row, test1, test2)
#             row[i] = test1[d1] = test2[d2] = False

#     return count
    

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())

#     row = [False] * N
#     test1 = [False] * (2 * N -1)
#     test2 = [False] * (2 * N -1)    # 나는 아직도 왜 test1, 2가 필요한 코드인지 모른다.

#     ans = chess(0, N, row, test1, test2)
#     print(f'#{tc} {ans}')

# N-Queen. 풀이 시간: Fail

# 그 녀석을 다시 만났다.
# 날 일주일간 괴롭힌 그 녀석.
# 지금의 나는 충분히 해결할 수 있다.
# 라고 믿어야 한다.

# 1. 목표: N * N 행렬 체스판에 N 개의 퀸을 서로 공격하지 못하게 두는 경우의 수를 구하는 것
# 2. 구조: 완전 탐색. 
    # 1. 일단 첫 번 째 칸에 퀸을 두고, 다음 열로 넘어간다. 
    # 2. 다음 열의 첫 번쨰 칸부터 마지막 칸 까지 퀸을 둔다. 놓을 수 있다면 놓고, 아니면 되돌아간다.
    # 3. 이것을 마지막 열까지 반복한다. 성공했다면 count에 1을 더한다.
# 3. 종료 조건: 첫 번째 재귀함수의 col이 N - 1열에 도달 후 모든 작업이 종료되었을 때

# 아래는 GPT의 코드다.
def Queen(row):
    if row == N:
        return 1

    count = 0

    for col in range(N):
        d1 = row + col
        d2 = row - col + N -1

        if not used_col[col] and not used_diag1[d1] and not used_diag2[d2]:
            used_col[col] = True
            used_diag1[d1] = True
            used_diag2[d2] = True

            count += Queen(row + 1)

            used_col[col] = False
            used_diag1[d1] = False
            used_diag2[d2] = False

    return count

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    used_col = [False] * N    # 내가 왜 이런 False 리스트를 작성하고 있는지 이유를 모르겠다.
    used_diag1 = [False] * (2 * N - 1)  # 내가 왜 이런 False 리스트를 작성하고 있는지 이유를 모르겠다.
    used_diag2 = [False] * (2 * N - 1)  # 내가 왜 이런 False 리스트를 작성하고 있는지 이유를 모르겠다.

    answer = Queen(0)

    print(f'#{tc} {answer}')