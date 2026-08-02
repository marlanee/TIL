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
        if g not in genre_songs:   # genre_songs에 딕셔너리 요소 추가. 
            genre_songs[g] = []
        genre_songs[g].append((p, i))   # 추가한 딕셔너리 요소에 재생 횟수와 인덱스 번호 추가 / 인덱스 번호를 왜 추가하지? 언제 써먹을까?
        # 자세히 보니 튜플로 저장했네? 그럼 지금 genre_songs = {'classic' : [(200, 1), (300, 4)]} 이런 식이겠군

    # Step 2: 총 재생 횟수가 많은 장르 순서로 정렬
    sorted_genres = sorted(
        genre_total.keys(), key=lambda g: genre_total[g], reverse=True
    )   # lambda 함수 선언을 알아야 한다. 어떤 순서로 작동하는걸까? / 일단, 재생 횟수가 많은 장르 순서로 정렬했다고 치자. 
    # 이런 식이려나? sorted_genres = {'classic' : 57000, 'pop' : 52000} 이렇게 내림차순으로.
    # 아니 그런데, value를 기준으로 정렬해야 되는거 아닌가? 왜 genre_total.keys()가 붙어있을까?
    # sorted() 함수의 반환값은 반드시 리스트라고 한다.

    answer = []

    # Step 3: 장르 순서대로 가장 많이 재생된 곡 최대 2개 추출
    for g in sorted_genres:   # 재생 횟수가 가장 많은 장르의 value를 g라는 변수에 담는 코드다. -> 아니다. ['pop', 'classic'] 식의 리스트다.
        # 재생 횟수(x[0])는 내림차순(-), 고유 번호(x[1])는 오름차순(+) 정렬
        songs = sorted(genre_songs[g], key=lambda x: (-x[0], x[1]))   # -x[0]을 1순위로 정렬하고, 2순위로 x[1]을 정렬한다고 한다.
        # 뭐지? 튜플로 이루어진 genre_songs[value] ? 이게 뭐지? key=lambda는 무슨 뜻이야?

        # 곡이 1개만 있을 수도 있으므로 슬라이싱[:2] 사용
        for song in songs[:2]:   # 뭐지? 어차피 곡이 1개든 2개든 슬라이싱[:2]를 해야 2개까지 뽑아내는거 아닌가?
            answer.append(song[1])   # songs[1]이 없을 때 직접 answer에 append 하면 IndexError가 뜬다고 한다. 그래서 직접 입력이 아닌 슬라이싱이다.

    return answer