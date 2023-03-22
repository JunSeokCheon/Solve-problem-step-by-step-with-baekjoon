import sys
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

m, n, h = map(int, sys.stdin.readline().split())
box = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

que = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 1:
                que.append((k, i, j, 0))

while que:
    he, x, y, day = que.popleft()

    for i in range(6):
        dhe = he + dz[i]
        ndx = x + dx[i]
        ndy = y + dy[i]
        dday = day + 1

        if dhe < 0 or dhe >= h or ndx < 0 or ndx >= n or ndy < 0 or ndy >= m:
            continue

        if box[dhe][ndx][ndy] == 0:
            que.append((dhe, ndx, ndy, dday))
            box[dhe][ndx][ndy] = 1

for k in range(h):
    for i in range(n):
        for j in range(m):
            if box[k][i][j] == 0:
                print(-1)
                exit(0)

print(dday-1)


