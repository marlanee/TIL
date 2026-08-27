T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    grid_num = N * N
    grid = [[0] * N for _ in range(N)]

    x, y = 0, 0 
    dist = 0

    xl = [1, 0, -1, 0]
    yl = [0, 1, 0, -1]

    for i in range(1, grid_num + 1):
        grid[x][y] = i

        nx = x + xl[dist]
        ny = y + yl[dist]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or grid[nx][ny] != 0:
            dist = (dist + 1) % 5