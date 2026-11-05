def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2

    build(node * 2, start, mid)
    build(node * 2 + 1, mid + 1, end)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

def query(node, start, end, left, right):
    # 1. 조회 구간과 겹치지 않는 경우
    if end < left or start > right:
        return 0
    # 2. 현재 노드 구간이 조회 구간에 완전히 포함되는 경우
    if left <= start and end <= right:
        return tree[node]
    # 3. 일부만 겹치는 경우
    # mid 계산
    mid = (start + end) // 2
    # 왼쪽과 오른쪽 자식 재귀 호출
    left_node = node * 2
    right_node = node * 2 + 1
    left_result = query(left_node, start, mid, left, right)
    right_result = query(right_node, mid + 1, end, left, right)
    # 두 결과 합산 후 반환
    return left_result + right_result

# build(), query()는 앞서 작성한 함수 사용

def update(node, start, end, idx, value):
    # 직접 구현
    if start == end:
        delta = value - tree[node]
        tree[node] = value
        return delta

    mid = (start + end) // 2
    if idx > mid:
        delta = update(node * 2 + 1, mid + 1, end, idx, value)
    else:
        delta = update(node * 2, start, mid, idx, value)

    tree[node] += delta

    return delta


N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]
tree = [0] * (4 * N)

build(1, 0, N - 1)

# M + K개의 연산 처리
for _ in range(M + K):
    a, b, c = map(int, input().split())

    # a == 1: update() 호출
    if a == 1:
        update(1, 0, N - 1, b - 1, c)
    # a == 2: query() 호출 및 결과 출력
    if a == 2:
        result = query(1, 0, N - 1, b - 1, c)

        print(result)