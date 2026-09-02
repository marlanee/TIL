# 전기 버스. 풀이 시간: 16:45

# 1. 목표: 최소한의 충전 횟수로 목적지에 도달하고, 충전 회수를 구하는 것
# 2. 구조: 
    # 1. 버스의 위치를 l로 설정
    # 2. l + K < 충전기 거리일 경우 0 출력
    # 3. l + K 거리 안에 충전기가 여러개 일 경우 l + K 내의 가장 큰 충전기로 이동
    # 4. l + K >= N 일 경우 종료
# 3. 종료: l + K >= N 일 경우.

T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split()) # K는 최대 이동 거리, N은 정류장의 개수, M은 충전기의 개수
    stations = list(map(int, input().split()))  # 충전기의 위치 stations의 약자

    l = 0   # 버스의 출발 위치

    for i in range(M):  # 충전기를 둘러볼 것이다.
        if l + K < stations[i]: # 첫 출발시 충전기가 더 멀면 0 출력
            print(f'{tc} 0')
        else:
            for s in stations:
                max_s = s
                

        


