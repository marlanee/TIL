# SWEA 3124. 최소 스패닝 트리

# 1차 시도: FAIL
# 복습: 20분(PASS) / Kruscal, Union-find! 새로 배운 개념들이다.
# 09.29. 복습 필요

# 목표: 
# def find(x):    # union의 대표를 반환함
#     if parent[x] != x:
#         parent[x] = find(parent[x])
#     return parent[x]

# def union(a, b):    # b를 a union으로 포섭함
#     ra = find(a)
#     rb = find(b)

#     if ra != rb:
#         parent[rb] = ra

# T = int(input())
# for tc in range(1, T + 1):
#     V, E = map(int, input().split())

#     parent = [i for i in range(V + 1)]  # 첫 시작은 각 정점의 대표자가 자기 자신!
#     edges = []  # 분류하기 쉽게 만드려고 만든 리스트

#     for _ in range(E):
#         a, b, cost = map(int, input().split())
#         edges.append((cost, a, b))

#     edges.sort()    # 비용 기준 오름차순으로 정렬

#     total = 0   # 총 비용?
#     count = 0   # 선택한 간선의 개수

#     for cost, a, b in edges:

#         if find(a) != find(b):
#             union(a, b)

#             total += cost
#             count += 1

#             if count == V - 1:
#                 break

#     print(f'#{tc} {total}')

# SWEA 3124. 최소 스패닝 트리

# 복습: 20분(PASS) / Kruscal, Union-find! 새로 배운 개념들이다.
# 09.29. 복습 필요

# 목표: 모든 V개의 정점을 연결하면서 가중치 합이 최소인 스패닝 트리 비용을 구하라.
# 상태: parents = 각 정점들의 대표자 리스트. package = 노드와 간선의 정보를 담은 리스트
# 자료구조: Kruscal + Union-find
# 핵심로직: 
    # # 1. 모든 간선을 가중치 기준 오름차순 정렬
    # 2. 가장 작은 간선부터 순회
    # 3. 두 정점의 대표자가 다르면 사이클이 생기지 않으므로 선택
    # 4. 두 집합을 union하고 가중치를 total에 더함
    # 5. V - 1개의 간선을 선택하면 MST 완성
# 종료조건: 선택한 간선의 개수가 V - 1개가 되면 total 출력 후 종료

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(A, B):

    Ax = find(A)
    Bx = find(B)

    if Ax != Bx:
        parents[Bx] = Ax

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    parents = [i for i in range(V + 1)]
    package = []

    for _ in range(E):
        A, B, C = map(int, input().split())
        package.append((C, A, B))

    package.sort()

    total = 0
    count = 0

    for price, A, B in package:

        if find(A) != find(B):
            union(A, B)
            count += 1
            total += price

        if count == V - 1:  # 간선의 개수가 V - 1이 됐다면, 노드의 개수는 V개.
            break

    print(f'#{tc} {total}')