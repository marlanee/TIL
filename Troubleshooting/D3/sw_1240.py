# 2026-08-18. 1차 시도: PASS(80분 소요)
# 2026-08-19. 2차 시도: PASS

# T = int(input())

# for i in range(1, T + 1):
#     c, r = map(int, input().split())
#     grid = [input().strip() for _ in range(c)]

#     numbers = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
#     code = ''
#     real_code = 0

#     for x in grid:
#         if '1' in x:
#             ei = x.rindex('1')
#             for y in range(8):
#                 code += str(numbers.index(x[(ei - 55 + 7 * y):(ei - 48 + 7 * y)]))
#                 if y % 2 == 0:
#                     real_code += int(code[y]) * 3
#                 else:
#                     real_code += int(code[y])
#             if real_code % 10 == 0:
#                 print(f'#{i} {sum(list(map(int, code)))}')
#                 break
#             else:
#                 print(f'#{i} 0')
#                 break

# 솔직히 자신 없었다. 어찌저찌 돌아간다 해도 이건 거의 실패했다.
password = {'0001101' : 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001' : 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    result = 0
    result_list = []

    for i in grid:
        if '1' in i:
            ed = i.rindex('1')
            for x in range(8):
                result_list.append(password[i[ed - 55 + 7 * x: ed - 48 + 7 * x]])
            sum_odd = sum(result_list[::2]) * 3
            sum_even = sum(result_list[1::2])
            result = sum_odd + sum_even
            if result % 10 == 0:
                print(f'#{tc} {sum(result_list)}')
            else:
                print(f'#{tc} 0')
            break
