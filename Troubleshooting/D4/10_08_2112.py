# SWEA 2112. 보호 필름
# 1차 시도: Reutime Error(1시간) 
# 10. 08. 복습 필요 / 최적화 필요

"""
목표: 0 또는 1로 채워진 D x W 2차원 행렬이 주어진다.
약품을 투입하면 열 하나를 A 또는 B로 모두 채워지도록 바꿀 수 있다.
최소로 약품을 사용하며 모든 행이 같은 문자가 K번 반복되도록 만들어야 한다.
이 때 약품 투약 횟수를 구하시오.
상태: 
자료구조:
핵심 로직:
1. 전체 열 각각에 K만큼 연속된 부분이 있는지 확인. 있으면 0 출력 후 continue
2. dfs로 0열부터 D - 1 열까지, 0으로 바꾸거나, 1로 바꾸거나, 안 바꾸는 DFS 실행
3. 만약 연속 조건이 만족되면 최소 투약횟수 갱신 return / row == D일 경우 return
종료 조건:
시간 복잡도
"""

def dfs(row, count):
    global result

    if count >= result:
        return

    check_grid = 0

    for c in range(W):
        streak = 1
        previous = grid[0][c]
        for r in range(1, D):
            current = grid[r][c]
            if previous == current:
                streak += 1
            else:
                streak = 1

            previous = current

            if streak >= K:
                check_grid += 1
                break

        if streak < K:
            break


    if check_grid == W:
        result = min(result, count)
        return

    if row == D:
        return

    dfs(row + 1, count)

    test_1 = grid[row]
    grid[row] = [0] * W
    dfs(row + 1, count + 1)
    grid[row] = test_1

    test_2 = grid[row]
    grid[row] = [1] * W
    dfs(row + 1, count + 1)
    grid[row] = test_2

T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(D)]

    result = K
    dfs(0, 0)

    print(f'#{tc} {result}')


# 아래는 GPT의 최적 코드다.

# def check():
#     if K == 1:
#         return True

#     for c in range(W):
#         streak = 1
#         previous = grid[0][c]

#         for r in range(1, D):
#             current = grid[r][c]

#             if current == previous:
#                 streak += 1
#             else:
#                 streak = 1

#             previous = current

#             if streak >= K:
#                 break

#         if streak < K:
#             return False

#     return True

# def dfs(row, count):
#     global result

#     if count >= result:
#         return

#     if row == D:
#         if check():
#             result = count
#         return

#     original = grid[row]

#     dfs(row + 1, count)

#     grid[row] = [0] * W
#     dfs(row + 1, count + 1)

#     grid[row] = [1]* W
#     dfs(row + 1, count + 1)

#     grid[row] = original

# T = int(input())
# for tc in range(1, T + 1):
#     D, W, K = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(D)]

#     result = K
#     dfs(0, 0)

#     print(f'#{tc} {result}')