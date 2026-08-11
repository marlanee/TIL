# 26.08.12. 1차 시도: PASS
N = int(input())

# 문자열로 자연수 N까지의 수열을 리스트로 만들자
# 그 리스트를 순회하며 하나씩 출력하자
# 출력할 때 3,6,9가 있으면 '-'를 출력하는 if문을 만들자

for i in range(1, N + 1):
  x = str(i)
  count_num = x.count('3') + x.count('6') + x.count('9')
  if count_num == 0:
    print(x, end=' ')
  else:
    print("-" * count_num, end=' ')