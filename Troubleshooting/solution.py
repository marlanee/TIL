import heapq

heap = [
    (2, 101, 1),
    (5, 101, 2),
    (2, 101, 3)
]

heapq.heapify(heap)

# ID -> (현재 점수, 최신 버전)
latest = {
    101: (2, 3)
}

def get_min_valid():
    # 직접 구현
    while heap:
        score, ID, version = heapq.heappop(heap)

        if latest.get(ID) != (score, version):
            continue

        return (score, ID)

    return None