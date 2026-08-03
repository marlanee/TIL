def solution(genres, plays):
    total_genres = {}   # 장르들의 총 재생횟수를 담는 딕셔너리 생성
    total_plays = {}    # 노래들의 재생횟수와 index를 담는 딕셔너리 생성

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        total_genres[g] = total_genres.get(g, 0) + p   # 장르들의 총 재생횟수를 딕셔너리로 다 담았다.

    # 이제, 그 딕셔너리를 정렬하자. value 내림차순으로.
    songs = sorted(total_genres.keys(), key=lambda x : total_genres[x], reverse=True)    # 만들어졌다. 그 녀석이. 리스트로 말이다.

    # 이제 total_plays를 담아보자.
    for i in range(len(genres)):
        g = genres[i]   # 변수는 새로 지정해야 한다.
        p = plays[i]
        total_plays.setdefault(g, [])
        total_plays[g].append((p, i))

    # 이제 total_plays를 정렬하자. 장르별로, 재생순서는 내림차순으로, 인덱스는 오름차순으로
    for z in songs:
        song_plays = sorted(total_plays[z], key=lambda y : (-y[0], y[1]))   # [[(300, 1,)(200, 2)], [(300, 1), (200, 2)]]

    answer = []
    for song in song_plays[:2]:
        return answer.append(song)


    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))


            
