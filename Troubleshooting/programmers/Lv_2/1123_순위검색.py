# 261116. 프로그래머스. 순위 검색
# 1차 시도: 15:18 / 28분 풀이법 탐색. AI도움 요청 / 힌트 참조하며 1시간 PASS
# 11. 23 복습 필요

"""
생김새가 딱 Numpy, pandas다. 그거 쓰면 참 편할텐데. pandas, numpy는 시간복잡도가 어떻게 될까?
목표: info에 지원자들의 지원 조건이 주어진다.
    1. query에는 개발팀의 문의사항이 주어진다.
    2. 개발팀의 문의사항에 포함되는 지원자들의 수를 순서대로 반환하라
핵심로직: 
    1. 다차원 딕셔너리는 어떠한가? total = {'cpp': {'backend':, 'frontend': }, 'java':, 'python':}
    2. 반복문을 돌며 앞자리가 '-'면 모든 주제 선택. 이외에는 주어진 주제만 선택. 수를 반환하는거다
    3. 일단 info를 반복문으로 돌며 다차원 딕셔너리를 만들어야겠지.
    4. 귀찮다. 리스트로 만들자
"""

from bisect import bisect_left

def solution(info, query):
    total = {}
    for key in info:
        key_list = tuple(key.split())
        target = list(key_list)

        def dfs(idx):
            if idx == 4:
                total.setdefault(tuple(target[:4]), []).append(int(target[-1]))
                return

            dfs(idx + 1)

            p = target[idx]
            target[idx] = '-'
            dfs(idx + 1)
            target[idx] = p

        dfs(0)

    for scores in total.values():
        scores.sort()

    answer = []

    for q in query:
        parts = q.replace('and', ' ').split()
        key, score = tuple(parts[:4]), int(parts[-1])

        scores = total.get(key, [])
        start = bisect_left(scores, score)

        answer.append(len(scores) - start)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))