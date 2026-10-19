# SWEA 5644. 무선 충전
# 10. 16. 1차 시도: 15:24

"""
목표: 10 x 10 지도에 A개의 BC가 주어진다.
    1. 두 사람(1, 1)(10, 10)이 주어진 동선으로 이동한다.
    2. 이동하며 BC의 범위 안에 들어가면 P만큼 충전된다.
        1. 두 사람이 동시에 같은 BC를 선택하면 p // 2만큼 각각 충전된다
        2. 범위는 맨해튼 거리로 주어진다.
    3. M 시간이 지난 후 두 사람의 총 충전량을 구하라
상태: 
    1. BC의 P만 담아놓는 power 리스트 생성
    2. BC들의 범위를 담아놓는 BC_range 생성
        1. 
자료구조: 델타 탐색
핵심로직:
    0. A_total, B_total에 가장 큰 P를 담고 시작
    1. M 시간만큼 반복 for m in range(M):
    2. A, B 둘 다 다음 칸으로 이동
    3. 다음 칸에서 가장 강력한 P를 total에 더함
종료조건: 반복문이 종료되면 A_total + B_total을 출력
시간복잡도:
"""
def cal(ar, ac, br, bc):
    global total_A, total_B

    choice_A = []
    choice_B = []

    for a in range(A):
        if (ar, ac) in BC_range[a]:
            choice_A.append((powers[a], a))
        if (br, bc) in BC_range[a]:
            choice_B.append((powers[a], a))

    choice_A.sort(reverse=True)
    choice_B.sort(reverse=True)

    if choice_A and choice_B:
        if choice_A[0] == choice_B[0]:
            if choice_A[1][1] >= choice_B[0][1]:
                total_A += choice_A[0][1]
                total_B += choice_B[0][0]
        else:
            total_A += choice_A[0][0]
            total_B += choice_B[0][0]
    elif choice_A:
        total_A += choice_A[0][0]
    elif choice_B:
        total_B += choice_B[0][0]


dr = [0, -1, 0, 1, 0]
dc = [0, 0, 1, 0, -1]

T = int(input())
for tc in range(1, T + 1):
    M, A = map(int, input().split())
    person_A = list(map(int, input().split()))
    person_B = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(A)]

    powers = [BC[i][3] for i in range(A)]  # P 만 담아놓는 리스트

    BC_range = [set() for _ in range(A)]

    for bc in range(A): # BC들의 범위를 담아놓는 코드
        row, col, bc_range, _ = BC[bc]

        for r in range(10):
            for c in range(10):
                if abs(row - r) + abs(col - c) <= bc_range:
                    BC_range[bc].add((r, c))
    
    total_A = 0
    total_B = 0

    ar, ac = 1, 1
    br, bc = 10, 10
    for m in range(M):
        ar = ar + dr[person_A[m]]
        ac = ac + dc[person_A[m]]
        br = br + dr[person_B[m]]
        bc = bc + dc[person_B[m]]

        cal(ar, ac, br, bc)

    print(f'#{tc} {total_B + total_A}')