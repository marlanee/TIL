# 2026-08-26. 1차 시도: PASS(50분)

# 지정된 인덱스에 명령어의 숫자들을 집어넣으면 되는 문제
# 명령어는 'I'로 구분된다.
# insert함수로 원하는 위치에 추가는 가능할 듯
# 우선 원본 암호문은 list 문자열로 받자.
# 명령어도 list 문자열로 받자
# for문으로 명령어를 순회하면서, I를 만나면 i + 1 의 index에 [i + 3 : i + 3 + 5]을 통째로 삽입

for tc in range(1, 11):
    _ = input()
    password = list(input().split())
    _ = input()
    order = list(input().split())

    for i, o in enumerate(order):
        if o == 'I':
            idx = int(order[i + 1])
            idn = int(order[i + 2])
            for t in range(idn):
                password.insert(idx + t, order[i + 3 + t])
    
    print(f"#{tc} {' '.join(password[:10])}")