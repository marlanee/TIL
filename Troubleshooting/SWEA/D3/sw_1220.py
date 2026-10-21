# 2026-08-20. 1차 시도: 09:03
# Magnetic 마마마 마그네틱. 
# 내가 진짜 D3 양학할 정도로 성장한다. 두고 봐라.

# for tc in range(1, 11):
#     N = int(input())
    # 1은 N극이다. 2는 S극이다.
    # 1은 한 단계마다 column - 1, 2는 column + 1 로 이동한다.
    # 그러나, 올라가야 하는 칸이 0이 아닌 경우 올라갈 수 없다.
    # N - 1칸에 도달한 1이나 0칸에 도달한 2는 다음 단계에 사라진다.
    # 하지만, 단계별로 진행할 필요성이 있을까?
    # 간단하게 행을 하나씩 뜯어보자.
    # 1이 있을 때, 2가 아래에 있을 경우 count + 1 아닌가? 
    # 즉, 1을 찾고 2가 아래에 있는지 판별하면 되는 것 아닌가.
    # 2는 찾을 필요가 없다. 어차피 2가 교착 상태에 빠지는 경우는 1이 있을 경우에만 발생하기 때문이다.
    # 좌, 우로 N/S극을 두면 너무 쉬울까봐 위 아래로 둔건가? 의심이 든다.
    # 그럼 내가 짜야할 코드는 다음과 같다.
    # 행에 1이 있을 때, 아래에 2가 있는지 찾는 코드
    # 그 2 밑에 또 1이 있는지 찾고 또 아래에 2가 있는지 찾는 코드
    # 이것을 행이 끝날때까지 반복한다.
    # grid = [list(map(int, input().split())) for _ in range(N)]   # 행렬을 만들기 위해 리스트 컴프리헨션을 사용했다.
    # count = 0   # 누적 교착상태의 개수
    # for r in range(N):   # 행을 하나씩 검사할거다. 행에 있는 교착상태 검사.
    #     column_list = [grid[c][r] for c in range(N)]
    #     if sum(column_list) <= 2:
    #         continue
    #     for s in range(len(column_list) - 1):
    #         sl = column_list[s + 1:]
    #         if column_list[s] == 1:
    #             if 2 in sl and 1 not in sl:
    #                 count += 1
    #                 break
    #             elif 2 not in sl:
    #                 break
    #             if sl.index(2) < sl.index(1):   # 조건문 아닌가? 왜 2가 없을 때 오류뜨지? index 메서드의 특징인가?
    #                 count += 1

    # print(f'#{tc} {count}')

    # 결과가 나오긴 하는데, 작게 나온다? 어떤 케이스를 빼먹은거지?
    # 2만 남았을 때를 빼먹었었다. 코드 수정했음

# Gemini 짜증난다. 내 코드를 잘못 리뷰했다. 요즘 신뢰하고 있었는데 뒤통수를 맞은 느낌
# 일단, 아래는 gemini의 코드다. 잘 돌아간다.

for tc in range(1, 11):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    deadlocks = 0

    for col in range(N):
        has_n = False
        for row in range(N):
            val = grid[row][col]
            if val == 1:
                has_n = True
            elif val == 2 and has_n:   # 대박이다. 1을 만나면 상태를 True로 저장해두는 거구나.
                deadlocks += 1
                has_n = False

    print(f'#{tc} {deadlocks}')