import sys
from collections import deque

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

n, m = map(int, sys.stdin.readline().split())
space = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result = 0

que = deque()
for i in range(n):
    for j in range(m):
        if space[i][j] == 1:
            que.append((i,j))

while que:
    x, y = que.popleft()

    for k in range(8):
        nx = dx[k] + x
        ny = dy[k] + y

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if space[nx][ny] == 0:
            que.append((nx,ny))
            space[nx][ny] = space[x][y] + 1

for i in range(n):
    for j in range(m):
        result = max(result, space[i][j])

print(result-1)