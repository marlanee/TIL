"""
26.11.04
SWEA 10507. 영어 공부
1차 시도: 30분 Runtime Error / 
보충 학습 내용: 투 포인터 알고리즘
11. 09. 복습 필요

목표: n개의 숫자가 주어진다. 
    1. p개 만큼 숫자를 추가할 수 있다
    2. 최대한 큰 연결된 숫자를 만들어야 한다
    3. 이론상 가능한 가장 큰 연결된 숫자열의 길이를 구하시오
상태:
자료구조:
핵심로직:
    1. 숫자의 삽입은 반드시 존재하는 n개의 숫자 앞 또는 뒤에 붙여야 한다
    2. 앞에 붙일 때는 해당하는 숫자로부터 내림차순으로 p개를 붙이며
    3. 뒤에 붙일 때에는 해당하는 숫자로부터 오름차순으로 p개를 붙인다.
    4. 앞, 뒤로 붙이던 숫자가, 이미 n개의 숫자에 포함되어 있다면 한 칸 더 가서 붙인다. 이 과정은 반복된다.
    5. 붙이는 과정이 완료되면 연속된 숫자의 수를 갱신한다. 
    6. 생각해보니 굳이 오름차순이 필요할까 싶다. 내림차순이 모든 역할을 다 한다.
종료조건:
시간복잡도:O(N^2)
"""

T = int(input())
for tc in range(1, T + 1):
    n, p = map(int, input().split())
    studies = list(map(int, input().split()))

    left = 0
    result = 0

    for right in range(len(studies)):   # 끝 날짜 조정
        while studies[right] - studies[left] - (right - left) > p:  # 전체 날에서 공부한 날을 뺀 날이 p보다 많으면
            left += 1   # 시작 날짜 조정

        length = (right - left + 1) + p # 공부한 날짜 + p

        result = max(result, length)

    print(f'#{tc} {result}')