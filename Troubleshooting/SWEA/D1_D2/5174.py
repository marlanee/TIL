# SWEA 5174. subtree

# 목표: Tree 구조에서 N으로 시작하는 노드의 길이를 구해라.
# 상태: node = 노드의 관계를 나타내는 딕셔너리. 
# 자료구조: dictionary
# 핵심 로직: 노드를 한 칸씩 내려가며 count를 하나씩 더함
# 종료 조건: current_node가 완전히 비었을 때, count를 출력

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())

    node = {}
    count = 1

    numbers = list(map(int, input().split()))

    for i in range(0, E * 2, 2):
        if numbers[i + 1] == 0:
            continue
        node.setdefault(numbers[i], [])
        node[numbers[i]].append(numbers[i + 1])

    current_node = {N}

    while current_node:
        next_node = set()

        for cn in current_node:
            if cn not in node:
                continue
            for n in node[cn]:
                next_node.add(n)

        current_node = next_node
        count += len(next_node)

    print(f'#{tc} {count}')