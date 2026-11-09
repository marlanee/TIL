# 261109. 세그먼트 트리 기초 구현 단계 PASS

arr = [5, 2, 8, 1, 7, 3, 6, 4]

N = len(arr)
tree = [0] * (4 * N)

# build 함수 작성
def build(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    left = node * 2
    right = node * 2 + 1

    build(left, start, mid)
    build(right, mid + 1, end)

    tree[node] = min(tree[left], tree[right])

# query 함수 작성
def query(node, start, end, left, right):
    # 아예 범위에서 벗어났으면
    if end < left or right < start:
        return float('inf')

    # 완전히 포함되어 있으면
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_node = query(node * 2, start, mid, left, right)
    right_node = query(node * 2 + 1, mid + 1, end, left, right)

    return min(left_node, right_node)

# update 함수 작성

def update(node, start, end, idx, value):
    if start == end:
        tree[node] = value
        return

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    if idx <= mid:
        update(left_node, start, mid, idx, value)
    else:
        update(right_node, mid + 1, end, idx, value)

    tree[node] = min(tree[left_node], tree[right_node])

    


build(1, 0, N - 1)

print(query(1, 0, N - 1, 2, 6))  # 1

update(1, 0, N - 1, 3, 9)

print(query(1, 0, N - 1, 2, 6))  # 3
print(query(1, 0, N - 1, 0, 7))  # 2