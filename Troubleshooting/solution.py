# 26. 10. 28
# SWEA 1248. 공통조상
# 1차 시도: PASS(35분)

"""
목표: 이진 트리가 주어진다.
    1. 임의의 두 정점에서 가장 가까운 공통 조상을 찾고
    2. 그 정점을 루트로 하는 서브 트리의 크기를 구하라.
상태: 
    1. big_papa = 공통 조상
    2. total = 트리의 크기
    3. son_node = 자식:부모 를 담는 딕셔너리
    4. parent_node = 부모:자식 을 담는 딕셔너리
자료구조: 딕셔너리
핵심로직:
    1. 간선의 부모를 찾으려면 어떻게 해야되지?
        1. 딕셔너리? key, value를 자식, 부모로 두면
        2. N1, N2에서 시작해서 value가 1이 나올때까지 부모 탐색을 반복해서 리스트에 넣기?
        3. 그 후 N1을 순서대로 순회하며 N2에 있다면 그게 최단 공통 조상?
    2. 공통 조상 루트 트리의 크기를 어떻게 구하지?
        1. 딕셔너리. key, value를 부모, 자식으로 두면
        2. big_papa에서 시작해서 자식들을 리스트에 넣고
        3. 그 리스트가 완전히 빌 때까지 자식을 탐색
        4. 자식을 탐색할때마다 total += 1
종료조건: find_size가 비었을 때, big_papa, total 출력
시간복잡도: O(E)
"""

''' 메모장

'''

T = int(input())
for tc in range(1, T + 1):
    V, E, N1, N2 = map(int, input().split())
    origin = list(map(int, input().split()))

    son_node = {}
    parent_node = {}
    for i in range(0, E * 2, 2):
        parent, son = origin[i], origin[i + 1]
        son_node[son] = parent
        parent_node.setdefault(parent, [])
        parent_node[parent].append(son)

    ancestors = set()
    now = N1

    while now:
        ancestors.add(now)
        now = son_node.get(now, 0)

    now = N2
    while now not in ancestors:
        now = son_node[now]

    big_papa = now

    stack = [big_papa]
    total = 0

    while stack:
        now = stack.pop()
        total += 1
        stack.extend(parent_node.get(now, []))

    print(f'#{tc} {big_papa} {total}')