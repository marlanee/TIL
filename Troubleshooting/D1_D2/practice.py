T = int(input())

for i in range(1, T + 1):
    pd = int(input())
    pn = list(map(int, input().strip().split()))

    total_profit = 0
    max_number = 0
    # 역순으로 순회하며 차액만큼 이득을 보는 코드 작성
    for x in reversed(pn):
        if x > max_number:
            max_number = x
        else:
            total_profit += max_number - x

    print(f'#{i} {total_profit}')
