# 문자열에서 반복되는 패턴의 길이 구하기. 마디의 길이는 최대 10, 문자열 길이는 30

# T = int(input())
# for i in range(1, T + 1):
#   test_str = input()   # 문자열을 T번만큼 입력받으려고 작성한 코드임.
#   set_str = set(test_str)
#   print(set_str)
#   print(f"#{i} {len(set_str)}")
# 이게 아니다. 세트가 아니다. SAMSUNG 같은 경우 S가 모두 날아간다.

T = int(input())
for i in range(1, T + 1):
  test_str = input()   # 문자열을 T번만큼 입력받으려고 작성한 코드임.
  # 슬라이싱으로 하드 코딩은 하기 싫다. 뭐 방법이 없을까?
  # 모르면 하드 슬라이싱이지 뭐. 하자.
  for x in range(1, 11):
    slice_str = test_str[:x]
    count_str = len(test_str) // x

    if test_str[:x * count_str] == slice_str * count_str:
      print(f"#{i} {x}")
      break
