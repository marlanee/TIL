# 2026-08-24. 1차 시도: FAIL(30분)
# 거듭제곱을 재귀호출을 이용해서 구현하는 문제.


# def cal(n, m):
#     if m == M:
#         tn = n
#         return tn

#     n  = N * n
#     cal(n, m + 1)
#     return tn

# for _ in range(1, 11):
#     tc = int(input())
#     N, M = map(int, input().split())
#     print(f'#{tc} {cal(N, 0)}')

# 젠장, 나는 재귀호출에 왜 이리도 약할까? 극복하자.
# 아래는  gemini의 코드다.
# 재귀 함수는 N이 0, 1 + 2일때 잘 되면 수학적 귀납으로 잘 된다고 생각해라.
# 복잡한 상상은 의도적으로 멈춰라
def cal(n, m):
    if m == 0:
        return 1   # 1이 나오는 순간 역산하도록 코드를 짜야 한다.
    return n * cal(n, m - 1)   # return값을 지금은 모르게 만들어야 한다.

for _ in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())

    result = cal(N, M)
    print(f'#{tc} {result}')