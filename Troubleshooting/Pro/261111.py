# 목표 학습량: 50분
# B형 대비

# 1. 개념 백지 복습 (10분) — Lazy Propagation의 불변식과 전파 원리
# 2. 독립 구현 (15분) — 구간 덧셈 + 구간 합 조회
# 3. 반례 및 디버깅 (15분) — 잘못된 구현의 원인을 추론
# 4. 실전 응용 (10분) — 시간복잡도와 구현 최적화

arr = [2, 4, 6, 8]
N = len(arr)

tree = [0] * (4 * N)
lazy = [0] * (4 * N)

def push(node, start, end):
    # 직접 구현
    if start == end or lazy[node] == 0: # 불필요한 전파 방지
        return

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    lazy[left_node] += lazy[node]
    lazy[right_node] += lazy[node] 

    tree[left_node] += (mid - start + 1) * lazy[node]
    tree[right_node] += (end - mid) * lazy[node]

    lazy[node] = 0

def range_update(node, start, end, left, right, value):
    # 직접 구현
    if start > right or end < left:
        return

    if left <= start and end <= right:
        tree[node] += (end - start + 1) * value
        lazy[node] += value
        return 

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    push(node, start, end)

    range_update(left_node, start, mid, left, right, value)
    range_update(right_node, mid + 1, end, left, right)

    tree[node] = tree[left_node] + tree[right_node]


def range_query(node, start, end, left, right):
    # 직접 구현
    if start > right or end < left:
        return 0

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    push(node, start, end)

    left_result = range_query(left_node, start, mid, left, right)
    right_result = range_query(right_node, mid + 1, end, left, right)

    return left_result + right_result

# 최종 과제 - 백지 구현

def range_update(node, start, end, left, right, value):
    # 백지 구현
    if start > right or end < left:
        return

    if left <= start and end <= right:
        tree[node] += (end - start + 1) * value
        lazy[node] += value
        return

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    push(node, start, end)

    range_update(left_node, start, mid, left, right, value)
    range_update(right_node, mid + 1, end, left, right, value)

    tree[node] = tree[left_node] + tree[right_node]