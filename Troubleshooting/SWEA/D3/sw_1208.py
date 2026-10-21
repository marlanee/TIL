# 26-08-15 1차 시도: Pass(11분 소요)
# 박스 평탄화 문제

# for i in range(1, 11):
#   N = int(input())
#   boxes = list(map(int, input().split()))
#   # 최댓값에서 1을 빼고, 최솟값에 1을 더하면 되는거 아닌가?
#   # N번 반복한 후 최댓값 - 최솟값을 출력하면 되는거지.
#   for x in range(N):
#     max_box = boxes.pop(boxes.index(max(boxes)))
#     boxes.append(max_box - 1)
#     min_box = boxes.pop(boxes.index(min(boxes)))
#     boxes.append(min_box + 1)

#   result = max(boxes) - min(boxes)
#   print(f'#{i}', result)

# Gemini가 보기에는 많이 아쉽다고 한다.
# 아래는 Gemini의 코드다

for tc in range(1, 11):
  N = int(input())
  boxes = list(map(int, input().split()))

  for _ in range(N):
    max_idx = boxes.index(max(boxes))
    min_idx = boxes.index(min(boxes))

    if boxes[max_idx] - boxes[min_idx] <= 1:   # 조건 만족시 작업을 종료하는 로직 추가.
      break

    boxes[max_idx] -= 1   # pop, append를 쓰지 않고 인덱스 값을 직접 수정했다
    boxes[min_idx] += 1   # 이 방법을 사용하면 메모리와 연산 속도가 훨씬 빨라진다

  result = max(boxes) - min(boxes)
  print(f'#{tc} {result}')