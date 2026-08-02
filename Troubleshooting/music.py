def solution(genres, plays):
    find_num_genres = {}
    for i in genres:   # 딕셔너리에 장르별로 항목을 추가함
        find_num_genres.setdefault(i, 0)
    for x in range(len(plays)):   # 딕셔너리의 장르들에 재생 횟수를 추가함
        find_num_genres[genres[x]] += plays[x]
    
    
    

# 문제 요구사항: 장르별로 노래 2개씩 선정해서, 그 노래의 index를 반환한다.
# 가장 많이 재생된 장르의 노래 2개부터 가장 적게 재생된 장르의 노래 2개까지 결과에 반영해야함.
# 일단, 장르의 재생 순위부터 찾자.

def solution(genres, plays):
    genre_total = {}  # 장르별 총 재생 횟수
    genre_songs = {}  # 장르별 곡 정보 [(재생 횟수, 고유 번호), ...]

    # Step 1: 데이터 수집
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]

        # 장르별 총 재생 횟수 누적
        genre_total[g] = genre_total.get(g, 0) + p   # get으로 초기값 0으로 설정, 이후 p만큼 계속 더함

        # 장르별 곡 정보 추가
        if g not in genre_songs:
            genre_songs[g] = []
        genre_songs[g].append((p, i))

    # Step 2: 총 재생 횟수가 많은 장르 순서로 정렬
    sorted_genres = sorted(
        genre_total.keys(), key=lambda g: genre_total[g], reverse=True
    )

    answer = []

    # Step 3: 장르 순서대로 가장 많이 재생된 곡 최대 2개 추출
    for g in sorted_genres:
        # 재생 횟수(x[0])는 내림차순(-), 고유 번호(x[1])는 오름차순(+) 정렬
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))

        # 곡이 1개만 있을 수도 있으므로 슬라이싱[:2] 사용
        for song in songs[:2]:
            answer.append(song[1])

    return answer
        