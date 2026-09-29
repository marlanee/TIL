# Baby-gin game

# 목표: 6자리 숫자가 Baby-gin인지 검사하라
# 상태: number = 정렬된 숫자


T = int(input())
for tc in range(1, T + 1):
    number = list(map(int, input()))

    count = [0] * 10

    for i in number:
        count[i] += 1

    baby_gin = 0

    for i in range(10):
        while count[i] >= 3:
            count[i] -= 3
            baby_gin += 1

    for i in range(8):
        while count[i] >= 1 and count[i + 1] >= 1 and count[i + 2] >= 1:
            count[i] -= 1
            count[i + 1] -= 1
            count[i + 2] -= 1
            baby_gin += 1

    if baby_gin == 2:
        result = True
    else:
        result = False

    print(f'#{tc} {result}')