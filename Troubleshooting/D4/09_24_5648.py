# 원자 소멸 시뮬레이션. 1차 시도: FAIL
# 복습. PASS(1시간) / 자소서 동시에 쓰느라 좀 늦음
# 09.24. 2차 복습 마지막? 

# 주석부터 읽고 복습할 것
# 우와! 원자 소멸 시뮬레이션!!!!

# 1. 목표: 원자들을 동시에 이동시키면서 충돌할 때 방출되는 에너지 총합 계산
# 2. 상태:
    # 1. atoms: 현재 살아있는 원자 [x, y, d, K]
    # 2. total: 지금까지 충돌로 방출된 에너지
# 3. 자료구조
    # 1. field 딕셔너리
    # 2. key = 이동 후 좌표 (x, y)
    # 3. value = 해당 좌표에 도착한 원자 리스트
# 4. 핵심로직
    # 1. 0.5초 충돌을 처리하기 위해 모든 좌표를 2배
    # 2. 모든 원자를 한 칸 이동
    # 3. 범위를 벗어난 원자는 제거
    # 4. 이동한 좌표별로 field에 원자를 묶음
    # 5. 같은 좌표에 1개면 생존
    # 6. 2개 이상이면 에너지를 더하고 모두 소멸
# 5. 종료 조건: 살아있는 원자가 하나도 없을 때

# dx = [0, 0, -1, 1]
# dy = [1, -1, 0, 0]

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     atoms = []
#     for _ in range(N):
#         x, y, d, K = map(int, input().split())
#         atoms.append([x * 2, y * 2, d, K])

#     total = 0

#     while atoms:
#         field = {}
#         for atom in atoms:
#             x, y, d, K = atom
#             nx = x + dx[d]
#             ny = y + dy[d]
#             atom[0], atom[1] = nx, ny

#             if not (-2000 <= nx <= 2000 and -2000 <= ny <= 2000):
#                 continue

#             field.setdefault((nx, ny), [])
#             field[(nx, ny)].append([nx, ny, d, K])

#         alive_atoms = []

#         for position, value in field.items(): # 순회 중인 리스트에서 원소를 제거하지 말자.
#             if len(value) == 1:
#                 alive_atoms.append(value[0])
#             elif len(value) >= 2:
#                 for x, y, d, K in value:
#                     total += K

#         atoms = alive_atoms   

#     print(f'#{tc} {total}')

# SWEA 5648. 원자 소멸 시뮬레이션

# 복습. PASS(1시간) / 자소서 동시에 쓰느라 좀 늦음

# 목표: 모든 원자를 동시에 이동시키며 충돌하는 원자들의 에너지 합을 계산
# 상태: atoms = 원자들의 좌표와 d, K를 담은 리스트. total = 방출된 누적 에너지
# 자료구조: dictionary / key = 이동 후 좌표 (x, y) / value = 해당 좌표로 이동한 원자들
# 핵심 로직: 동기식 시뮬레이션 + 좌표 스케일링 + 해시맵 기반 충돌 그룹화
    # 1. 0.5초 충돌 처리를 위해 좌표 2배 확대
    # 2. 살아 있는 모든 원자를 동시에 한 칸 이동
    # 3. 범위를 벗어난 원자는 제거
    # 4. 이동 후 좌표를 dictionary로 그룹화
    # 5. 한 좌표에 원자가 1개면 생존
    # 6. 2개 이상이면 모두 소멸시키고 K를 total에 합산
    # 7. 생존한 원자로 다음 시뮬레이션 진행
# 종료 조건: 모든 원자들이 좌표에서 사라지면 종료

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    atoms = []
    total = 0

    for _ in range(N):
        x, y, d, K = map(int, input().split())
        x = x * 2
        y = y * 2
        atoms.append([x, y, d, K])

    while atoms:
        current_atoms = []
        location = {}
        for x, y, d, K in atoms:
            nx = x + dx[d]
            ny = y + dy[d]

            if -2000 <= nx <= 2000 and -2000 <= ny <= 2000:
                x, y = nx, ny
                location.setdefault((x, y), [])
                location[(x, y)].append([x, y, d, K])
            else:
                continue

        for value in location.values():
            if len(value) == 1:
                current_atoms.append(value[0])
            else:
                for x, y, d, K in value:
                    total += K

        atoms = current_atoms

    print(f'#{tc} {total}')