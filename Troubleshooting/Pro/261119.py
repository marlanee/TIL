N = len(arr)
tree = [0] * (4 * N)
lazy = [[0, None] for _ in range(4 * N)]

# lazy[node][0]: 덧셈
# lazy[node][1]: 대입

def push(node, start, end):
    if start == end:
        return
    if lazy[node] == [0,None]:
        return

    left = node * 2
    right = node * 2 + 1
    mid = (start + end) // 2

    add = lazy[node][0]
    assign = lazy[node][1]

    if add:
        tree[left] += (mid - start + 1) * add
        tree[right] += (end - mid) * add

        if lazy[left][1] is not None:   # if lazy[left][0]를 쓰면 왜 안된다고 했더라?
            lazy[left][1] += add
        else:
            lazy[left][0] += add
        if lazy[right][1] is not None:
            lazy[right][1] += add
        else:
            lazy[right][0] += add

    else:
        tree[left] = (mid - start + 1) * assign
        tree[right] = (end - mid) * assign

        lazy[left] = [0, assign]
        lazy[right] = [0, assign]

    lazy[node] = [0, None]


def range_update(node, start, end, left, right, value, mode):
    if start > right or end < left:
        return
    if left <= start and end <= right:
        if mode == 'add':
            if lazy[node][1] is not None:
                lazy[node][1] += value
                tree[node] += (end - start + 1) * value
            else:
                lazy[node][0] += value
                tree[node] += (end - start + 1) * value
        else:
            lazy[node] = [0, value]
            tree[node] = (end - start + 1) * value

        return

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    push(node, start, end)

    range_update(left_node, start, mid, left, right, value, mode)
    range_update(right_node, mid + 1, end, left, right, value, mode)

    tree[node] = tree[left_node] + tree[right_node]
        

def range_query(node, start, end, left, right):
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    push(node, start, end)

    left_result = range_query(left_node, start, mid, left, right)
    right_reuslt = range_query(right_node, mid + 1, end, left, right)

    return left_result + right_reuslt