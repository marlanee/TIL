# 261117. 합승 택시 요금
# 1차 시도: 09:11 / 09:31 힌트 1회 / 09:41 힌트 2회 / 10:00 PASS
# 학습 내용: 플로이드 워셜

"""
목표: A, B 두 사람이 택시를 같이 타려고 한다.
    1. 가는 길에 두 사람이 택시를 같이 탈 수도 있고, 각자 탈 수도 있다.
    2. 간선마다 요금이 다르며, 이동 방향에 상관없이 요금은 동일하다.
    3. n, s, a, b, fares = 지점 개수, S출발지, A도착지, B도착지, 지점 사이 택시요금
    4. A, B가 s에서 출발해서 각각의 도착 지점까지 택시를 타고 갈 때, 최저 예상 택시요금을 return하라
    5. 합승을 하지 않을 수도 있다
핵심로직: 
    1. 합승을 한다면, 출발지부터 임의의 지점까지 하게 될 것이다.
        / 따로 가다가 합승하는 경우는 어떠한 경우에도 비효율적이다
    2. 한 번 간 길을 다시 돌아오는 경우도 비효율적이다.
    ##3. 모든 정점 사이의 최단 거리를 구하는 플로이드 워셜 알고리즘을 사용해야 한다
"""

def solution(n, s, a, b, fares):
    INF = float('inf')
    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):   # 우측 하단 대각선을 모두 0으로 만든다? 왜? 
        dist[i][i] = 0  # 아니구나, 자기 자신에게 가는 비용을 0으로 만든거구나.

    for u, v, cost in fares:    # u -> v, v -> u로 가는 비용을 cost에 저장하는거구나.
        dist[u][v] = cost
        dist[v][u] = cost
    # 플로이드 워셜의 핵심: 다른 지점을 경유하는 것이 더 저렴하면 거리 배열을 갱신한다.
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    answer = INF

    for i in range(n + 1):
        together = dist[s][i]
        if together >= answer:
            continue
        A_alone = dist[i][a]
        B_alone = dist[i][b]

        answer = min(answer, together + A_alone + B_alone)
    
    return answer