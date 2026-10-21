# SWEA 9367. 점점 커지는 당근의 개수

# 1차 시도: PASS(15분)

# 목표: 숫자들이 주어질 때, 오름차순 부분집합의 길이를 구하시오.
# 상태: stack = 오름차순일 경우 담아놓는 임시 숫자열
# 자료구조: stack
# 핵심 로직
    # 1. 숫자들을 순회함
    # 2. stack이 비었을 경우 stack.append(n) / continue
    # 3. stack[-1] < n: stack.append(n)
    # 4. else: total = max(total, len(stack))
    # 5. stack = []
# 종료 조건: 순회가 종료되었을 때, total = max(total, len(stack)) 갱신 후 total 출력

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrots = list(map(int, input().split()))
    stack = []
    total = 0

    for c in carrots:
        if not stack:
            stack.append(c)
            continue

        if stack[-1] < c:
            stack.append(c)
        else:
            total = max(total, len(stack))
            stack = [c]

    total = max(total, len(stack))

    print(f'#{tc} {total}')