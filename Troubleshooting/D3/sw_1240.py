# 2026-08-18. 1차 시도: PASS(80분 소요)

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
# 아래는 gemini의 코드다

PATTERNS = {
    '0001101' : 0, '0011001': 1, '0010011': 2, '0111101' : 3, '0100011': 4,
    '0110001' : 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9
}   # 변하지 않는 값이라 변수명을 대문자로 선언. 메모리 아끼려고 딕셔너리 형태로 선언

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]

    for row in grid:
        if '1' in row:
            end_idx = row.rindex('1')
            code = [
                PATTERNS[row[end_idx - 55 + 7 * y : end_idx - 48 + 7 * y]]
                for y in range(8)
            ]

            odd_sum = sum(code[0::2])
            even_sum = sum(code[1::2])

            if (odd_sum * 3 + even_sum) % 10 == 0:
                print(f'#{tc} {sum(code)}')
            else:
                print(f'#{tc} 0')

            break
