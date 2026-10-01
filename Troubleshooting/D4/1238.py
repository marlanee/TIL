# SWEA 1238. Contact

# 1차 시도: PASS(45분)
# 9.23. 복습 한 번 더 하자
# 복습: FAIL
# 10.2. 복습 필요
# 복습 2회차: PASS(24분)
# 졸업

# 이게 뭐야ㅐ?

# 목표: 숫자들이 주어진다. 각 숫자들은 정해진 숫자들로 이어지며, 반복된다. 이 때, 마지막으로 이어진 숫자 중 가장 큰 숫자를 구하라.
# 상태: members = 각 숫자들의 관계를 관리하는 딕셔너리. stack = 순서가 한 번 지났을 때, 연락을 받은 숫자들을 보관하는 리스트
# 자료구조: 딕셔너리 + set + BFS 레벨 탐색
# 핵심 로직
    # 1. data에 담긴 숫자들을 members로 관계 분류함
    # 2. 시작하는 숫자 S부터, 이어지는 숫자가 없이 연락이 완전히 끊길 때까지 연락한다.
# 종료 조건: 연락이 완전히 끊겼을 때, max(stack)을 출력
# for tc in range(1, 11):
#     N, S = map(int, input().split())

#     data = list(map(int, input().split()))
#     members = {}

#     for i in range(0, N, 2):
#         member = data[i]
#         members.setdefault(member, set())
#         members[member].add(data[i + 1])

#     stack = [S]
#     called = {S}

#     while len(stack) >= 1:
#         new_stack = []

#         for i in stack:
#             if i not in members:
#                 continue
#             for n in members[i]:
#                 if n not in called:
#                     new_stack.append(n)
#                     called.add(n)

#         if not new_stack:
#             result = max(stack)
#             break

#         stack = new_stack

#     print(f'#{tc} {result}')

    # SWEA 1238. Contact

# 복습: FAIL
# 10.2. 복습 필요

# 목표: graph 구조에서, visited를 활용해 tree 처럼 사용해, 너비 탐색을 하며 가장 마지막에 호출되는 정점 중 큰 숫자를 구하라
# 상태: graph = 정점의 정보를 담는 리스트. visited = 중복 방문을 막는 리스트. q = 임시 queue
# 자료구조: tree, BFS, deque
# 핵심 로직: graph로 tree 구조로 전처리, BFS로 순회, deque 이용
# 종료 조건: 마지막 숫자들이 호출되었을 떄, max 값 출력
# from collections import deque

# def bfs(node):
#     q = deque([node])
#     visited[node] = True

#     last_level = []

#     while q:
#         last_level = list(q)

#         for _ in range(len(q)):
#             current = q.popleft()

#             for next_node in graph[current]:
#                 if not visited[next_node]:
#                     visited[next_node] = True
#                     q.append(next_node)

#     return max(last_level)

# for tc in range(1, 11):
#     N, lemon = map(int, input().split())

#     graph = [[] for _ in range(101)]
#     visited = [False] * 101

#     origin = list(map(int, input().split()))

#     for i in range(0, N, 2):
#         start, to = origin[i], origin[i + 1]
#         graph[start].append(to)

#     result = bfs(lemon)

#     print(f'#{tc} {result}')

# SWEA 1238. Contact

# 복습 2회차: PASS(24분)

"""
목표: 
    1. 정점들을 가진 graph가 주어진다. 각 정점에서 간선을 통해 일정한 간격으로 한 칸씩 이동한다
    2. 이미 등장한 정점들은 다시 방문하지 않는다.
    3. 이 때, 마지막 순서로 등장하는 정점들 중 최대값을 구하라
상태: graph = 정점들의 관계를 나타내는 리스트, visited = 등장 여부 확인 리스트
자료구조: graph, visited, BFS, deque
핵심 로직: 
    1. graph로 입력받은 데이터 전처리
    2. BFS로 한 너비씩 탐색
    3. next_queue가 비었을 때, max(queue) 출력 후 종료
종료 조건: queue가 비었을 때
시간복잡도: O(V + E)
"""
from collections import deque

for tc in range(1, 11):
    N, S = map(int, input().split())
    origin = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    visited = [False] * (101)

    for i in range(0, N, 2):
        graph[origin[i]].append(origin[i + 1])

    q = deque([S])
    visited[S] = True

    while q:
        next_q = deque()
        result = max(q)

        for _ in range(len(q)):
            node = q.popleft()

            for next_node in graph[node]:   # node가 빈 리스트 일 경우 continue 하는 코드가 필요한가?
                if not visited[next_node]:
                    next_q.append(next_node)
                    visited[next_node] = True

        q = next_q

    print(f'#{tc} {result}')