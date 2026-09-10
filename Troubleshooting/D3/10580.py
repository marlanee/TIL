# 전봇대. 1차 시도: PASS(30분)

# 1. 목표: 두 양의 정수 a, b들이 N개 주어질 때, 선분 ab들의 교차점이 몇 개인지 구한다.
# 2. 상태: lines = [[a, b]]로 선분들을 관리
# 3. 자료구조: 2중 반복문
# 4. 핵심로직
#   1. for r in range(N):
#   2. for c in range(r, N):
#   3. if lines[r][0] < lines[c][0] and lines[r][1] > lines[c][1]: count += 1
#   4. elif lines[r][0] > lines[c][0] and lines[r][1] < lines[c][1]: count += 1
# 5. 종료조건: for문이 모두 끝날 때

T = int(input())
for tc in range(1, T + 1):
  N = int(input())
  lines = [list(map(int, input().split())) for _ in range(N)]

  count = 0

  for r in range(N):
    for c in range(r + 1, N):
      if (lines[r][0] < lines[c][0] and lines[r][1] > lines[c][1]) or (lines[r][0] > lines[c][0] and lines[r][1] < lines[c][1]):
        count += 1

  print(f'#{tc} {count}')