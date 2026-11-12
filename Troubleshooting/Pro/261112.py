# 오늘의 학습 계획
# 30분

# 5분	구간 덧셈과 대입의 차이 이해
# 8분	push() 함수 직접 설계
# 10분	range_update() 백지 구현
# 5분	반례 및 시간복잡도 검증
# 2분	최종 백지 복습

# push함수 백지 구현
N = 4
arr = [1, 2, 3, 4]

tree = [0] * (4 * N)
lazy = [None] * (4 * N)

def push(node, start, end):
    if lazy[node] is None:
        return

    if start == end:
        lazy[node] = None
        return

    mid = (start + end) // 2
    left = node * 2
    right = node * 2 + 1

    tree[left] = (mid - start + 1) * lazy[node]
    tree[right] = (end - mid) * lazy[node]

    lazy[left] = lazy[node]
    lazy[right] = lazy[node]

    lazy[node] = None

# push의 핵심 목적: 과거의 지연 대입 명령을 자식에게 먼저 반영하여, 이후 발생하는 새로운 대입 명령과의 실행 순서 보장

# 추가 질문 답변: 등호 연산이 필요합니다. 자식 노드들에 값이 더해지는 것이 아니라 대체되는 것이기 때문입니다.
# 추가 질문 답변: 5의 명령 순서가 후순위로 들어왔기 때문입니다. 이제 7이 아닌 5로 지연 전파 대기합니다.

# range_assign() 백지 구현
def range_assign(node, start, end, left, right, value):
    if start > right or end < left:
        return

    if left <= start and end <= right:
        lazy[node] = value
        tree[node] = (end - start + 1) * value
        return

    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1

    push(node, start, end)

    range_assign(left_node, start, mid, left, right, value)
    range_assign(right_node, mid + 1, end, left, right, value)

    tree[node] = tree[left_node] + tree[right_node]



