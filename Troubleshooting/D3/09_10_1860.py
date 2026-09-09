# 진기의 최고급 붕어빵. 1차 시도: PASS(30분)
# 풀었으나, 개선점 많음.
# 9. 10. 복습 필요

# 1. 목표: 붕어빵의 개수가 사람의 수보다 적으면 Impossible, 많으면 possible을 출력. / 붕어빵의 개수가 사람보다 많은지 확인
# 2. 상태: t 변수로 시간을 관리, bread 변수로 붕어빵의 개수를 관리, people 변수로 사람 명수를 관리.
# 3. 자료구조: 사람 도착 시간을 people_list에 담아서 관리. while문으로 t <= max(people_list) 조건에서 반복
# 4. 핵심 로직: if t % M == 0:, bread += K / if t in people_list:, people += 1
# 5. 종료 조건: t > max(people_list)

# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     people_list = list(map(int, input().split()))

#     t = 1
#     bread = 0
#     people = 0
#     if 0 in people_list:
#         print(f'#{tc} Impossible')
#         continue

#     while t <= max(people_list):
#         if t in people_list:
#             people += people_list.count(t)
#         if t % M == 0:
#             bread += K
#         if people > bread:
#             print(f'#{tc} Impossible')
#             break
#         else:
#             bread = bread - people
#             people = 0
#         t += 1

#     if t > max(people_list):
#         print(f'#{tc} Possible')


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    people_list = sorted(map(int, input().split()))

    result = 'Possible'

    for i in range(N):
        time = people_list[i]

        bread = (time // M) * K

        if bread < i + 1:
            result = 'Impossible'
            break

    print(f'#{tc} {result}')

