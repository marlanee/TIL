"""
풀이시간: 14:40
목표: 문자열이 담긴 리스트가 주어진다.
    1. 모든 문자열에 대해서, 1 ~ N까지의 문자열이 접두어로 포함된 문자열이 있는지 판별하라.
상태: set_book = 세트로 형변환한 원래 리스트
자료구조: set
핵심로직:
    Bad case: 리스트를 이중 순회하며 문자열 n이 자신을 제외한 모든 문자열에 포함되어있는지 확인 / 일단 해보자 시간복잡도: O(N^2)
    ! Better case: 리스트를 세트로 변환. 리스트를 순회하며 문자열 길이까지 순회. 그 문자열이 세트 안에 있는지 판별
종료조건: 반복문이 종료되거나 포함된 문자열이 있을 때
시간 복잡도: O(N)
"""

'''
# Bad case
def solution(phone_book):
    for idx, n in enumerate(phone_book):
        for next_idx, next_n in enumerate(phone_book):
            if len(n) >= len(next_n):
                continue
            if n == next_n[:len(n)]:
                return False
    answer = True
    return answer
'''

# Better case
def solution(phone_book):
    set_book = set(phone_book)
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in set_book:
                return False
            
    return True