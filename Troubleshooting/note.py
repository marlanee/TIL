n = 5
k = 2

prev = [-1, 0, 1, 2, 3]
next = [1, 2, 3, 4, -1]
deleted = []

# 여기에 2번 노드를 삭제하는 코드를 작성
left = prev[k]
right = next[k]
deleted.append(k)