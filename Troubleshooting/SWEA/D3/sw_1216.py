# 체스판 문제를 언제까지 묵혀둘 것인가. 오늘 승부를 봐야 한다.
# 2026-08-23. 1차 시도: PASS(60분)

# 100x100 행렬에서 가로, 세로 중 가장 긴 회문의 길이를 구하는 문제
# grid로 주어진 행렬을 입력받자.
# 행렬을 row, column으로 순회하며 가장 긴 회문의 길이를 찾자.
# 찾는 방식은? 
# row의 경우 뒤집은 글자가 동일하면 찾는걸로 하자. 큰 길이부터 탐색해서.
# 그러면 굳이 list 행렬로 받을 필요가 있나?
# column의 경우에도 마찬가지로, row 형식으로 바꿔서 같은 방법을 사용하자
# row 형식은 리스트 컴프리헨션으로 만들자
for _ in range(1, 11):
  tc = int(input())
  grid = [input().strip() for _ in range(100)]

  max_len = 0

  for row in grid:
    for x in range(100):
      for y in range(100 - x):
        if row[x:100-y] == row[x:100-y][::-1] and len(row[x:100-y]) > max_len:
          max_len = len(row[x:100-y])
          break

  column = []

  for t in range(100):
    column.append(''.join([grid[c][t] for c in range(100)]))

  for z in column:
    for a in range(100):
      for b in range(100 - a):
        if z[a:100-b] == z[a:100-b][::-1] and len(z[a:100-b]) > max_len:
          max_len = len(z[a:100-b])
          break

  print(f'#{tc} {max_len}')

# Gemini의 총평: 코드 결함은 없으나 CPU 연산시간이 너무 길다.
# 낭비가 많은 코드다.
# 직관적이지만 낭비가 많다. 눈물 ㅠ

# 아래는 Gemini의 코드다
# 얼마나 잘 짰나 보자. 이새끼야.

def solve_grid(grid):   # 함수를 쓰네?
  all_lines = grid + [''.join(col) for col in zip(*grid)]   # * 은 언패킹 연산자. 리스트 요소들을 하나씩 푼다. zip함수는 여러 문자열에서 같은 인덱스의 글자들을 묶어 튜플로 반환함

  for length in range(100, 0, -1):   # 긴 길이먼저 탐색한다.
    for line in all_lines:
      for start in range(100 - length + 1):
        target = line[start:start + length]
        if target == target[::-1]:
          return length

  return 1

for _ in range(10):
  tc = int(input())
  grid = [input().strip() for _ in range(100)]
  print(f'#{tc} {solve_grid(grid)}')