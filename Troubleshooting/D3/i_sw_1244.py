# 2026-08-19. 1차 시도: FAIL 줜나 어렵다
# 2026-08-20. 2차 시도: PASS(40분)

# T = int(input())
# for i in range(1, T + 1):
#     N, L = map(input().split())
#     n = list(map(int, N))
#     l = int(L)
# 각 자릿수의 숫자를 교체해 최댓값을 만드는 코드
# 단, 제시된 교체 숫자만큼은 반드시 교체해야함
# 이미 최댓값을 만들어도 교체해야하는 경우도 있을 수 있다는 것임
# 어떤 알고리즘을 구현해야할까?
# 먼저, 어떤 값이 최댓값인지 생각해보자. 
# 주어진 숫자들을 sorted(reverse=True) 한 것이 최댓값이다.
# 우선, 가장 큰 첫 번째 자릿수를 체크하고 교체해야 할 것이다.
# 이미 최댓값을 완성했을 때, 남은 교체횟수가 짝수이면 그대로 최댓값을 출력한다
# 이미 최댓값을 완성했을 때, 남은 교체횟수가 홀수이면 가장 우측의 낮은 숫자들끼리 교체한다.
# 최댓값을 순서대로 만들기 위한 로직은?
# 재귀함수를 써야하나? 가장 우측에 있는 max값을 제일 왼쪽으로 옮기는 함수
# def dfs(index, max_num):
#     ri = n.rindex(max(n[index:]))
#     rm = n[ri]

#     if n[index] != rm:
#         n[ri] = n[index]
#         n[index] = rm

#     if index > 2:

# 1차 피드백 후 작성
# 겉보기에 규칙이 쉬워 보여도, 예외가 존재할 수 있다면 완전 탐색을 고려해야 한다.
# dfs(재귀 + 백트래킹)
# def dfs(depth):
#     global max_result

#     state = (''.join(numbers), depth)   # N_str이 join 메서드 사용 후 결과와 같지 않나? 그리고 state라는 변수에 세트 형태로 문자열과 정수형을 같이 넣은건가?
#     if state in visited:
#         return
#     visited.add(state)

#     if depth == L:
#         max_result = max(max_result, int(''.join(numbers)))
#         return

#     n_len = len(numbers)
#     for i in range(n_len - 1):   # 마지막 숫자 빼고 전부
#         for j in range(i + 1, n_len):   # 첫 숫자 빼고 전부
#             numbers[i], numbers[j] = numbers[j], numbers[i]   # 한 줄에 두 요소를 바꿔치기했네. 이런 방법도 있구나.
#             dfs(depth + 1)
#             numbers[i], numbers[j] = numbers[j], numbers[i]

# T = int(input())
# for tc in range(1, T + 1):
#     N_str, L_str = input().split()   # map 없이도 각 변수에 선언할 수 있다.
#     numbers = list(N_str)
#     L = int(L_str)

#     max_result = 0
#     visited = set()   # 그냥 ()로 쓰면 튜플이 되나? 빈 세트 선언은 set()?

#     dfs(0)
#     print(f'#{tc} {max_result}')

# BFS(반복문 + set)

T = int(input())
for tc in range(1, T + 1):
    n_str, t_str = input().split()
    t = int(t_str)

    # 완전탐색 or BFS
    # 발생할 수 있는 모든 케이스를 구한 뒤, 최댓값을 출력한다
    current_num  = {n_str}

    # 탐색을 할 때에는 정수형으로 형변환 할 필요는 없어 보인다.
    ln = len(n_str)

    for i in range(t):
        find_set = set()
        for z in current_num:
            zl = list(z)
            for x in range(ln -1):
                for y in range(x + 1, ln):   # x와 y가 같으면 안된다. 1 대신 x + 1
                    zl[x], zl[y] = zl[y], zl[x]
                    find_set.add(''.join(zl))
                    zl[y], zl[x] = zl[x], zl[y]

        current_num = find_set

    print(f'#{tc} {max(map(int, current_num))}')