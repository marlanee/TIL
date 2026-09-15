# SWEA 1218. 괄호 짝짓기

# 1차 시도: 1시간(PASS)
# 9.22. 복습 1회 필요

# 목표: 괄호의 짝이 맞는지 확인하라
# 상태: stack으로 누적 괄호 상태 확인
# 자료구조: stack
# 핵심 로직
    # 1. (, [, {, < 가 들어오면 append
    # 2. ), ], }, > 가 들어오면 stack[-1]와 일치하는지 확인
    # 3. 일치하면 stack.pop()
    # 4. 일치하지 않으면 break print(0)
# 종료 조건: 괄호 조건이 일치하지 않을 경우 0, 순회 완료 후 모든 조건이 일치할 경우 1 출력

front = ['(', '[', '{', '<']
pair = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

for tc in range(1, 11):
    N = int(input())
    chaoses = input()
    stack = []

    result = 1

    if N % 2 == 1:
        print(f'#{tc} 0')
        continue

    for c in chaoses:
        if c in front:
            stack.append(c)

        else:
            if not stack:
                result = 0
                break

            if stack[-1] == pair[c]:
                stack.pop()
            else:
                result = 0
                break

    if stack:
        result = 0

    print(f'#{tc} {result}')