# 26. 10. 29.
# SWEA 5658. 보물상자 비밀번호
# 30분 PASS

"""
목표: 각 변에 16진수 숫자들이 적혀있는 보물상자가 있다.
    1. 시계방향으로 회전시켜 숫자들을 한 칸씩 회전시킬 수 있다.
    2. 회전하며 만들 수 있는 숫자들 중 10번째로 큰 수를 10진수로 만든 수를 구하라
상태:
자료구조:
핵심로직:
    1. 몇 번을 돌리면 0회전과 동일한 값이 나올까? 
        1. 각 변마다 part_4 = N // 4 개씩 숫자가 들어간다.
        2. part_4 번 돌리면 0회전과 동일한 값이 나온다.
        3. 그러니, (part_4 - 1)번까지 돌리면 된다.
    2. 회전시키는 방법은 간단하다.
    3. for _ in range(part_4):
        1. first = number_16.pop()
        2. number_16 = [first] + number_16
        3. for i in range(4):
            total.add(number_16[part_4 * i:part_4 + part_4 * i])
    4. 16진수 문자열을 10진수 숫자로 형변환하고 정렬한 후 [K - 1]번쨰 숫자를 출력
종료조건: 반복문이 종료되면 [K -1]번째 숫자를 출력
시간복잡도:
"""

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    number_16 = list(input())

    part_4 = N // 4
    total = set()

    for _ in range(part_4):
        first = number_16.pop()
        number_16 = [first] + number_16

        for i in range(4):
            total.add(''.join(number_16[part_4 * i:part_4 *(i + 1)]))

    sort_total = sorted(total, reverse=True)

    result = int(sort_total[K - 1], 16)
    print(f'#{tc} {result}')