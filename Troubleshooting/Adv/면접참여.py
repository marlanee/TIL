# 261112. 기출. 면접 참여
# 1차 시도: 30분 PASS

"""
목표: N개의 문제, M개의 맞힌 문제, K의 카운터가 주어진다.
    1. 아래 조건이 주어질 때, 이론상 가능한 최소 점수를 구하라
        1. 카운터의 초기값은 0
        2. 문제를 틀릴 경우 카운터는 0으로 초기화
        3. 문제를 맞추면 1점 획득 후 카운터 1 증가
        4. 카운터가 K에 도달시 카운터 0 초기화, 총점 2배
핵심로직:
    1. M이 (N // 2) + 1 이하이면 M이 정답.
    2. 그 이외에는 어떤 방법을 쓸까?
        1. M을 하나씩 소모하는 방법
            0. [0] * N 리스트를 만든다.
            1. N을 2칸씩 건너며 1로 만든다.
            2. 인덱스 1부터 시작해서 4칸씩 건너뛰며 1로 바꾼다.
            3. 이 방법은 폐기한다. 그 이후 계산이 힘들다
        2. DFS를 사용하는 방법
            1. count가 M이 될 때까지 idx를 하나씩 겹치지 않게 1로 바꾼다
            2. 점수를 계산하는 함수로 계산 후 갱신한다.
            3. 가능은 하나 시간복잡도가 걱정이다. O(N!)?
            4. 미리 0을 흩뿌려놓고 시간복잡도를 줄일 수 있다.
            5. 아무래도 혁신적으로 줄긴 한다.
"""

def dfs(idx, count):
    global total

    if count == M:
        # 계산하는 코드 작성
        current = 0
        counter = 0
        for i in range(N):
            if arr[i] == 1:
                current += 1
                counter += 1
                if counter == K:
                    counter = 0
                    current *= 2
            else:
                counter = 0

        total = min(total, current)
        return  

    for i in range(idx, N):
        arr[i] = 1
        dfs(i + 1, count + 1)
        arr[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [0] * N

    if M <= (N // 2 + 1):
        print(f'#{tc} {M}')
        continue

    total = float('inf')

    dfs(0, 0)

    print(f'#{tc} {total}')