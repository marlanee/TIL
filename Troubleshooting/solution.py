# 261113. 기출. 헌터
# 1차 시도: PASS

"""
목표: 상하좌우로 움직이는 헌터는 몬스터를 사냥한다.
    1. 모든 몬스터가 처리되고 모든 고객들에게 방문하면 작업이 끝난다
    2. 모든 작업을 완료할 수 있는 최소 시간을 구하라
핵심로직:
    1. 이것 역시 DFS로 풀면 간단하지 않나?
    2. 랜덤한 몬스터를 잡고 나서 (시간은 멘헤튼 거리만큼 소요됨)
    3. 다른 몬스터를 잡으러 가던가, 아니면 잡은 몬스터에 해당하는 고객을 방문하는 분기 생성
    4. 몬스터도 다 잡고, 고객도 다 방문했다면 시간 갱신.
    5. 일단 해볼까.
"""

def dfs(r, c, time, meet):
    global result
    if time >= result:
        return

    if meet == M:
        result = time
        return

    # 몬스터를 잡으러 가는 코드 작성
    for i in range(1, M + 1):
        if i not in m_check:
            m_check.add(i)
            mr, mc = monster[i]
            dfs(mr, mc, time + abs(r - mr) + abs(c - mc), meet)
            m_check.remove(i)

    # 고객을 만나러 가는 코드 작성
    for j in range(1, M + 1):
        if j in m_check and j not in p_check:
            p_check.add(j)
            pr, pc = people[j]
            dfs(pr, pc, time + abs(r - pr) + abs(c - pc), meet + 1)
            p_check.remove(j)
    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    people = {}
    monster = {}

    for r in range(N):
        for c in range(N):
            current = grid[r][c]
            if current < 0:
                people[-current] = (r, c)
            elif current > 0:
                monster[current] = (r, c)

    M = len(people)

    m_check = set()
    p_check = set()

    result = float('inf')

    dfs(0, 0, 0, 0)

    print(f'#{tc} {result}')