# 2026_08_04 1차 풀이: 성공
# 어떤 수도회사를 고를까?
# P: A사의 요금/L 
# Q: B사의 기본 요금
# R: B사의 기본 요금 상한
# S: B사의 추가 요금/L
# W: 수도 사용량/L

T = int(input())

for i in range(1, T + 1):
  # test_num = list(map(int, input().split()))   # 리스트로 묶어 필요한 요소를 하나씩 빼려고 형변환했다.
  # P = test_num[0]
  # Q = test_num[1]
  # R = test_num[2]
  # S = test_num[3]
  # W = test_num[4]   # 이것들은 보기에, 작성하기에 편하려고 선언한 변수이다.
  P, Q, R, S, W = map(int, input().split())   # 이런 식으로도 map 함수로 묶어 하나씩 지정 가능하다. 홀리 몰리. 한 줄로 끝나는군.

  A_total = P * W   # A사 사용시 총 요금량
  B_total = Q + (S * (W - R))
  if W - R < 0:   # 기본 요금보다 적게 사용하면 기본 요금만 받는다.
    B_total = Q

  # if A_total < B_total:   # 처음에 부호를 반대로 썼다. 바본가.
  #   print(f'#{i} {A_total}')
  # else:
  #   print(f'#{i} {B_total}')

  min_cost = min(A_total, B_total)   # min 함수 사용으로 if-else문을 생략했다. 대단하다
  # 튜플을 생성하지 않고, 바로바로 A_total과 B_total을 min 함수에 넘기는 방식으로 동작한다.
  # Ex) min(100, 20) / 즉, min 함수 내부에 패킹하지 않고 숫자를 나열해도 min 함수는 동작한다.
  print(f'#{i} {min_cost}')   