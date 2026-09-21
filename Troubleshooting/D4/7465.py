# SWEA 7465. 창용 마을 그룹의 개수

# 1차 시도: FAIL(1시간 이상)
# 복습: PASS(20분)
# 졸업

# 목표: 서로 연결된 사람들을 그룹라고 한다. 그룹의 개수를 구한다.
# 상태: graph = 각 사람이 알고 있는 사람 / visited = 해당 사람이 이미 그룹에 속해있는지 확인 / count = 그룹의 개수
# 자료구조: 무방향 그래프, DFS
# 핵심 로직: 
    # 1. 사람 관계를 양방향 그래프로 저장
    # 2. 1번부터 N번까지 확인
    # 3. 아직 방문하지 않은 사람이 나오면 새로운 그룹임. count += 1
    # 4. 해당 사람부터 DFS로 같은 그룹 사람을 모두 visited = True 처리
# 종료 조건: 모든 사람 확인이 끝나면 count 출력

# def dfs(person):
#     visited[person] = True

#     for next_person in graph[person]:
#         if not visited[next_person]:
#             dfs(next_person)
    

# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     numbers = [list(map(int, input().split())) for _ in range(M)]

#     graph = [[] for _ in range(N + 1)]

#     for person, know in numbers:
#         graph[person].append(know)
#         graph[know].append[person]

#     visited = [False] * (N + 1)
#     count = 0

#     for person in range(1, N + 1):
#         if visited[person] == False:
#             count += 1
#             dfs(person)

#     print(f'#{tc} {count}')

# SWEA 7465. 창용 마을 무리의 개수

# 복습: PASS(20분)

# 목표: N명의 사람에 몇 개의 무리가 존재하는지 구하기. 무리가 겹치지는 않는다.
# 상태: known = 이미 검증된 사람 리스트 / graph = 사람들의 지인 정보를 담는 그래프
# 자료구조: graph / DFS
# 핵심 로직: 순회문으로 graph를 돌며 그 사람과 관련 있는 사람은 모두 known = True 처리
# 종료 조건: 순회문이 끝났을 때 count 출력

def group(person):

    for p in graph[person]:
        if not known[p]:
            known[p] = True
            group(p)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    known = [False] * (N + 1)
    count = 0

    for _ in range(M):
        person, know = map(int, input().split())

        graph[person].append(know)
        graph[know].append(person)

    for i in range(1, N + 1):
        if not known[i]:
            known[i] = True
            group(i)
            count += 1

    print(f'#{tc} {count}')