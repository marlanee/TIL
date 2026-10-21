# 내가 어제 작성한 코드 다 어디 갔어?
# 처음부터 다시!

T = int(input())

for i in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle_list = []

    for _ in range(N):
        puzzle_list.append(list(map(int, input().split())))

    puzzle_num = 0

    # 1이 연속해서 K개 일 경우에만 puzzle_num 숫자를 1 증가시키기로 했었지.


# 아래는 가로 퍼즐을 세는 방식임
    for row in puzzle_list:   # 여기선 1열씩 row에 들어갈 것이다. -> 들어간다
        one_number = 0   # 해당 칸에 1이 있을 경우 숫자가 올라갈 예정인 변수이다.

        for square in row:   # 한 칸에 뭐가 있는지 체크해보자.
            if square == 1:   # 1이 있을 경우 one_number의 숫자가 하나씩 올라가고
                one_number += 1
            else:
                if one_number == K:   # 0을 만났을 때 one_number가 K면 퍼즐 조건을 만족한다.
                    puzzle_num += 1   # 따라서 puzzle_num 숫자를 1 증가시킴
                one_number = 0   # 그리고 다시 초기화
# 하나가 부족하다. 0을 만나지 않고 for 문이 끝났을 떄 puzzle_num 이 K 일 경우.

        if one_number == K:   # 하나의 row 가 종료되었을 때 조건을 만족하면 puzzle_num을 1 증가
            puzzle_num += 1


# 이제 세로 퍼즐 로직을 구현을 시작해야함
# 세로의 경우, puzzle_list의 row는 고정되고 column만 1씩 증가하며 체크해야함
# 그렇다면, N * N 번 체크해야 한다는 결론이 나옴
# 그리고 N번 마다, row를 한 칸씩 오른쪽으로 이동시켜야 함

    for x in range(N):
        one_number = 0

        for y in range(N):
            if puzzle_list[y][x] == 1:   # 가로와 크게 다르지 않음. 
                one_number += 1   
            else:
                if one_number == K:   # 세로로 카운팅해서 조건을 만족하면 puzzle_num 숫자를 1 증가시킴
                    puzzle_num += 1
                one_number = 0

        if one_number == K:   # 하나의 row 가 종료되었을 때 조건을 만족하면 puzzle_num을 1 증가
            puzzle_num += 1

    print(f"#{i} {puzzle_num}")

