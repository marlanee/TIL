import re   # 드디어 쓰는 모듈! 소문자와 숫자, 정해진 특문이 아닌 모든 것들을 제거하는 강력한 클래스다.

def solution(new_id):
    # 1단계
    first_id = new_id.lower()
    # 2단계
    second_id = re.sub(r'[^a-z0-9-._]', '', first_id)   # re 클래스의 sub 메서드로 다 처리해버렸다. 위대하다. 멋있다.
    # 3단계
    third_id = second_id.replace('..', '.')
    # 4단계 
    if third_id[0] != '.' and third_id[-1] != '.':
        fourth_id = third_id
    elif third_id[0] == '.':
        fourth_id = third_id[1:]
    else:
        fourth_id = third_id[:-1]
