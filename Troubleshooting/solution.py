# 261111. SWEA 1259. 
# 1차 시도: 17:34

"""
목표: N개의 금속 막대가 주어진다.
    1. 금속 막대의 끝부분이 다른 금속 막대의 앞부분과 일치해야 연결된다.
    2. 어떤 순서로 연결해야 가장 많은 연결하는지를 찾는 프로그램을 작성하라
    3. 가장 많이 연결하기 위한 금속 막대의 앞부분과 끝부분을 순서대로 출력하라
    4. 개수가 아닌 순서대로 출력하라는 것은, 모든 나사가 연결되는 케이스밖에 없다는 것인가?
핵심로직:
    1. DFS로 모든 경우의 수를 찾고 연결되지 않으면 return?
    2. 연결되면 리스트 갱신 후 return?
    3. 더 좋은 방법이 있나? 일단 해보자
"""

def dfs(count, current):
    global result

    if result:
        return

    if count == N:
        # 연결되었는지 확인하는 코드 작성
        
        for x in range(0, N - 1):
            if current[x][1] != current[x + 1][0]:
                return
        result = current.copy()
        return


    for j in range(N):
        if not visited[j]:
            current.append(NASA[j])
            visited[j] = True
            dfs(count + 1, current)
            current.pop()
            visited[j] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    origin = list(map(int, input().split()))
    NASA = []
    for i in range(0, 2 * N, 2):
        NASA.append(origin[i:i + 2])

    result = []
    visited = [False] * N

    dfs(0, [])

    print(f'#{tc}', end=' ')
    for nasa in result:
        print(nasa[0], nasa[1], end=' ')

    print()


    