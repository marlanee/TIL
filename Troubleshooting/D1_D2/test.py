''' 1P-3 문자열 심화
password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.
first_char = password[28:36]
second_word = password[113:118]
# third_word = password[66:69:-1]   # 이런식으로 하면 안된다. 66에서 출발해서 역순으로 가게 된다.
# fourth_word = password[322:326:-1]   # 마찬가지다. 
third_word = password[66:69][::-1]   # 일단 슬라이싱을 한 후 뒤집어라.
fourth_word = password[322:326][::-1]
fifth_word = password[365:371]

print(f'{first_char}{second_word} {third_word} {fourth_word} "{fifth_word}".')
'''
# 피드백
# 오만했다. 고작 기초 문법이라고 생각했다. 
# third_word, fourth_word 에 해당하는 문자열을 순서대로 슬라이싱 한 뒤 역으로 세면 될 줄 알았다.
# 그러나 그런 식으로 작동하지 않았다. 첫 숫자의 문자열부터 숫자가 감소하며 슬라이싱 하는 것이었다.
# 그러니 해법은, third_word[68:65:-1] 또는 third_word[66:69][::-1] 이었다.
# D2 문제 3문제 풀었다고 까불지 마라. 기본에 충실해라. 부실 공사는 안된다.

# print(list(set(authors)))   # set 함수로 형변환이 가능하다. / set, list의 형변환 과정은 괄호가 바뀐다.

