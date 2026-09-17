# SWEA 1232. 사칙연산

# 파핑파핑 풀지 말고 이거 풀란다.
# 1차 시도: FAIL(1시간)
# 9. 22. 복습 필요

# 목표: 연산 트리의 루트부터 재귀적으로 값 계산
# 상태: tree[node] = [노드 번호, 값/연산자, 왼쪽 자식, 오른쪽 자식]
# 자료구조: Tree, Dfs, 재귀, 후위 순회
# 핵심 로직: 
    # 1. 숫자 노드면 자신의 숫자를 return
    # 2. 왼쪽 subtree의 계산값 구함
    # 3. 오른쪽 subtree의 계산값 구함
    # 4. 현재 연산자로 두 값 계산해서 부모에게 return
# 종료 조건: left == 0 and right == 0인 leaf node에 도착했을 때

def cal_tree(node):
    index, main, left, right = tree[node]

    if left == 0 and right == 0:
        return main

    left_value = cal_tree(left)
    right_value = cal_tree(right)

    if main == '+':
        return left_value + right_value

    elif main == '-':
        return left_value - right_value

    elif main == '*':
        return left_value * right_value

    elif main == '/':
        return left_value / right_value

tool = ["+", "-", "*", "/"]

for tc in range(1, 11):
    N = int(input())

    tree = [None] * (N + 1)

    for i in range(1, N + 1):
        top = input().split()

        if len(top) == 2:
            index = int(top[0])
            number = int(top[1])
            tree[index] = [index, number, 0, 0]

        else:
            index = int(top[0])
            operator = top[1]
            left = int(top[2])
            right = int(top[3])

            tree[index] = [index, operator, left, right]

    answer = cal_tree(1)

    print(f'#{tc} {int(answer)}')