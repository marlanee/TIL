# 2026-08-23. 1차 시도: PASS(19분)

T = int(input())
for tc in range(1, 1+ T):
  n = list(map(int, input().strip()))
  count = 0
  # 플래그 방식으로 풀어보자.
  flag = False

  for i in n:
    if i == flag:
      continue
    else:
      count += 1
      if not flag:
        flag = True
      else:
        flag = False
  print(f'#{tc} {count}')

# 잘 했지만 아쉽단다.
# 아래는 gemini의 코드다

import sys

input = sys.stdin.readline   # 문자열 입력할 때 반드시 쓰란다. 습관적으로. 입출력 속도를 줄여준대.

T = int(input())
for tc in range(1, T + 1):
  target = input().strip()   # sys 라이브러리 사용할 때는 문자열 입력시 strip 필수래.
  count = 0
  current = '0'

  for bit in target:
    if bit != current:
      count += 1
      current = bit

  print(f'#{tc} {count}')