# 26. 10. 27.
# SWEA 14596. [Pro] 섬 지키기
# 1차 시도: 10:00
from typing import List
from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
N = 0
mMap = []

def init(n:int, map_data:List[List[int]]) -> None:
    global N, mMap

    N = n
    mMap = [row[:n] for row in map_data[:n]]

    return

def numberOfCandidate(M:int, mStructure:List[int]) -> int:
    mStructure = mStructure[:M]
    count = 0

    if M == 1:
        return N * N

    reversed_structure = mStructure[::-1]

    for r in range(N):
        for c in range(N - M + 1):
            ground = mMap[r][c:c + M]

            if can_install(ground, mStructure) or can_install(ground, reversed_structure):
                count += 1

    for c in range(N):
        for r in range(N - M + 1):
            ground = []
            for i in range(M):
                ground.append(mMap[r + i][c])

            if can_install(ground, mStructure) or can_install(ground, reversed_structure):
                count += 1

    return count


def maxArea(M:int, mStructure:List[int], mSeaLevel:int) -> int:
    mStructure = mStructure[:M]
    answer = -1
    reversed_mStructure = mStructure[::-1]


    for r in range(N):
        for c in range(N - M + 1):
            ground = mMap[r][c:c + M]
            if can_install(ground, mStructure):
                for i in range(M):
                    mMap[r][c + i] += mStructure[i]

                current = count_flooded(mSeaLevel)
                result = N * N - current
                answer = max(answer, result)

                for i in range(M):
                    mMap[r][c + i] -= mStructure[i]

            elif can_install(ground, reversed_mStructure):
                for i in range(M):
                    mMap[r][c + i] += reversed_mStructure[i]

                current = count_flooded(mSeaLevel)
                result = N * N - current
                answer = max(answer, result)

                for i in range(M):
                    mMap[r][c + i] -= reversed_mStructure[i]

    for c in range(N):
        for r in range(N - M + 1):
            ground = []
            for m in range(M):
                ground.append(mMap[r + m][c])

            if can_install(ground, mStructure):
                for i in range(M):
                    mMap[r + i][c] += mStructure[i]

                current = count_flooded(mSeaLevel)
                result = N * N - current
                answer = max(answer, result)

                for i in range(M):
                    mMap[r + i][c] -= mStructure[i]

            elif can_install(ground, reversed_mStructure):
                for i in range(M):
                    mMap[r + i][c] += reversed_mStructure[i]

                current = count_flooded(mSeaLevel)
                result = N * N - current
                answer = max(answer, result)

                for i in range(M):
                    mMap[r + i][c] -= reversed_mStructure[i]

    return answer

def can_install(ground, structure):
    # ground: 연속된 M칸의 지형 높이
    # structure: 설치할 구조물의 높이
    M = len(structure)

    target = ground[0] + structure[0]

    for i in range(1, M):
        if ground[i] + structure[i] != target:
            return False

    return True

def count_flooded(mSeaLevel):
    q = deque()
    visited = [[False] * N for _ in range(N)]
    flooded = 0

    # 현재 지도에서 바닷물이 침범할 수 있는 칸의 개수
    # 반환: 침수된 칸의 수    

    # 1. 지도 테두리의 BFS 시작점 등록

    for i in range(N):
        if mMap[0][i] < mSeaLevel:  # 0번째 행
            if not visited[0][i]:
                visited[0][i] = True
                q.append((0, i))
                flooded += 1

        if mMap[N - 1][i] < mSeaLevel:  # 마지막 행
            if not visited[N - 1][i]:
                visited[N - 1][i] = True
                q.append((N - 1, i))
                flooded += 1

        if mMap[i][0] < mSeaLevel:
            if not visited[i][0]:
                visited[i][0] = True
                q.append((i, 0))
                flooded += 1

        if mMap[i][N - 1] < mSeaLevel:
            if not visited[i][N - 1]:
                visited[i][N - 1] = True
                q.append((i, N - 1))
                flooded += 1

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            if visited[nr][nc]:
                continue

            if mMap[nr][nc] >= mSeaLevel:
                continue

            q.append((nr, nc))
            visited[nr][nc] = True
            flooded += 1

    return flooded