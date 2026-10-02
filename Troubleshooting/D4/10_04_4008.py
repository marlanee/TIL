# SWEA 4008. 숫자 만들기
# 영원이 거짓임은 영원하다.
# 나의 거짓됨도 영원하리.
# 고독과 사색과 고통과 회피
# 1차 시도: FAIL(1시간)-Runtimeerror -> 힌트로 PASS

"""
목표: 
    1. N 개의 숫자가 주어진다. N - 1개의 연산자 카드도 주어진다.
    2. 만들 수 있는 수식의 최댓값과 최솟값의 차를 구하라.
상태: cmd = 연산자(N - 1)개, numbers = 숫자(N)개
자료구조: dfs이지 않을까 싶음, visited 도 쓰여야 되지 않을까 싶음, 그러면 백트래킹도 쓰여야 함
핵심로직: 연산자를 넣은 수식을 dfs로 완전 탐색하고 최댓값과 최솟값을 찾아볼까
종료조건: 완전 탐색이 끝나면 최댓값 - 최솟값 출력
시간복잡도: 글쎄, 풀어봐야 알겠지. O(N!)
"""
"""
def dfs(number, command):
    global max_num, min_num

    if command == N - 1:
        max_num = max(max_num, number)
        min_num = min(min_num, number)
        return

    for i in range(N - 1):
        if visited[i]:
            continue

        visited[i] = True

        if cmd[i] == 0:
            a = number + numbers[command + 1]
            dfs(a, command + 1)
        elif cmd[i] == 1:
            b = number - numbers[command + 1]
            dfs(b, command + 1)
        elif cmd[i] == 2:
            c = number * numbers[command + 1]
            dfs(c, command + 1)
        else:
            d = int(number / numbers[command + 1])
            dfs(d, command + 1)

        visited[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    origin = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    cmd = []

    for c in range(4):
        cmd.extend([c] * origin[c])

    max_num = float('-inf')
    min_num = float('inf')
    visited = [False] * N

    dfs(numbers[0], 0)

    print(f'#{tc} {max_num - min_num}')
"""

def dfs(number, command):
    global max_num, min_num

    if command == N - 1:
        max_num = max(max_num, number)
        min_num = min(min_num, number)
        return

    for i in range(4):
        if origin[i] == 0:
            continue

        origin[i] -= 1

        if i == 0:
            a = number + numbers[command + 1]
            dfs(a, command + 1)
        elif i == 1:
            b = number - numbers[command + 1]
            dfs(b, command + 1)
        elif i == 2:
            c = number * numbers[command + 1]
            dfs(c, command + 1)
        else:
            d = int(number / numbers[command + 1])
            dfs(d, command + 1)

        origin[i] += 1



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    origin = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_num = float('-inf')
    min_num = float('inf')

    dfs(numbers[0], 0)

    print(f'#{tc} {max_num - min_num}')