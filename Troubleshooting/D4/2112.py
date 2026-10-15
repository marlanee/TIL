# SWEA 2112. 보호 필름
# 1차 시도: Reutime Error(1시간) 
# 10. 08. 복습 필요 / 최적화 필요
# 10. 15. 복습: PASS(28분)
# 졸업

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

# def dfs(row, count):
#     global result

#     if count >= result:
#         return

#     check_grid = 0

#     for c in range(W):
#         streak = 1
#         previous = grid[0][c]
#         for r in range(1, D):
#             current = grid[r][c]
#             if previous == current:
#                 streak += 1
#             else:
#                 streak = 1

#             previous = current

#             if streak >= K:
#                 check_grid += 1
#                 break

#         if streak < K:
#             break


#     if check_grid == W:
#         result = min(result, count)
#         return

#     if row == D:
#         return

#     dfs(row + 1, count)

#     test_1 = grid[row]
#     grid[row] = [0] * W
#     dfs(row + 1, count + 1)
#     grid[row] = test_1

#     test_2 = grid[row]
#     grid[row] = [1] * W
#     dfs(row + 1, count + 1)
#     grid[row] = test_2

# T = int(input())
# for tc in range(1, T + 1):
#     D, W, K = map(int, input().split())
#     grid = [list(map(int, input().split())) for _ in range(D)]

#     result = K
#     dfs(0, 0)

#     print(f'#{tc} {result}')


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

# SWEA 2112. 보호 필름
# 10. 15. 복습: PASS(28분)
# 졸업

"""
목표: D x W 크기의 보호 필름이 주어진다.
    0. 보호 필름이 성능 검사를 통과할 수 있도록 만들고, 그 때의 최소 약품 투입 횟수를 구하여라
    1. 성능 검사: 각 열마다 연속한 값이 k번 반복되어야 통과한다.
    2. 약품 투입: 각 행을 특정 값으로 모두 변환한다.
상태: min_count = 최소 약품 투입 횟수
자료구조: DFS / 백트래킹
핵심로직: 
    1. DFS 재귀호출 3단계로 구성 / 
        1. 약품 투입 x 
        2. A 특성으로 약품 투입
        3. B 특성으로 약품 투입
    2. 종료 조건: 성능 검사 조건을 만족할 때
    2-2. 종료 조건 추가: row == D 일 때.
    3. 가지치기: 현재까지 구한 최소 약품 투입 횟수보다 크거나 같을 때
    4. dfs 매개변수 종류: dfs(row, count)
        1. row = 필름의 bar에 해당함. 약품을 투입하지 않아도 1씩 증가하며 호출
        2. count = 약품의 투약 횟수. 약품을 투약할 때만 1씩 증가
    5. 백트래킹: 약품을 투약하기 전 row 상태를 저장해 둔 후 약품 투입. 호출 후 원상태로 백트래킹
    6. dfs 시작 값: dfs(0, 0)
종료조건: 성능 검사 조건 만족, row == D / 출력값: 최소 약품 투입 횟수
시간 복잡도: O(3^D * W * D)
"""

def dfs(row, count):
    global min_count

    if count >= min_count:  # 더 탐색해도 의미가 없음. 가지치기
        return
    
    if check(grid): # 조건을 만족했는지 검사
        min_count = count
        return

    if row == D:    # 끝까지 탐색했다면 더 나아갈 수 없음.
        return

    dfs(row + 1, count) # 약품 투입 안 하는 경우

    save = grid[row]    # 백트래킹을 위해 원본 값 저장

    grid[row] = [0] * W
    dfs(row + 1, count + 1) # A로 바꾸는 약품 투입
    grid[row] = save   # 백트래킹

    grid[row] = [1] * W
    dfs(row + 1, count + 1) # B로 바꾸는 약품 투입
    grid[row] = save


def check(grid):    # 조건을 만족했는지 검사하는 함수. 각 행에서 같은 문자가 K번 반복되었는지 확인
    for c in range(W):
        current = 1
        for r in range(D - 1):
            if current == K:
                break
            if grid[r][c] == grid[r + 1][c]:
                current += 1
            else:
                current = 1

        if current < K: # 한 줄이라도 조건 불만족시 False 반환
            return False

    return True


T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(D)]

    min_count = K   # K번 투입하면 반드시 조건을 만족하므로 최댓값으로 미리 설정

    dfs(0, 0)

    print(f'#{tc} {min_count}')