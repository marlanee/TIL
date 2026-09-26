# stack 1 연습문제 3

# 1차 시도: 19:34

# 목표: 정점과 간선들을 깊이 우선 탐색하여 경로를 출력하기
# 상태: graph = 정점들의 정보를 갖는 리스트
# 자료구조: graph, DFS
# 핵심 로직: 정점 1 호출 -> 루트 출력 -> 왼쪽 재귀호출 -> 오른쪽 재귀호출
# 종료 조건: DFS 호출이 종료되었을 때

def dfs(node):
    visited[node] = True

    print(node, end = '')

    for n in graph[node]:
        if not visited[n]:
            dfs(n)

N, S = map(int, input().split())

numbers = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(0, S * 2, 2):
    a, b = numbers[i], numbers[i + 1]
    graph[a].append(b)
    graph[b].append(a)

dfs(1)