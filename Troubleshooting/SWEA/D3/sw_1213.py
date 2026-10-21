# 2026-08-24. 1차 시도: PASS(12분)
# 영어 문장에서 특정 문자의 개수를 찾는 프로그램
# 찾아야 할 문자열의 길이만큼 처음부터 끝까지 탐색하면 되는거 아닌가?

for _ in range(1, 11):
    tc = int(input())
    find_str = input().strip()
    total_str = input().strip()

    fl = len(find_str)
    tl = len(total_str)

    count = 0
    for i in range(tl - fl + 1):
        if total_str[i:i + fl] == find_str:
            count += 1

    print(f'#{tc} {count}')
    print(total_str.count(find_str))   #count로도 두 글자 이상 문자 탐색 가능하다.
# 다 풀었다. 허접한 문제네.