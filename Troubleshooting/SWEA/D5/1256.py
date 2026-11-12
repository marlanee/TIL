# 261112. SWEA 1256. K번째 접미어
# 1차 시도: PASS(10분)

"""
목표: 길이가 n인 문자열이 주어진다.
    1. 이 문자열로 n개의 접미어를 만들 수 있다.
    2. 사전적으로 정렬했을 때 K번째 접미어를 출력하라
핵심로직:
    1. 슬라이싱으로 접미어 n개 만들어서 한 리스트에 넣고 sort로 정렬해서 K - 1번째 문자 출력
"""

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    word = input().strip()
    total = []

    for i in range(len(word)):
        total.append(word[i:])

    total.sort()

    print(f'#{tc} {total[K-1]}')