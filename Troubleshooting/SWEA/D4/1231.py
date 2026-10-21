# SWEA 1231. 중위순회
# 복습: PASS(20분)
# 졸업

# 1차 시도: FAIL(1시간)
# 9. 21. 복습 필요
# 다음에 풀 때는 트리 순회 공식으로 해보자. gpt에게 힌트 구하기.

# 목표: 중위 순회. in-order 방식. 왼쪽 서브트리 0> 현재 노드 -> 오른쪽 서브트리
# 상태: tree = 트리의 장식물을 관리하는 리스트
# 자료구조: dfs / tree
# 핵심로직: 왼쪽이 없으면 내꺼 출력 후 오른쪽으로 넘어감
# 종료 조건: dfs 재귀 호출이 끝날 때

# def inorder(node):
#     alphabet, left, right = tree[node]

#     if left != 0:
#         inorder(left)

#     print(alphabet, end = '')

#     if right != 0:
#         inorder(right)

# for tc in range(1, 11):
#     N = int(input())
    
#     tree = [None] * (N + 1)

#     for _ in range(N):
#         top = (input().split())

#         if len(top) == 4:
#             number, alphabet, left, right = top

#         elif len(top) == 3:
#             number, alphabet, left = top
#             right = 0

#         else:
#             number, alphabet = top
#             right, left = 0, 0

#         tree[int(number)] = [alphabet, int(left), int(right)]

#     print(f'#{tc}', end = ' ')

#     inorder(1)

#     print()

# SWEA 1231. 중위순회

# 복습: PASS(20분)
# 졸업

# 목표: 중위 순회. in-order 방식. 왼쪽 -> main -> 오른쪽 순서로 우선 출력하는 트리 출력 프로그램 만들기
# 상태: tree = 트리의 정보를 담는 리스트.
# 자료구조: tree, DFS
# 핵심 로직: 왼쪽 -> main -> 오른쪽 순서로 완전 탐색 / 왼쪽이 0이 아니면 왼쪽 탐색 -> main 출력 -> 오른쪽 0 아니면 탐색
# 종료 조건: 호출이 더 이상 발생하지 않을 때

def inorder(node):
    alphabet, left, right = tree[node]

    if left:
        inorder(left)

    print(alphabet, end = '')

    if right:
        inorder(right)

    
for tc in range(1, 11):
    N = int(input())

    tree = [None] * (N + 1)

    for _ in range(N):
        data = input().split()

        node = int(data[0])
        alphabet = data[1]

        left = int(data[2]) if len(data) >= 3 else 0
        right = int(data[3]) if len(data) >= 4 else 0

        tree[node] = [alphabet, left, right]

    print(f'#{tc}', end = ' ')

    inorder(1)

    print()