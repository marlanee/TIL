# 2026_08_04 1차 풀이:
# 숫자가 주어지면, 그 크기의 파스칼 삼각형을 출력해야 하는 문제다.

T = int(input())

for u in range(1, T + 1):
  triangle_size = int(input())

  # 이제 삼각형을 출력하는 코드를 작성해야 한다. 어떤 규칙이 있을까?
  # 양 끝 숫자는 항상 1이다
  # n행의 n열에 있는 숫자는 n-1행의 n-1열 + n열 이다.
  # 첫 출력값은 1로 하드 코딩 해도 될 듯 하다. 규칙이 없어 보인다.
  # print(1)    # 알고리즘에 넣었다. 지우자.
  # 두 번째 출력값도 마찬가지다.
  # print(1, 1)   # 1 1이 출력된다. 한 칸 띄워서 출력되네? 붙여서 출력되면 정수 11이라 그런가보다.
  # 아니다. 두 번째 출력값부터 알고리즘에 넣어보자.
  # 일단 삼각형의 크기 * 삼각형의 크기 인 행렬을 만들어보자. 여기에 하나씩 추가해보자.
  triangle_shape = [[0] * triangle_size for _ in range(triangle_size)]   # 리스트 컴프리헨션 성공했다! sorted(반환값, key=lambda x:) 함수와 비슷하네. 
  triangle_shape[0][0] = 1
  for i in range(triangle_size):   # 깨달았다. for 반복문이 최소 2중으로 필요하다. i 말고 다른 반복 변수가 필요해.
    triangle_shape[i][0] = 1
    triangle_shape[i][i] = 1   # triangle_shape[i][0, 1] 이런것도 되나? 궁금하다. 나중에 피드백할 때 알려줘 gemini야.
    for x in range(i):   # 우선 0번째 칸과 i번째 칸에 1을 집어넣어야 한다. / # range() 범위 조절로 0번째 칸과 i번째 칸에도 적용되는걸 방지한다.
      # 이제 더하는 알고리즘을 작성해야 한다.
      if x != 0 and x != i:
        triangle_shape[i][x] = triangle_shape[i - 1][x - 1] + triangle_shape[i - 1][x]

  print(f'#{u}')
  # for row in triangle_shape:
  #   for result in row:
  #     if result == 0:
  #             break
  #     print(result, end=' ')   # 문제 발생. 모든 row가 이어져서 출력된다.

  for row in triangle_shape:
    for result in row:
      if result == 0:
              break
      print(result, end=' ')   # 문제 발생. 모든 row가 이어져서 출력된다.
    print()   # 한 칸 아예 띄우는 줄 알았는데 end만 바꾸네? 줄바꿈이 하나 추가되는거구나.

       


  #1
  #1 1
  #1 2 1
  #1 3 3 1
  #1 4 6 4 1
  #1 5 10 10 5 1