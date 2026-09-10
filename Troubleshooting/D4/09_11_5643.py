# 키 순서. 1차 시도: FAIL
# 09. 11. 복습 필요

# 1. 목표: N명의 학생의 키를 랜덤으로 두 명씩 뽑아 M 번 비교할 때, 키의 순서가 확정된 학생의 수를 구하라.
# 2. 상태
    # 1. up[i]: i보다 크다고 확인된 학생들
    # 2. down[i]: i보다 작다고 확인된 학생들
    # 3. visited: i를 기준으로 DFS/BFS를 했을 때 직접, 간접적으로 관계가 확인된 학생

# 모든 학생과 직접, 간접 비교가 있는 학생만이 순서가 확정되었다고 볼 수 있다.

# 작거나 큰 건 문제가 되지 않는다.

def dfs(start, graph, N):
    visited = [False] * (N + 1)
    stack = [start]
    visited[start] = True

    count = 0

    while stack:
        now = stack.pop()

        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)
                count += 1

    return count

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    M = int(input())

    up = [[] for _ in range(N + 1)]
    down = [[] for _ in range(N + 1)]

    count = 0

    for _ in range(M):
        small, tall = map(int, input().split())
        up[small].append(tall)
        down[tall].append(small)

    answer = 0


    for student in range(1, N + 1):
        taller = dfs(student, up, N)
        shorter = dfs(student, down, N)

        if taller + shorter == N - 1:
            answer += 1

    print(f'#{tc} {answer}')