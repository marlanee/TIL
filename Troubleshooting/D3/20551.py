# 증가하는 사탕 수열. 1차 시도: PASS(16분)

# 1. 목표: 세 개의 숫자를 1 이상의 오름차순 정렬로 만들 때, 각 요소에서 뺀 값의 총합을 구하라.
# 2. 상태: a, b, c = map(int, input().split()) / 새로운 수열은 numbers = [a, b, c] 로 관리
# 3. 자료구조: 자료구조 불필요
# 4. 핵심로직: 
  # 0. 원래의 총 합에서 빼고 난 후의 총합을 뺀다.
  # 1. def cal(numbers): 
  # 2. if a < 1 or b < 2 or c < 3: return -1
  # 3. if b >= c: numbers[1] = numbers[2] - 1
  # 4. if a >= b: numbers[0] = numbers[1] - 1
  # 5. return a + b + c - sum(numbers)
# 5. 종료조건: 함수 실행이 종료되었을 때

def cal(total, numbers):  # 이 함수가 정말 필요한 입력값은 무엇인가?
  if numbers[0] < 1 or numbers[1] < 2 or numbers[2] < 3: # 자기 인자만으로 동작하는 함수가 좋다.
    return -1
  if numbers[1] >= numbers[2]:
    numbers[1] = numbers[2] - 1
  if numbers[0] >= numbers[1]:
    numbers[0] = numbers[1] - 1
  return total - sum(numbers)

T = int(input())
for tc in range(1, T + 1):
  a, b, c = map(int, input().split())
  total = a + b + c
  numbers = [a, b, c]
  print(f'#{tc} {cal(total, numbers)}')