# 261112. SWEA 5521. 상원이의 생일파티
# 1차 시도: 17:02

"""
목표: N명의 학생이 있고, M개의 친한 친구 관계가 있다
    1. 상원이의 친한 친구와, 친한 친구의 친구만 생일 파티에 초대하려 한다
    2. 몇 명의 친구들에게 초대장을 주어야 하는지 구하라
    777. 상식적으로 친한 친구의 친한 친구의 친한 친구는 안 부르겠지.
핵심로직:
    1. 친한 친구의 관계를 담은 딕셔너리를 구상한다
    2. queue를 만들어서 친한 친구로 선정된 친구를 담는다.
    3. q를 반복하며 또 담는다.
    4. q가 비면 종료한다.
"""

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    friends = {}

    for _ in range(M):
        a, b = map(int, input().split())
        friends.setdefault(a, set()).add(b) # 
        friends.setdefault(b, set()).add(a) #

    q = friends.get(1, set())   #

    total = set(q) # 세트는 반복이 가능하다!!!!!!

    for i in q:
        total.update(friends[i])    # update가 뭐냐?

    total.discard(1)    # 이건 또 뭐야?

    print(f'#{tc} {len(total)}')