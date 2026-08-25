# 2026-08-25. 2차 시도: FAIL

# 미루고 미루던 체스 문제다.
# 완전 탐색이 최선의 풀이 방법인 그 녀석 말이다.
# 마음의 짐이 된 녀석을 내려놓을 때가 되었다.

def chess(r, n, row, test1, test2):
    if r == n:
        return 1

    count = 0

    for i in range(n):
        d1 = r + i
        d2 = r - i + (N - 1)   # d1, d2변수가 왜 필요한지 모르겠다.

        if not row[i] and not test1[d1] and not test2[d2]:
            row[i] = test1[d1] = test2[d2] = True
            count += chess(r + 1, n, row, test1, test2)
            row[i] = test1[d1] = test2[d2] = False

    return count
    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    row = [False] * N
    test1 = [False] * (2 * N -1)
    test2 = [False] * (2 * N -1)    # 나는 아직도 왜 test1, 2가 필요한 코드인지 모른다.

    ans = chess(0, N, row, test1, test2)
    print(f'#{tc} {ans}')
