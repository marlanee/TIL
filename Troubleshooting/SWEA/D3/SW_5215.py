# 26-08-14 1차 시도:
# 햄버거 다이어트

# T = int(input())

# for i in range(1, T + 1):
#     N, L = map(int,input().split())
#     food_list = [list(map(int, input().split())) for _ in range(N)]

#     # 도대체 어떤 로직을 짜야되지?
#     # 효율순으로 담는다?
#     good_food = sorted(food_list, key=lambda x : (x[1] / x[0]))

#     total_cal = 0
#     total_score = 0
#     for score, cal in good_food:
#         total_cal += cal

#         if total_cal > L:
#             total_cal -= cal
#             continue
#         total_score += score

#     print(f'#{i}', total_score)

#     # Fail이래. 그래. 나도 안될거 알고 있었어. 그래도 20개 중 14개 맞췄대.

