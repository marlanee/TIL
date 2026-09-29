# SWEA 3289. 서로소 집합.
# GPT가 추천해준 문제.

# 1차 시도: PASS(15분)
# 원트 졸업

# 목표: 두 원소가 같은 집합에 속해 있는지 아닌지를 판별하라
# 상태: Union: 대표자를 영입하는 함수, Find = 대표자를 반환하는 함수
# 자료구조: Union-Find
# 핵심로직: 리스트를 순회하며 Union-Find 로직 실행
# 종료 조건: 순회가 종료되었을 때 result 출력

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):

    au = find(a)
    bu = find(b)

    parents[bu] = au
    return

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    parents = [i for i in range(N + 1)]
    result = ''

    for _ in range(M):
        tool, a, b = map(int, input().split())
        
        if tool == 0:
            union(a, b)
        else:
            if find(a) != find(b):
                result += '0'
            else:
                result += '1'

    print(f'#{tc} {result}')