# 2026.08.10. 1차 시도: 실패
T = int(input())

for i in range(1, T + 1):
    pd = int(input())
    pn = list(map(int, input().strip().split()))

    profit = 0
    max_price = 0

    for price in reversed(pn):
        if price > max_price:
            max_price = price
        else:
            profit = profit + (max_price - price)
    print(f'#{i} {profit}')
        

'''
T = int(input())

for i in range(1, T + 1):
    pd = int(input())
    pn = list(map(int, input().strip().split()))

    # 최대 이익을 출력하는 알고리즘 작성 필요
    # 어떤 알고리즘을 구현해야할까?
    # 전부 매입하다가 더 낮은 금액이 나오면 전량 매도하는 방법? / 허점은? 다음 금액이 없을 때
    # 폐기
    # 가장 큰 수와 그 수의 인덱스 번호를 찾고 그 앞의 모든 물건을 매수한 후 그 가격에 판매
    # 그리고 또 반복.
    buy_list = []
    profit = 0

    max_index = pn.index(max(pn))
    past_max = 0
    while past_max < pd-1:
        for y in range(past_max, max_index):
            buy_list.append(pn[y])
        profit = profit + (len(buy_list) * max(pn[past_max:])) - sum(buy_list)
        past_max = max_index + 1
        if past_max >= pd - 1:
            break
        max_index = pn.index(max(pn[past_max:]))
        buy_list = []

    print(f"#{i} {profit}")
'''