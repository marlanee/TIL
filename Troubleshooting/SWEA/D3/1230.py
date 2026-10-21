# 암호문3 1차 시도: PASS(40분)

# 1. 목표: 명령어로 암호문을 수정하고, password[:10] 까지의 암호문을 출력
# 2. 상태: 암호문은 password 리스트로, 명령어도 order 리스트로 관리하자.
# 3. 자료구조: password.insert(a, *str), del password[4:6], append(*str)
# 4. 핵심 로직: while i < M:, i 가 암호문마다 다르게 누적합 연산
# 5. 종료 조건: while i >= M:

for tc in range(1, 11):
    N = int(input())
    password = list(input().split())
    M = int(input())
    order = list(input().split())

    i = 0

    while i < len(order):
        if order[i] == 'I':
            idx = int(order[i + 1])
            add_num = int(order[i + 2])
            password[idx:idx] = order[i + 3:i + 3 + add_num]    # 아니 어떻게? 슬라이싱의 신기한 삽입 방법이다.
            i += (3 + add_num)
        elif order[i] == 'D':
            idx = int(order[i + 1])
            count = int(order[i + 2])
            del password[idx:idx + count]
            i += 3
        elif order[i] == 'A':
            append_num = int(order[i + 1])
            password.extend(order[i + 2:i + 2 + append_num])
            i += (2 + append_num)

    print(f'#{tc} {" ".join(password[:10])}')