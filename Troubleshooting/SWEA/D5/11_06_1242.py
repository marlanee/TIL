"""
26.11.03.
SWEA 1242. 암호코드 스캔
1차 시도: 1시간 30분. 힌트 작성 후 PASS
11. 06. 복습 필요

목표: 세로 2000 x 가로 500 이하의 크기를 가진 직사각형 배열이 주어진다.
    1. 배열은 16진수이며, 배열을 2진수로 변환하여 암호코드인지 확인해야 한다.
    2. 배열에는 1개 이상의 암호코드가 존재한다. 정상 암호들의 숫자들의 합을 출력하라
    3. 암호코드는 8개의 숫자로 구성되어 있다. (7개 고유번호 + 1개 검증코드)
    4. 각 숫자 하나가 차지하는 최소 칸수는 7개 비트로, 암호코드 하나의 최소 가로 길이는 56이다.
    5. 암호코드의 가로 길이는 56의 배수가 된다. 
상태:
자료구조: 
핵심로직:
    1. 16진수를 2진수로 변환
    1-2. 한 줄씩 체크해서 1이 없으면 패스함.
    2. 오른쪽부터 체크해서 1일 경우, 리스트가 4개 미만일 때까지 연속된 같은 숫자의 개수를 담음
    3. 가장 작은 숫자가 문자열의 배수임. / min_num
    4. 56 * min_num이 암호코드의 크기가 됨.
    5. 가장 오른쪽 1의 인덱스 + 1까지 반복문을 돌림. / for i in range(end_idx - 56 * min_num, end_idx + 1)
    6. 슬라이싱된 리스트를 stirp()으로 겉부분 0을 자르고 연속된 숫자의 개수를 리스트에 담음. 담을 때 min_num으로 나누기
    7. 딕셔너리의 10진수 암호로 변환.
    8. 암호코드가 유효한지 확인
한 암호코드의 최대 길이는 448. 한 숫자의 최대 길이는 56.
종료조건: 
시간복잡도:
"""

password = {
    (1, 1, 2) : 0,
    (1, 2, 2) : 1,
    (2, 2, 1) : 2,
    (1, 1, 4) : 3,
    (2, 3, 1) : 4,
    (1, 3, 2) : 5,
    (4, 1, 1) : 6,
    (2, 1, 3) : 7,
    (3, 1, 2) : 8,
    (2, 1, 1) : 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = []

    for _ in range(N):
        row_16 = input().strip()

        row_2 = ''.join(format(int(ch, 16), '04b') for ch in row_16)
        grid.append(row_2)

    find_password = []

    for row in grid:
        find_min_num = [0] * 3
        if '1' not in row:
            continue
        i = len(row) - 1
        while i >= 0:  # 1, 배율 찾기
            if not find_min_num[1] and row[i] == '1':
                find_min_num[0] += 1

            if not find_min_num[2] and find_min_num[0] and row[i] == '0':
                find_min_num[1] += 1

            if find_min_num[1] and row[i] == '1':
                find_min_num[2] += 1

            if all(find_min_num) and row[i] == '0':
                min_num = min(find_min_num)
                left_zero = 7 * min_num - sum(find_min_num)
                ratio = tuple(x // min_num for x in find_min_num)
                find_password.append(password[ratio])
                find_min_num = [0] * 3
                i -= left_zero
                continue

            i -= 1

    result = 0
    seen = set()

    for start in range(0, len(find_password), 8):
        code = find_password[start:start + 8][::-1]
        code_key = tuple(code)

        if code_key in seen:
            continue

        seen.add(code_key)

        total = code[-1]

        for j in range(7):
            if j % 2 == 0:
                total += code[j] * 3
            else:
                total += code[j]

        if total % 10 == 0:
            result += sum(code)

    print(f'#{tc} {result}')