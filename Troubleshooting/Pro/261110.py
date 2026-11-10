# 261110. Lazy Propagation
'''
30분 커리큘럼
0~5분

기존 세그먼트 트리의 한계

구간 갱신의 시간복잡도 분석


5~12분

Lazy Propagation 원리

갱신을 미뤄도 정답이 유지되는 이유 설명


12~25분

독립 구현

range_update()와 range_query() 구현


25~30분

검증 및 코드 리뷰

반례, 복잡도, B형 실전 적용
'''

def push(node, start, end):
    if lazy[node] == 0 or start == end:
        return

    mid = (start + end) // 2
    left = node * 2
    right = node * 2 + 1

    # 자식 노드의 구간 합 갱신
    tree[left] += (mid - start + 1) * lazy[node]
    tree[right] += (end - mid) * lazy[node]

    # 자식에게 지연 갱신 정보 전달
    lazy[left] += lazy[node]
    lazy[right] += lazy[node]

    # 부모의 지연 갱신 정보 초기화
    lazy[node] = 0

def range_update(node, start, end, left, right, value):
    # 1. 겹치지 않는 경우
    if start > right or end < left:
        return

    # 2. 완전히 포함되는 경우
    if left <= start and end <= right:
        tree[node] += (end - start + 1) * value
        lazy[node] += value
        return
    # 3. 일부 겹치는 경우
    #    기존 지연 갱신 전파
    push(node, start, end)
    #    좌우 자식 재귀 갱신
    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1
    range_update(left_node, start, mid, left, right, value)
    range_update(right_node, mid + 1, end, left, right, value)
    #    부모 구간 합 재계산
    tree[node] = tree[left_node] + tree[right_node]

def range_query(node, start, end, left, right):
    # 1. 겹치지 않는 경우
    if start > right or end < left:
        return 0
    # 2. 완전히 포함되는 경우
    if left <= start and end <= right:
        return tree[node]
    # 3. 일부 겹치는 경우
    # 기존 lazy 전파
    push(node, start, end)
    # 왼쪽, 오른쪽 구간 합 조회
    mid = (start + end) // 2
    left_node = node * 2
    right_node = node * 2 + 1
    left_result = range_query(left_node, start, mid, left, right)
    right_result = range_query(right_node, mid + 1, end, left, right)
    # 두 결과의 합 반환
    return left_result + right_result