# 2026-08-24. 1차 시도: PASS(2시간 30분)
# 2026-08-25. 2차 시도: Half PASS(50분)

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

# 아래는 gemini의 코드다
# 델타 딕셔너리 기반 압축 풀이라고 한다. 이름이 거창하다
# DIRS = {'U': (-1, 0, '^'), 'D': (1, 0 , 'v'), 'L': (0, -1, '<'), 'R': (0, 1, '>')}
# SHOOT_DELTAS = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

# T = int(input())
# for tc in range(1, T + 1):
#   H, W = map(int, input().split())
#   grid = [list(input().strip()) for _ in range(H)]
#   input()
#   cmds = input().strip()

#   x, y = next((r, c) for r in range(H) for c in range(W) if grid[r][c] in SHOOT_DELTAS)
#   # next 함수가 뭐지? -> 원하는 걸 찾으면 바로 값을 반환하고 break

#   for cmd in cmds:
#     if cmd in DIRS:
#       dx, dy, shape = DIRS[cmd] 
#       grid[x][y] = shape
#       nx, ny = x + dx, y + dy
#       if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
#         grid[nx][ny], grid[x][y] = shape, '.'
#         x, y = nx, ny

#     else:
#       sx, sy = SHOOT_DELTAS[grid[x][y]]
#       bx, by = x + sx, y + sy
#       while 0 <= bx < H and 0 <= by < W:
#         if grid[bx][by] == '*':
#           grid[bx][by] = '.'
#           break
#         if grid[bx][by] == '#':
#           break
#         bx, by = bx + sx, by + sy

#   print(f'#{tc} {"".join(grid[0])}')
#   for row in grid[1:]:
#     print("".join(row))

# 배틀필드 문제다.
# 나는 1차 시도에 2시간 30분만에 80줄의 코드로 PASS했다.

CONTROL = {'U': (-1, 0, '^'), 'D': (1, 0, 'v'), 'L':(0, -1, '<'), 'R':(0, 1, '>')}
SHOOT = {'^': (-1, 0), 'v':(1, 0), '<':(0, -1), '>':(0, 1)}

T = int(input())
for tc in range(1, T + 1):
  H, W = map(int, input().split())
  grid = [list(input()) for _ in range(H)]
  N = input()
  command = input()

  for a in range(H):
    for b in range(W):
      if grid[a][b] in SHOOT:
        x, y = a, b
        break

  for c in command:
    if c in CONTROL:
      grid[x][y] = CONTROL[c][2]
      mx = CONTROL[c][0]
      my = CONTROL[c][1]
      if 0 <= x + mx < H and 0 <= y + my < W and grid[x+mx][y+my] == '.':
        grid[x][y] = '.'
        grid[x+mx][y+my] = CONTROL[c][2]
        x, y = x + mx, y + my

    else:   # S인 경우
      sx = SHOOT[grid[x][y]][0]
      sy = SHOOT[grid[x][y]][1]
      cx = x + sx
      cy = y + sy
      while 0 <= cx < H and 0 <= cy <  W:
        if grid[cx][cy] == '*':
          grid[cx][cy] = '.'
          break
        elif grid[cx][cy] == '#':
          break
        cx += sx
        cy += sy

  print(f'#{tc}', end=' ')
  for z in grid:
    print(f"{''.join(z)}")