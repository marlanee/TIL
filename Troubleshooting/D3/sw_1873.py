# 2026-08-24. 1차 시도: PASS(2시간 30분)
# D3 문제인데 뭐가 이렇게 복잡하고 기냐?
# 각 행동마다 구성요소별 실제 동작을 코드로 구현하는 수밖에 없나?

# T = int(input())
# for tc in range(1, T + 1):
#     H, W = map(int, input().split())
#     minimap = [list(input()) for _ in range(H)]
#     N = int(input())
#     control = input().strip()

#     for i, o in enumerate(minimap):
#         if '^' in o:
#             x, y = i, o.index('^')
#         elif 'v' in o:
#             x, y = i, o.index('v')
#         elif '<' in o:
#             x, y = i, o.index('<')
#         elif '>' in o:
#             x, y = i, o.index('>')

#     for c in control:
#         if c == 'U':
#             minimap[x][y] = '^'
#             if x - 1 >= 0:
#                 if minimap[x - 1][y] == '.':
#                     minimap[x - 1][y] = '^'
#                     minimap[x][y] = '.'
#                     x = x - 1
                
#         elif c == 'D':
#             minimap[x][y] = 'v'
#             if x + 1 < H:
#                 if minimap[x + 1][y] == '.':
#                     minimap[x + 1][y] = 'v'
#                     minimap[x][y] = '.'
#                     x = x + 1

#         elif c == 'L':
#             minimap[x][y] = '<'
#             if y - 1 >= 0:
#                 if minimap[x][y - 1] == '.':
#                     minimap[x][y - 1] = '<'
#                     minimap[x][y] = '.'
#                     y = y - 1

#         elif c == 'R':
#             minimap[x][y] = '>'
#             if y + 1 < W:
#                 if minimap[x][y + 1] == '.':
#                     minimap[x][y + 1] = '>'
#                     minimap[x][y] = '.'
#                     y = y + 1

#         else:   # 대망의 S다.
#             if minimap[x][y] == '^':
#                 if x == 0:
#                     continue
#                 else:
#                     for u in range(1, x+1):
#                         if minimap[x-u][y] == '*':
#                             minimap[x-u][y] = '.'
#                             break
#                         elif minimap[x-u][y] == '#':
#                             break

#             elif minimap[x][y] == 'v':
#                 if x == H - 1:
#                     continue
#                 else:
#                     for d in range(1, H - x):
#                         if minimap[x + d][y] == '*':
#                             minimap[x + d][y] = '.'
#                             break
#                         elif minimap[x + d][y] == '#':
#                             break

#             elif minimap[x][y] == '<':
#                 if y == 0:
#                     continue
#                 else:
#                     for l in range(1, y + 1):
#                         if minimap[x][y - l] == '*':
#                             minimap[x][y - l] = '.'
#                             break
#                         elif minimap[x][y - l] == '#':
#                             break
#             else:
#                 if y == W - 1:
#                     continue
#                 else:
#                     for r in range(1, W - y):
#                         if minimap[x][y + r] == '*':
#                             minimap[x][y + r] = '.'
#                             break
#                         elif minimap[x][y + r] == '#':
#                             break

#     print(f'#{tc}', end=' ')
#     for z in minimap:
#         print(f"{''.join(z)}")

# 상호의 배틀필드. Time: 40분

TANK = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)} 
COMMAND = {'U': (-1, 0, '^'), 'D': (1, 0, 'v'), 'L': (0, -1, '<'), 'R': (0, 1, '>')}

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())    # H x W의 게임 격자판 크기
    # grid = [input().strip() for _ in range(H)]
    # 위 코드는 사용 불가. 2차원 행렬로 만들어야 수정이 가능함. 문자열은 불변.
    grid = [list(input()) for _ in range(H)]
    # 리스트로 문자열을 형변환 하면, 하나씩 언패킹되어 요소로 들어간다.
    N = int(input())
    control = input().strip()

    for r in range(H):  # 아래 반복문은 탱크의 위치를 찾는 코드임
        for c in range(W):
            if grid[r][c] in TANK:
                x, y = r, c
                break
        else:   # 반복문 끊는 코드.
            continue
        break

    for c in control:
        s = grid[x][y]  # s는 shape의 약자임. 탱크의 방향 상태.
        if c == 'S':    # c가 S 일 경우 코드다.
            sx = x + TANK[s][0]
            sy = y + TANK[s][1]
            while 0 <= sx < H and 0 <= sy < W and grid[sx][sy] != '#':
                if grid[sx][sy] == '*':
                    grid[sx][sy] = '.'
                    break
                sx = sx + TANK[s][0]
                sy = sy + TANK[s][1]

        else:
            grid[x][y] = COMMAND[c][2]
            nx = x + COMMAND[c][0]
            ny = y + COMMAND[c][1]
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
                grid[nx][ny] = grid[x][y]
                grid[x][y] = '.'
                x, y= nx, ny

    print(f'#{tc}', end = ' ')
    for row in grid:
        print(''.join(row))