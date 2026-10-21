# 문자열 비교. 1차 시도: PASS(5분)

# 1. 목표: 문자열 str2 안에 str1이 있는지 확인, 있으면 1 아니면 0
# 2. 상태: 둘 다 문자열로 존재
# 3. 자료구조: 있는지 확인하는 in 코드 사용
# 4. 핵심 로직: if str1 in str2:
# 5. 종료 조건: in 함수 사용 후

T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')