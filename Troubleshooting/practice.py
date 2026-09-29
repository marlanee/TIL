# 부분집합

def dfs(start, total):
    if total == 10:
        if current not in result:
            result.append(current[:])
        return

    if total > 10:
        return

    for i in range(start, 11):
        current.append(i)
        dfs(i + 1, total + i)
        current.pop()

arr = list(range(1, 11))

result = []
current = []

dfs(1, 0)

for x in result:
    print(*x)

