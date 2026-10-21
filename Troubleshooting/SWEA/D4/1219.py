# SWEA 1219. 길찾기

# 1차 시도: PASS(30분)

# 목표: 출발지에서 목표까지 각 node를 거쳐 도착할 수 있는지 여부를 파악하라.
# 상태: Tree = 각 node의 정보를 담는 리스트, Visited = node가 이미 방문처리 되었는지 확인
# 자료구조: Tree
# 핵심로직: DFS 
# 종료 조건: 재귀 호출에서 99를 만나면 return 1, 아닐 경우 return 0

def path(node):
    if node == 99:
        return 1

    for next_node in tree[node]:
        
        if not visited[next_node]:
            visited[next_node] = True

            if path(next_node) == 1:
                return 1

    return 0


for _ in range(10):
    tc, N = map(int, input().split())

    tree = [[] for _ in range(100)]
    visited = [False] * (100)

    origin = list(map(int, input().split()))

    origin_len = len(origin)

    for i in range(0, origin_len, 2):
        start = origin[i]
        arrive = origin[i + 1]

        tree[start].append(arrive)

    visited[0] = True

    result = path(0)

    print(f'#{tc} {result}')