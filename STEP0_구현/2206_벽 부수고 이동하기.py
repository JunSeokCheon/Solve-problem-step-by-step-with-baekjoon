import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

wall = [[[0] * 2 for _ in range(m)] for _ in range(n)]

que = deque()
que.append((0,0,1))
wall[0][0][1] = 1

while que:
    x, y, chance = que.popleft()

    if x == n-1 and y == m-1:
        print(wall[x][y][chance])
        exit()
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if board[nx][ny] == 1 and chance == 1:
            wall[nx][ny][0] = wall[x][y][chance] + 1
            que.append((nx, ny, 0))
        elif wall[nx][ny][chance] == 0 and board[nx][ny] == 0:
            wall[nx][ny][chance] = wall[x][y][chance] + 1
            que.append((nx,ny,chance))

print(-1)