
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

directions = [1, 0, -1, -2]

d = 0

for i in range(4):
    nd = (d + directions[i]) % 4
    print(nd)