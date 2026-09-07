# 초심자의 회문 검사. 1차 시도: PASS(5분)

# 1. 목표: 주어진 단어가 회문인지 검사
# 2. 상태: word = input()
# 3. 자료구조: 리스트 슬라이싱
# 4. 핵심 로직: word == word[::-1]
# 5. 종료 조건: print()

T = int(input())
for tc in range(1, T + 1):
    word = input().strip()
    if word == word[::-1]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')