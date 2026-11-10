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