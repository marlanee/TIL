T = int(input())

for i in range(1, T+1):
  N, M = map(int, input().split())

  fly_list = []
  fly_number = 0
  new_fly_number = 0
  for _ in range(N):
    fly_list.append(list(map(int, input().split())))

    # 행 x 열 : 2 x 2칸이 최대가 될 때를 찾는 코드를 작성해야 한다.
  for column_move in range(N - M + 1):
    for row_move in range(N - M + 1):
      new_fly_number = 0
      for column_fly in range(M):
        for row_fly in range(M):
          new_fly_number = new_fly_number + fly_list[column_move + column_fly][row_move + row_fly]

      if new_fly_number > fly_number:
        fly_number = new_fly_number

  print(f"#{i} {fly_number}")