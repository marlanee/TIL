# SWEA 4873 반복문자 지우기
# 1차 시도: 01:00

# 1. 목표: 한 문자열에서, 두 번 연속 반복되는 문자를 지운다. 반복 문자가 없어질 때까지 반복한 후 문자열의 길이를 구한다.
# 2. 상태: new_words = [] 로 새로운 문자열을 받는다.
# 3. 자료구조: Stack
# 4. 핵심로직
  1. words = list(input())
  2. for i in range(len(words) - 1):
      if words[i] != words[i + 1]:
        new_words.append(words[i])
