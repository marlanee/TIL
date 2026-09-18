# SWEA 7465. 창용 마을 그룹의 개수

# 1차 시도: FAIL(1시간 이상)
# 9. 21 복습 필요

# 목표: 서로 연결된 사람들을 그룹라고 한다. 그룹의 개수를 구한다.
# 상태: graph = 각 사람이 알고 있는 사람 / visited = 해당 사람이 이미 그룹에 속해있는지 확인 / count = 그룹의 개수
# 자료구조: 무방향 그래프, DFS
# 핵심 로직: 
    # 1. 사람 관계를 양방향 그래프로 저장
    # 2. 1번부터 N번까지 확인
    # 3. 아직 방문하지 않은 사람이 나오면 새로운 그룹임. count += 1
    # 4. 해당 사람부터 DFS로 같은 그룹 사람을 모두 visited = True 처리
# 종료 조건: 모든 사람 확인이 끝나면 count 출력

def dfs(person):
    visited[person] = True

    for next_person in graph[person]:
        if not visited[next_person]:
            dfs(next_person)
    

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(M)]

    graph = [[] for _ in range(N + 1)]

    for person, know in numbers:
        graph[person].append(know)
        graph[know].append[person]

    visited = [False] * (N + 1)
    count = 0

    for person in range(1, N + 1):
        if visited[person] == False:
            count += 1
            dfs(person)

    print(f'#{tc} {count}')