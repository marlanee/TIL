def solution(genres, plays):
    total_genres = {}   # 장르들의 총 재생횟수를 담는 딕셔너리 생성
    total_plays = {}    # 노래들의 재생횟수와 index를 담는 딕셔너리 생성

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        total_genres[g] = total_genres.get(g, 0) + p   # 장르들의 총 재생횟수를 딕셔너리로 다 담았다.

        

    