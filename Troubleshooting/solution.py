# 261118. 광고 삽입
# 1차 시도: 10:09

"""
목표: logs에 사용자들의 시청 기록이 주어진다
    1. 시청 기록이 가장 오래 겹치는 구간에 adv_time을 배치하여 광고를 오래 시청하게 만들어라.
    2. play_time은 동영상의 전체 길이이다.
    3. 광고를 최대 시청 시간으로 만드는 시작 시각을 반환하라
    4. 만약 광고 최대 시청 시간이 동일할 경우, 가장 빠른 시작 시각을 반환하라
핵심로직:
    1. 시, 분, 초를 초 단위로 변환하자. / 데이터 사용의 편리성을 올려주기 위함이다.
    2. play_time 길이 만큼의 리스트를 만들어서 [0] * len(play_time) + 1각 사용자 구간별로 1씩 더한다?
    3. 반복문으로 리스트를 순회하며 adv_time 만큼의 길이를 슬라이싱해서 최대 합을 구한다? 최대값일 경우 시작점을 갱신한다? 같으면 저장 안하고?
    4. 이거 너무 시간복잡도가 높지 않나? logs 길이 30만에, play_time 길이 36만? 합연산이라 괜찮으려나?
"""

def solution(play_time, adv_time, logs):
    def to_seconds(time):
        h, m, s = map(int, time.split(':'))
        return h * 3600 + m * 60 + s

    s_play_time = to_seconds(play_time)
    find_user = [0] * (s_play_time + 1)

    for user_log in logs:
        start, end = user_log.split('-')
        s_start = to_seconds(start)
        s_end = to_seconds(end)

        find_user[s_start] += 1
        find_user[s_end] -= 1

    for i in range(1, s_play_time + 1):
        find_user[i] += find_user[i - 1]

    s_adv_time = to_seconds(adv_time)
    s_answer = 0
    total = current = sum(find_user[:s_adv_time])

    for i in range(s_adv_time, s_play_time):
        current -= find_user[i - s_adv_time]
        current += find_user[i]
        if current > total:
            total = current
            s_answer = i - s_adv_time + 1

    h, remainder = divmod(s_answer, 3600)
    m, s = divmod(remainder, 60)

    answer = f'{h:02d}:{m:02d}:{s:02d}' # 정수를 최소 두 자리로 표현하는 기능! 대단하다.

    return answer