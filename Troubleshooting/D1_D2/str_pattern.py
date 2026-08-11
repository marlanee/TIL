T = int(input())   # 전체 테스트 케이스의 개수 T를 받는 코드 정의, range문제 쓰려고 정수로 형변환

for i in range(1, T + 1):
    test_str = input().strip()

    for x in range(1, len(test_str) + 1):
        y = len(test_str) // x
        # 문자열의 전체 길이를 x로 나눈 몫을 y라고 하면, test_str[:x] * y == test_str[:x * y]가 되어야 한다.
        if test_str[:x] == test_str[x:(x * 2)] and test_str[:x] * y == test_str[:(x * y)]:   # 이것만으로는 불충분하다. asasd를 못 막는다.
            print(f'#{i} {x}')
            break   # 멈추지 않으면, 마디의 길이마다 계속해서 출력하게 된다.     