# 2026-08-24. 1차 시도: PASS(2시간 30분)
# D3 문제인데 뭐가 이렇게 복잡하고 기냐?
# 각 행동마다 구성요소별 실제 동작을 코드로 구현하는 수밖에 없나?

T = int(input())
for tc in range(1, T + 1):
    H, W = map(int, input().split())
    minimap = [list(input()) for _ in range(H)]
    N = int(input())
    control = input().strip()

    for i, o in enumerate(minimap):
        if '^' in o:
            x, y = i, o.index('^')
        elif 'v' in o:
            x, y = i, o.index('v')
        elif '<' in o:
            x, y = i, o.index('<')
        elif '>' in o:
            x, y = i, o.index('>')

    for c in control:
        if c == 'U':
            minimap[x][y] = '^'
            if x - 1 >= 0:
                if minimap[x - 1][y] == '.':
                    minimap[x - 1][y] = '^'
                    minimap[x][y] = '.'
                    x = x - 1
                
        elif c == 'D':
            minimap[x][y] = 'v'
            if x + 1 < H:
                if minimap[x + 1][y] == '.':
                    minimap[x + 1][y] = 'v'
                    minimap[x][y] = '.'
                    x = x + 1

        elif c == 'L':
            minimap[x][y] = '<'
            if y - 1 >= 0:
                if minimap[x][y - 1] == '.':
                    minimap[x][y - 1] = '<'
                    minimap[x][y] = '.'
                    y = y - 1

        elif c == 'R':
            minimap[x][y] = '>'
            if y + 1 < W:
                if minimap[x][y + 1] == '.':
                    minimap[x][y + 1] = '>'
                    minimap[x][y] = '.'
                    y = y + 1

        else:   # 대망의 S다.
            if minimap[x][y] == '^':
                if x == 0:
                    continue
                else:
                    for u in range(1, x+1):
                        if minimap[x-u][y] == '*':
                            minimap[x-u][y] = '.'
                            break
                        elif minimap[x-u][y] == '#':
                            break

            elif minimap[x][y] == 'v':
                if x == H - 1:
                    continue
                else:
                    for d in range(1, H - x):
                        if minimap[x + d][y] == '*':
                            minimap[x + d][y] = '.'
                            break
                        elif minimap[x + d][y] == '#':
                            break

            elif minimap[x][y] == '<':
                if y == 0:
                    continue
                else:
                    for l in range(1, y + 1):
                        if minimap[x][y - l] == '*':
                            minimap[x][y - l] = '.'
                            break
                        elif minimap[x][y - l] == '#':
                            break
            else:
                if y == W - 1:
                    continue
                else:
                    for r in range(1, W - y):
                        if minimap[x][y + r] == '*':
                            minimap[x][y + r] = '.'
                            break
                        elif minimap[x][y + r] == '#':
                            break

    print(f'#{tc}', end=' ')
    for z in minimap:
        print(f"{''.join(z)}")