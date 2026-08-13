# 26-08-13. 1차 시도: PASS (30분 소요)
# 암호를 생성해야 하는 문제임.
# 8개의 수를 갖고, 0이 될때까지 만들어야함
# 그 후 암호를 반환해야함
# for i in range(1, 2):
#     _ = int(input())
#     num_list = list(map(int, input().strip().split()))
#     #앞에 있는 숫자의 번호를 1 줄이고 뒤로 보내야 한다.
#     cn = [1, 2, 3, 4, 5]
#     x = 0
#     while 0 not in num_list:
#         num_list[0] = num_list[0] - cn[x]
#         calculated_num = num_list.pop(0)
#         num_list.append(calculated_num)
#         if num_list[7] <= 0:
#             num_list[7] = 0
#             break
#         x = (x + 1) % 5

#     print(f'#{i}', *num_list)


# 다 풀었다. Gemini가 잘했다고 칭찬해줬다. 
# 그런데 더 좋은 방법이 있다고 한다. 하.

# 아래는 gemini의 풀이 방식이다.
from collections import deque   # 양방향 큐인 deque를 사용한다.

for i in range(1, 11):
    _ = int(input())

    queue = deque(map(int, input().split())) # 리스트가 아니라 deque를 쓰네? 뭐가 queue에 저장되지? 얘 type은 뭐지?

    sub = 1

    while True:
        val = queue.popleft - sub   # pop(0)메서드와 동일하다. 다만 훨씬 빠르다.

        if val <= 0:
            queue.append(0)
            break

        queue.append(val)

        sub = (sub % 5) + 1

    print(f'#{i}, *queue')   # 이렇게 하면 리스트가 다 언패킹되어 토해진다고 한다.