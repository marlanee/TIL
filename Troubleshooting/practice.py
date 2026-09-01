# 달팽이 문제 복습. 1차 시도:
# 달팽이는 2차원 행렬 문제다.
# 벽이나 숫자를 만나면 꺾어야 한다.
# 진행 방향이 우 하 좌 상 으로 정해져 있다.
# 방향을 담는 리스트를 만들고, 벽이나 숫자에 막히면 다음 리스트 요소로 넘어간다.
T = int(input())

for tc in range(1, T + 1):
  N = int(input())
  grid = [[0] * N for _ in range(N)]  # 2차원 행렬 선언

  x, y = 0, 0   # 달팽이의 첫 위치
  dist = 0  # 진행 방향 결정요소

  nx = [1, 0, -1, 0]  # x축 진행방향
  ny = [0, 1, 0, -1]  # y축 진행방향

  for i in range(1, N * N + 1):
    grid[y][x] = i
    cx = x + nx[dist]
    cy = y + ny[dist]

    if cx < 0 or cx >= N or cy < 0 or cy >= N or grid[cy][cx] != 0: # 달팽이가 벽이나 숫자를 만날 경우
      dist = (dist + 1) % 4 # 상하좌우를 모두 돈 이후에는 처음부터 다시 반복
      cx = x + nx[dist]
      cy = y + ny[dist]

    x = cx
    y = cy

  print(f'#{tc}')
  for x in grid:
    print(*x)
