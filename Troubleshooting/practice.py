def dev(index, current_score, current_cal):
  global max_score
  if current_cal > L:
    return

  if index == N:
    max_score = max(max_score, current_score)
    return

  score, cal = foods[index]
  dev(index + 1, current_score + score, current_cal + cal)
  dev(index + 1, current_score, current_cal)

T = int(input())

for i in range(1, T + 1):
  N, L = map(int, input().split())
  foods = [list(map(int, input().split())) for _ in range(N)]

  max_score = 0

  dev(0, 0, 0)

  print(f'#{i} {max_score}')