'''
26. 11. 03
SWEA 1798. 범준이의 제주도 여행 계획
1차 시도: FAIL(2시간) / 전처리 실패, 구현 완성도 부족
11. 06. 복습 필요

목표: M일의 시간, N개의 방문 지점이 주어진다.
    1. 방문 지점 중 관광포인트는 중복 방문이 불가하다
    2. 관광포인트마다 소요 시간과 얻을 수 있는 만족도가 있다.
    3. 각 지점들은 서로 간에 모두 연결된 길이 있으며 이동 소요 시간이 정해져 있다. / 다른 길 우회 x
    4. 하루에 이동 + 놀이에 소요되는 시간이 9시간을 넘으면 안 된다. 그 전에 반드시 호텔에 입실해야 한다
    5. M일째 날에도 9시간 이용 가능, 그 전에 공항에 도착해야함
    6. 최대한 만족도가 높은 여행 계획을 세워라
상태:
자료구조:
핵심로직:
    1. 완전완전탐색
    2. 공항, 호텔, 관광포인트 등 어딜 가도 좋다.
    3. 하지만 놀이 시간이 9시간을 넘는다면 그 즉시 return 할 것이다
    4. 마지막으로 방문한 곳이 호텔이 아닐지라도 그 즉시 return 할 것이다.
    5. 마지막 날에는 반드시 마지막 방문한 곳이 공항이어야 할 것이다.
종료조건:
시간복잡도:
'''

def dfs(cur, day, used, score):
    global max_score, best

    if day == M:
        if used + dist[cur][airport] <= 540 and score > max_score:
            max_score = score
            best = path + [airport]
    else:
        for h in hotel:
            if used + dist[cur][h] <= 540:
                path.append(h)
                dfs(h, day + 1, 0, score)
                path.pop()

    for p in trip:
        if not visited[p]:
            t = used + dist[cur][p] + play[p]
            if t <= 540:
                visited[p] = True
                path.append(p)
                dfs(p, day, t, score + sat[p])
                path.pop()
                visited[p] = False

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    dist = [[0] * N for _ in range(N)]
    for i in range(N - 1):
        row = list(map(int, input().split()))
        for k, t in enumerate(row):
            j = i + 1 + k
            dist[i][j] = dist[j][i] = t

    play = [0] * N
    sat = [0] * N
    trip, hotel = [], []

    for idx in range(N):
        info = input().split()
        if info[0] == 'A':
            airport = idx
        elif info[0] == 'P':
            trip.append(idx)
            play[idx], sat[idx] = int(info[1]), int(info[2])
        else:
            hotel.append(idx)

    max_score = 0
    best = []
    path = []
    visited = [False] * N
    dfs(airport, 1, 0, 0)

    if max_score == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {max_score}', *[x + 1 for x in best])