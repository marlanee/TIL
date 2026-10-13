# SWEA 4013. 특이한 자석
# 1차 시도: FAIL(1시간) -> 힌트 딱 하나 보고 바로 PASS
# 10. 20. 복습 필요

"""
목표: 
    1. 8개의 날을 가진 4개의 자석이 주어진다
    2. 자석을 K번 회전시킨 후 날의 정보에 따라 점수의 총합을 구하라
    3. 1개의 자석이 회전할 떄, 양 옆의 자석도 같이 회전한다
    4. 양 옆의 자석이 극(2, 6)이 다르면 양 옆 자석은 반대 방향으로 1칸 회전한다
    5. 극이 같다면 양 옆 자석은 회전하지 않는다.
    6. 0번 index가 점수를 계산하는 지점이며, S극(1)일때만 점수를 획득한다
    7. 자석별로 1번: 1점, 2번: 2점, 3번: 4점, 4번: 8점이다
상태: m = 회전하는 자석, d = 회전 방향, magnets[m][0] = 화살표에 위치한 날
자료구조: 시뮬레이션?
핵심로직:
    1. 자석을 기준으로 왼쪽과 오른쪽을 나눠서 회전시키자
    2. cmd를 순회한다.
        1. for m, d in cmd:
    3. 일단 d 방향으로 m에 해당하는 자석을 회전시킨다. / 리스트 슬라이싱 활용
    3-1. d = - d # 양 옆은 반시계로 돌아야 하므로
    4. i = 1 / while m - i >= 0 # 왼쪽 방향 확인. 왼쪽에 자석이 있을 경우에만 실행됨
    5. if magnets[m][2 - d] != magnets[m - i][2] # 극이 다르면
    6. m - 1번 자석을 d 방향으로 회전
    7. i += 1
종료조건: for문이 종료되었을 때 magnets[][0]으로 총합 점수 계산
시간복잡도: 코드 작성 후 계산
"""

def rotation(magnet, d):
    if d == 1:
        p = magnets[magnet][-1]   # 마지막 날을 임시 저장
        magnets[magnet][1:] = magnets[magnet][:7] # 시계방향으로 한 칸 회전
        magnets[magnet][0] = p
    else:
        p = magnets[magnet][0]   # 첫번째 날 임시 저장
        magnets[magnet][:7] = magnets[magnet][1:] # 반시계 방향으로 한 칸 회전
        magnets[magnet][-1] = p

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    cmd = []
    for i in range(K):
        m, d = map(int, input().split())
        cmd.append((m - 1, d))

    for m, d in cmd:
        rotation(m, d)

        origin_d = d

        d = - d
        origin_m = m

        while m - 1 >= 0:   # 왼쪽 자석 회전
            if magnets[m][6 - d] == magnets[m - 1][2]:
                break

            rotation(m - 1, d)

            d = - d
            m -= 1

        d = - origin_d
        m = origin_m

        while m + 1 <= 3:
            if magnets[m][2 - d] == magnets[m + 1][6]:
                break

            rotation(m + 1, d)

            d = - d
            m += 1

    result = 0
    count = 1

    for i in range(4):
        if magnets[i][0] == 1:
            result += count
        count *= 2

    print(f'#{tc} {result}')