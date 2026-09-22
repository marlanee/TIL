# SWEA 3124. 최소 스패닝 트리

# 1차 시도: 20:37

# 목표: 
def find(x):    # union의 대표를 반환함
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):    # b를 a union으로 포섭함
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    parent = [i for i in range(V + 1)]  # 첫 시작은 각 정점의 대표자가 자기 자신!
    edges = []  # 분류하기 쉽게 만드려고 만든 리스트

    for _ in range(E):
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort()    # 비용 기준 오름차순으로 정렬

    total = 0   # 총 비용?
    count = 0   # 선택한 간선의 개수

    for cost, a, b in edges:

        if find(a) != find(b):
            union(a, b)

            total += cost
            count += 1

            if count == V - 1:
                break

    print(f'#{tc} {total}')