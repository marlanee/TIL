# Segment Tree 심화

# 1단계. 백지 복습
# 문제1. 구간 대입 Lazy Propagtion

# def push(node, start, end):
#     if lazy[node] is None:
#         return
#     if start == end:
#         return

#     mid = (start + end) // 2
#     left = node * 2
#     right = node * 2 + 1    # 왜지? 왜 left와 right는 이런거지? 규칙? 그래. 이것은 규칙이다. 효율적 규칙
#     # 규칙의 조건
#     # 1. 서로 다른 노드의 인덱스가 충돌하지 않아야 한다.
#     # 2. 부모와 자식의 관계를 정확하게 찾을 수 있어야 한다
#     # 3. 모든 함수에서 동일한 규칙을 사용해야 한다
#     # 4. 가급적 시간 및 공간복잡도에 불이익이 없어야 한다.

#     tree[left] = (mid - start + 1) * lazy[node]
#     tree[right] = (end - mid) * lazy[node]

#     lazy[left] = lazy[node]
#     lazy[right] = lazy[node]

#     lazy[node] = None

# def range_query(node, start, end, left, right):
#     if start > right or end < left:
#         return 0

#     if left <= start and end <= right:
#         return tree[node]

#     mid = (start + end) // 2

#     push(node, start, end)

#     left_result = range_query(node * 2, start, mid, left, right)
#     right_result = range_query(node * 2 + 1, mid + 1, end, left, right)

#     return left_result + right_result

# 3. 문제 8. 혼합 push() 백지 구현
tree = [0] * (4 * N)
lazy = [[0, None] for _ in range(4 * N)]

# lazy[node][0]: 덧셈
# lazy[node][1]: 대입

def push(node, start, end):
    if not lazy[node][0] and lazy[node][1] is None: 
        return
    if start == end:
        return

    mid = (start + end) // 2
    left = node * 2
    right = node * 2 + 1

    if lazy[node][0]:
        tree[left] += (mid - start + 1) * lazy[node][0]
        tree[right] += (end - mid) * lazy[node][0]

        if lazy[left][1] is not None:
            lazy[left][1] += lazy[node][0]
        else:
            lazy[left][0] += lazy[node][0]
        if lazy[right][1] is not None:
            lazy[right][1] += lazy[node][0]
        else:
            lazy[right][0] += lazy[node][0]

    elif lazy[node][1] is not None:
        tree[left] = (mid - start + 1) * lazy[node][1]
        tree[right] = (end - mid) * lazy[node][1]

        lazy[left] = [0, lazy[node][1]]
        lazy[right] = [0, lazy[node][1]]

    lazy[node] = [0, None]