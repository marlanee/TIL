261113. 시험. 1. 편지
1차 시도: 30분
"""
목표: N명의 사람이 있다.

1. 1번 사람이 자신의 친구들에게 모두 편지를 1통씩 보낸다
2. 2번부터 N - 1번의 사람들은 처음 편지를 받았을 때만, 자신의 친구들에게 편지를 1통씩 보낸다
3. N번 사람은 편지를 받기만 한다. N번 사람이 몇 개의 편지를 받는지 계산하라
자료구조:

1. 편지를 받았는지 확인하는 배열이 필요하다. / 또한 이것을 각 사람이 편지를 몇 번 받았는지 사용할 것이다
2. queue를 쓰면 될 것 같다. while q: 처음 편지를 받는 놈만 q에 넣는거지.
3. N - 1 인덱스를 가진 사람의 편지 받은 수를 구하면 된다
4. 그 전에, 저 grid를 전처리 해야된다.
"""

from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    friends = {}

for r in range(N):
    for c in range(N):
        if r == c:
            continue
        if grid[r][c] == 1:
            friends.setdefault(r, set()).add(c)
            friends.setdefault(c, set()).add(r)

letter = [0] * N
letter[0] = float('inf')

q = deque([0])

while q:
    next_friends = q.popleft()
    nxt = friends.get(next_friends, [])  # 1번 친구가 친구가 없으면 keyError. / 히든테케 딱

    for i in nxt:
        if letter[i] == 0 and i != N - 1:
            letter[i] += 1
            q.append(i)
            continue
        letter[i] += 1

print(f'#{tc} {letter[-1]}')