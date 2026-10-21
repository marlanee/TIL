# SWEA 1232. 사칙연산

# 파핑파핑 풀지 말고 이거 풀란다.
# 1차 시도: FAIL(1시간)
# 복습: PASS(18분)
# 9. 29. 복습 필요
# 복습 2회차: PASS(자소서 쓰며 45분)
# 졸업

# 목표: 연산 트리의 루트부터 재귀적으로 값 계산
# 상태: tree[node] = [노드 번호, 값/연산자, 왼쪽 자식, 오른쪽 자식]
# 자료구조: Tree, Dfs, 재귀, 후위 순회
# 핵심 로직: 
    # 1. 숫자 노드면 자신의 숫자를 return
    # 2. 왼쪽 subtree의 계산값 구함
    # 3. 오른쪽 subtree의 계산값 구함
    # 4. 현재 연산자로 두 값 계산해서 부모에게 return
# 종료 조건: left == 0 and right == 0인 leaf node에 도착했을 때

# def cal_tree(node):
#     index, main, left, right = tree[node]

#     if left == 0 and right == 0:
#         return main

#     left_value = cal_tree(left)
#     right_value = cal_tree(right)

#     if main == '+':
#         return left_value + right_value

#     elif main == '-':
#         return left_value - right_value

#     elif main == '*':
#         return left_value * right_value

#     elif main == '/':
#         return left_value / right_value

# tool = ["+", "-", "*", "/"]

# for tc in range(1, 11):
#     N = int(input())

#     tree = [None] * (N + 1)

#     for i in range(1, N + 1):
#         top = input().split()

#         if len(top) == 2:
#             index = int(top[0])
#             number = int(top[1])
#             tree[index] = [index, number, 0, 0]

#         else:
#             index = int(top[0])
#             operator = top[1]
#             left = int(top[2])
#             right = int(top[3])

#             tree[index] = [index, operator, left, right]

#     answer = cal_tree(1)

#     print(f'#{tc} {int(answer)}')

# SWEA 1232. 사칙연산

# 복습: PASS(18분)
# 9. 29. 복습 필요

# 목표: 후위 순회. 왼쪽, 오른쪽 결과를 구하고 중앙 연산자로 계산 처리할 것
# 상태: Tree = 정점의 정보를 담는 트리.
# 자료구조: Tree, DFS
# 핵심 로직: 좌, 우 결과값을 구해서 중앙 연산자로 계산하기
# 종료 조건: 리프 노드에 도달하면 숫자 값을 반환. 반환된 좌/우 결과를 현재 연산자로 계산하며 재귀를 복귀

# def cal(node):
#     main, left, right = tree[node]

#     if left == 0:
#         return main

#     left_result = cal(left)
#     right_result = cal(right)

#     if main == '+':
#         return left_result + right_result
#     elif main == '-':
#         return left_result - right_result
#     elif main == '*':
#         return left_result * right_result
#     else:
#         return left_result / right_result

# for tc in range(1, 11):
#     N = int(input())
#     tree = [None] * (N + 1)

#     for i in range(1, N + 1):
#         node = input().split()
#         num = int(node[0])

#         if len(node) == 2:
#             main, left, right = int(node[1]), 0, 0
#         else:
#             main, left, right = node[1], int(node[2]), int(node[3])

#         tree[num] = [main, left, right]

#     result = int(cal(1))

#     print(f'#{tc} {result}')

# SWEA 1232. 사칙연산

# 복습 2회차: PASS(자소서 쓰며 45분)

# 목표: 이진 트리를 후위 순회하여 사칙연산을 한 결과를 반환하는 코드를 작성하라
# 상태: left = 왼쪽 노드의 반환값, right = 오른쪽 노드의 반환값, tree = 정점들의 정보를 담는 트리
# 자료구조: tree, DFS
# 핵심 로직: 
    # 1. 리프 노드라면 숫자를 반환한다.
    # 2. 왼쪽 서브트리의 계산 결과를 얻는다
    # 3. 오른쪽 서브트리의 계산 결과를 얻는다
    # 4. 현재 노드의 연산자로 두 결과를 계산해 부모에게 반환한다.
# 종료 조건: 현재 노드가 리프 노드라면 저장된 숫자를 반환

def dfs(node):

    _, main, left_node, right_node = tree[node]

    if left_node == 0:
        return int(main)

    left = dfs(int(left_node))
    right = dfs(int(right_node))

    if main == '+':
        return left + right
    elif main == '-':
        return left - right
    elif main == '*':
        return left * right
    else:
        return left / right

for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for i in range(1, N + 1):
        node = input().split()
        if len(node) == 2:
            node.append(0)
            node.append(0)

        tree[i] = node

    result = int(dfs(1))

    print(f'#{tc} {result}')