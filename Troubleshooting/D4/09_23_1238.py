# SWEA 1238. Contact

# 1차 시도: PASS(45분)
# 9.23. 복습 한 번 더 하자

# 이게 뭐야ㅐ?

# 목표: 숫자들이 주어진다. 각 숫자들은 정해진 숫자들로 이어지며, 반복된다. 이 때, 마지막으로 이어진 숫자 중 가장 큰 숫자를 구하라.
# 상태: members = 각 숫자들의 관계를 관리하는 딕셔너리. stack = 순서가 한 번 지났을 때, 연락을 받은 숫자들을 보관하는 리스트
# 자료구조: 딕셔너리 + set + BFS 레벨 탐색
# 핵심 로직
    # 1. data에 담긴 숫자들을 members로 관계 분류함
    # 2. 시작하는 숫자 S부터, 이어지는 숫자가 없이 연락이 완전히 끊길 때까지 연락한다.
# 종료 조건: 연락이 완전히 끊겼을 때, max(stack)을 출력
for tc in range(1, 11):
    N, S = map(int, input().split())

    data = list(map(int, input().split()))
    members = {}

    for i in range(0, N, 2):
        member = data[i]
        members.setdefault(member, set())
        members[member].add(data[i + 1])

    stack = [S]
    called = {S}

    while len(stack) >= 1:
        new_stack = []

        for i in stack:
            if i not in members:
                continue
            for n in members[i]:
                if n not in called:
                    new_stack.append(n)
                    called.add(n)

        if not new_stack:
            result = max(stack)
            break

        stack = new_stack

    print(f'#{tc} {result}')