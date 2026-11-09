# 261106 programmers 불량 사용자
# 1차 시도: FAIL(40분) / DFS 구현 실패
# 11. 12. 복습 필요

"""
목표: 유저들의 아이디와 '*'로 매핑된 불량 아이디가 주어진다. 
    1. 불량 아이디가 될 수 있는 유저들의 아이디의 경우의 수를 구하라
핵심로직:
    1. 불량 아이디 하나당 몇개의 원본 아이디가 될 수 있는지 탐색한다
        1. 길이가 같은지 확인한다.
        2. 한 자릿수씩 확인하며 일치하는지 확인한다.
        3. 일치한다면 이미 탐색한 아이디인지 확인한다
        4. current += 1을 한다 / seen 에 넣는다
        5. total에 current를 곱한다.
시간복잡도:
"""


def solution(user_id, banned_id):
    global candidate, total

    candidate = [[] for _ in range(len(banned_id))]
    for idx, bid in enumerate(banned_id):
        for uid in user_id:
            if len(bid) != len(uid):
                continue
            for i in range(len(bid)):
                if bid[i] == '*':
                    continue
                else:
                    if bid[i] != uid[i]:
                        break
            else:
                candidate[idx].append(uid)

    total = set()

    def dfs(idx, current):

        if idx == len(candidate):
            total.add(frozenset(current))
            return

        for uid in candidate[idx]:

            if uid in current:
                continue

            current.add(uid)
            dfs(idx + 1, current)
            current.remove(uid)

    dfs(0, set())

    return len(total)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

print(solution(user_id, banned_id))