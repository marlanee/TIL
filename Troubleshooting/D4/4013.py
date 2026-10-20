# SWEA 4013. 특이한 자석
# 1차 시도: FAIL(1시간) -> 힌트 딱 하나 보고 바로 PASS
# 10. 20. 복습 필요
# SWEA 4013. 특이한 자석
# 10. 20. 1차 복습: PASS(50분)
# 졸업

"""
목표: 8개의 날을 가진 4개의 자석이 주어짐
    1. 4개 중 임의의 자석을 (시계 or 반시계) 방향으로 회전시킴
    2. 회전한 자석과 인접한 자석이 반대 자성일 경우 인접한 자석은 반대 방향으로 회전함
    3. 모든 회전이 끝난 후 화살표 위치에 있는 자성에 따라 점수를 계산하고 총합을 구하라
상태: 
    1. total = 점수의 총합
자료구조: 따로 필요하지 않음
핵심 로직:
    1. cmd를 순회, 해당 자석을 회전시킴
    2. 인접한 자석들의 날이 해당 자석의 날과 반대인지 확인
    3. 반대라면, 반대 방향으로 회전시킴
    4. 연쇄 회전한 자석과 인접한 자석의 날을 체크 후 회전 또는 미회전
종료 조건: 
    1. cmd 순회가 종료되었을 때.
    2. for row in grid: / row[0] 을 확인해서 점수 계산 후 총합 출력
시간 복잡도: O(K)
"""

def spin_magnet(target, spin):

    if spin == 1:   # 시계방향의 경우 / 회전
        q = grid[target][-1]
        grid[target][1:8] = grid[target][:7]
        grid[target][0] = q
        return
    else:   # 반시계 방향의 경우
        q = grid[target][0]
        grid[target][:7] = grid[target][1:8]
        grid[target][-1] = q
        return

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    grid = [list(map(int, input().split())) for _ in range(4)]
    cmd = []

    for _ in range(K):  # 코드 작성을 쉽게 하기 위해 번호를 1씩 빼서 저장함
        magnet, spin = map(int, input().split())
        cmd.append((magnet - 1, spin))

    for magnet, d in cmd:
        spin_magnet(magnet, d)  # 회전

        # 이제 양 옆에 자석이 있는지 확인한 후, 조건에 따라 회전시켜야 한다.
        # 우선 왼쪽 확인
        left_idx = magnet
        left_d = d
        while left_idx - 1 >= 0:
            if grid[left_idx][6 + left_d] != grid[left_idx - 1][2]:
                spin_magnet(left_idx - 1, -left_d)
            else:
                break

            left_idx -= 1
            left_d = -left_d

        right_idx = magnet
        right_d = d
        while right_idx + 1 < 4:
            if grid[right_idx][2 + right_d] != grid[right_idx + 1][6]:
                spin_magnet(right_idx + 1, -right_d)
            else:
                break

            right_idx += 1
            right_d = -right_d

    count = 1
    total = 0

    for row in grid:
        if row[0] == 1:
            total += count
        count *= 2

    print(f'#{tc} {total}')
    
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