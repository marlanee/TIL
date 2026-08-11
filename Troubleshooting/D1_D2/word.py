T = int(input())   # 테스트 케이스의 개수 T
N, K = map(int, input().split())   # 퍼즐의 크기 N과 단어의 길이 K 입력

# 이제, 퍼즐의 모양이 2차원 정보로 주어진다. 이것을 받을 코드를 작성해야 된다.
# 일단, 한 줄 씩 띄워서 입력해주기 때문에 for 반복문을 사용해보자.
# 받아서 바로 리스트에 넣어버리자.
for _ in range(1, T + 1):   # 10번 반복해서 입력받아야 한다. #T 출력을 위해 1부터 시작했다.
  puzzle_list = []   # 퍼즐의 틀과 모양이다.  
  puzzle_number = 0   # 단어가 들어갈 수 있는 개수이다.

  for _ in range(N):
    puzzle_list.appned(list(map(int, input().split())))   # 입력받은 숫자로 퍼즐의 모양을 완성함

# 이제 단어를 퍼즐에 딱 맞게 끼우는 방법을 찾아야 한다.
# 가로든, 세로든 1이 연속으로 K개 있으면 숫자 + 1이다.
# 일단, 가로를 체크해보자. 어렵지 않으니까.
# 아니, 어쩌면 세로와 비슷한 매커니즘일수도 있다. 같이 생각하자.
# 그런데 K 개가 연속으로 1인지 어떻게 판단하지?
# K개가 연속으로 1인 것을 찾는 코드
# 1을 만나면 값이 1 오르는 변수를 설정하는거다. 
# 그러다가 값이 K에서 멈추면 puzzle_number에 1을 더하는거다.
# 값이 K 일때 다음게 0이면 되는거다.
  for colunm in puzzle_list:   # 가로에서 몇 개 들어갈지 구할 수 있다.
    puzzle_length = 0
    for colunm_test in colunm:
      if colunm_test == 1:
        puzzle_length += 1
      else:
        if puzzle_length == K:
          puzzle_number += 1
        else:
          puzzle_length = 0
