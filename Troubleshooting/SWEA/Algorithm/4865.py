# 글자수. 1차 시도: 16:33

# 1. 목표: 문자열 str2에 들어있는 str1의 요소 중 최댓값을 구하기.
# 2. 상태: str2는 문자열 그대로, str1은 중복 요소를 빼기 위해 set로 설정
# 3. 자료구조: str1 = set(input())
# 4. 핵심 로직: for s in str1:, str2.count(s), if str2.count(s) > max_count, 갱신
# 5. 종료 조건: str1을 끝까지 순회하면 종료

T = int(input())

for tc in range(1, T + 1):
    str1 = set(input())
    str2 = input().strip()
    max_count = 0

    for s in str1:
        cn = str2.count(s)
        if cn > max_count:
            max_count = cn

    print(f'#{tc} {max_count}')