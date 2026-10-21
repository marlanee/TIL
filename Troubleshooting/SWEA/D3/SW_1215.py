# 2026-08-12  # 1차 시도: Fail
# 26-08-13. 2차 시도: Neutral
# 26-09-03. 복습: PASS(11분) / 안녕. 이제는 쉽다

# 인생 최초 D3 문제 도전
# 회문 문제
# 8 x 8 2차원 행렬에서 제시된 길이를 가진 회문의 개수를 반환해야함
# 행렬의 내용은 A, B, C 중 하나임
# for i in range(1, 11):
#     find_len = int(input())   # 제시된 길이 변수 선언
#     # 주어진 8 x 8 2차원 행렬을 받는 코드 작성
#     total_word = []   # 8 x 8 2차원 행렬 글자판
#     for _ in range(8):
#         row_word = list(input().strip())   # 문자열을 리스트에 넣으면 한 글자씩 담긴다.
#         total_word.append(row_word)   # 행렬 글자판 완성!
#     # 다음으로, 행렬 글자판에서 회문의 개수를 구해야 한다.
#     # 회문을 어떻게 구했더라. 슬라이싱을 썼던 것 같은데.
#     # 아래는 회문 탐색 코드이다.
#     total_count = 0  # 일치하는 회문 개수를 담는 변수

#     # 회문 탐색을 어떻게 해야되지?
#     for x in range(8):   # 이 코드는 row를 탐색하는 코드이다.
#         for y in range(8 - find_len + 1):
#             sub_str = total_word[x][y:y + find_len]   # find_len 길이만큼의 칸을 우측으로 이동하며 탐색! 가히 천재적이다.

#             if sub_str == sub_str[::-1]:
#                 total_count += 1

#     # 자, 이제 column을 탐색해야 한다.
#     for y in range(8):
#         for x in range(8 - find_len + 1):
#             sub_str = []
#             for z in range(find_len):
#                 sub_str.append(total_word[x + z][y])
#             # 더 좋은 방법: sub_str = [total_word[x + z][y] for z in range(find_len)]

#             if sub_str == sub_str[::-1]:
#                 total_count += 1

#     print(f'#{i} {total_count}')

# for i in range(1, 11):
#     N = int(input())

#     grid = [list(input()) for _ in range(8)]   # 격자 생성

#     # 가로와 세로를 분리해서 길이에 맞는 순회문을 찾아야 한다.
#     total_num = 0
#     # 아래는 가로 순회문을 찾는 코드이다.
#     for c in range(8):
#         for r in range(9 - N):
#             sub_str = grid[c][r:r + N]
#             if sub_str == sub_str[::-1]:
#                 total_num += 1
#     # 아래는 세로 순회문을 찾는 코드이다.
#     for r in range(8):   # 젠장, 코드를 잘못 적어서 가로를 한번 더 순회했다.
#         for c in range(9 - N):
#             sub_list = [grid[c + x][r] for x in range(N)]
#             if sub_list == sub_list[::-1]:
#                 total_num += 1
#     print(f'#{i} {total_num}')

# 회문1. 복습: PASS(11분)

# 목표: 주어진 길이 M 만큼의 회문을 찾아야 함. 행과 열 둘 다.
# 구조: 열 전치로 total_grid를 만들고 리스트 슬라이싱으로 탐색
# 종료: for r in range(2 * 8) 가 종료될 때. 회문에 해당하는 count 수를 출력

for tc in range(1, 11):
    M = int(input())
    row_grid = [list(input()) for _ in range(8)]
    col_grid = list(zip(*row_grid))
    total_grid = row_grid + col_grid
    count = 0

    for r in range(16):
        for c in range(8 - M + 1):
            word = total_grid[r][c:c + M]
            if word == word[::-1]:
                count += 1

    print(f'#{tc} {count}')