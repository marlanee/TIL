T = int(input())

for i in range(1, T + 1):   # T번만큼, 줄바꿈하면서 정수를 받아 N에 넣음
    N = int(input())

    snail_list = [[0] * N for _ in range(N)]   # 달팽이 리스트를 0이 가득한 행렬로 만듦

    row_list = [0, 1, 0, -1]   # row를 이동시키는 숫자를 담은 리스트 작성
    column_list = [1, 0, -1, 0]   # column을 이동시키는 숫자를 담은 리스트 작성

    row = 0   # 멍청한 달팽이의 첫 시작 행 위치
    column = 0   # 멍청한 달팽이의 첫 시작 열 위치
    direction = 0 # 거리? 벽에 박히는 것을 감지할 때 들어가는 변수임

    for num in range(1, N * N + 1):   # 달팽이는 반드시, 1부터 N의 제곱까지의 숫자를 남기면서 지나가야함
        snail_list[row][column] = num   # 0이 가득한 바둑판에, 한 칸 씩 지나가며 숫자를 남길 예정임

        new_row = row + row_list[direction]   # 새로운 row는 기존 row + 이동시키는 숫자가 될 것임
        new_column = column + column_list[direction]   # 이것도 마찬가지임

        # 이제 그 대망의, 벽에 충돌하면 방향을 전환하는 코드를 작성해야 한다. 뭐, 괜찮다. 조금씩 하면 되는거 아니냐.
        # 심호흡하고, 어떤 조건이 돼야 벽에 박을지 생각해보자.
        # 첫째, new_row 또는 new_column이 N보다 크면 안된다. 완전히 벽에 박는다. 다음 숫자가 N일 때 방향을 바꿔야 한다.
        # 둘째? 뭐가 있을까? 숫자에 박는 경우다. 그게 어떤 경우일까? 다음 위치가, 0이 아닌 다른 숫자가 들어있는 경우다.
        # 셋째? 숫자와 벽을 다 했으니 된거 아닌가? 일단 해보자.
        # 벽을 만났다면, new_row와 new_column의 값을 바꿔서, 다른 칸으로 가야 한다.
        # gemini가 dist를 4로 나누던데, 이유는 모르겠다. 우선 작성해보고 차근차근 이해해보자. -> 아! 움직이는 방향을 바꿔야 하기 때문이다. distance 가 아니라 direction인 듯 하다.

        if new_row == N or new_column == N or snail_list[new_row][new_column] != 0:
            direction = (direction + 1) % 4
            new_row = row + row_list[direction]
            new_column = column + column_list[direction]

        # 자, 이제 모든 연산이 끝났으면 새로운 칸으로 이동해야 한다.
        row = new_row
        column = new_column

# 이제 완전히 바뀐 snail_list를 출력해보자.
# 다만, 한 줄에 N 개의 숫자씩 출력해야 한다.
    print(f"#{i}")
    for y in snail_list:
        print(y)
        #print(int(''.join(map(str,y))))
# 오 완성했다. 그런데, 리스트가 아니라 숫자로 출력해야 하는데.
    


    '''
snail_list = [[0] * 3 for _ in range(3)]
[0, 0, 0],
[0, 0, 0],
[0, 0, 0]
'''