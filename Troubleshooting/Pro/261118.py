"""
1. 혼합 Lazy propagtion
2. 연산 순서의 역전
3. 혼합 push() 백지 구현
"""

# 3.
tree = [0] * (4 * N)
lazy = [[0, None] for _ in range(4 * N)]

# lazy[node][0]: 덧셈
# lazy[node][1]: 대입
def push(node, start, end):
    if not lazy[node][0] and lazy[node][1] is None:
        return
    if start == end:    # 리프 노드는 어차피 lazy값이 없는거 아닌가? 이 코드, 필요한가? 필요하다. 리프에도 lazy가 전파된다
        return

    mid = (start + end) // 2
    left = node * 2
    right = node * 2 + 1

    plus = lazy[node][0]
    insert = lazy[node][1]

    if plus:
        tree[left] += (mid - start + 1) * plus
        tree[right] += (end - mid) * plus

        if lazy[left][1] is not None:
            lazy[left][1] += plus
        else:
            lazy[left][0] += plus

        if lazy[right][1] is not None:
            lazy[right][1] += plus
        else:
            lazy[right][0] += plus

    else:
        tree[left] = (mid - start + 1) * insert
        tree[right] = (end - mid) * insert

        lazy[left] = [0, insert]  # 이러면 동일한 객체를 참조하게 된다...
        lazy[right] = [0, insert]

    lazy[node] = [0, None]
