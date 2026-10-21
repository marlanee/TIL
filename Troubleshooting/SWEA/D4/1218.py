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

# front = ['(', '[', '{', '<']
# pair = {
#     ')': '(',
#     ']': '[',
#     '}': '{',
#     '>': '<'
# }

# for tc in range(1, 11):
#     N = int(input())
#     chaoses = input()
#     stack = []

#     result = 1

#     if N % 2 == 1:
#         print(f'#{tc} 0')
#         continue

#     for c in chaoses:
#         if c in front:
#             stack.append(c)

#         else:
#             if not stack:
#                 result = 0
#                 break

#             if stack[-1] == pair[c]:
#                 stack.pop()
#             else:
#                 result = 0
#                 break

#     if stack:
#         result = 0

#     print(f'#{tc} {result}')

# SWEA 1218. 괄호 짝짓기

# 복습: PASS(10분)

# 목표: 괄호들의 짝이 맞는지 판별하는 프로그램을 작성하라.
# 상태: stack = 들어온 괄호를 관리하는 리스트
# 자료구조: stack
# 핵심로직: 문자열을 순회하며, 왼쪽 괄호는 stack.append(), 오른쪽 괄호일 경우에는 stack.pop()과 비교.
# 종료 조건: 순회 중 짝이 맞지 않으면 0, 순회 종료 후 stack이 비어 있으면 1, 남아 있으면 0

left = ['(', '[', '{', '<']
pair = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}   # 대응 관계는 딕셔너리로 표현

for tc in range(1, 11):
    N = int(input())
    mate = input()
    stack = []
    result = 1

    for m in mate:
        if m in left:
            stack.append(m)

        else:
            if not stack:
                result = 0
                break

            target = stack.pop()

            if target != pair[m]:
                result = 0
                break

    if stack:
        result = 0

    print(f'#{tc} {result}')