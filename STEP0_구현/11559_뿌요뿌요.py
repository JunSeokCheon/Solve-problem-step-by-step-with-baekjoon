import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

field = [list(map(str, sys.stdin.readline().strip())) for _ in range(12)]
chain = 0

def bfs():
    global chain
    boom = False
    visited = [[False]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if field[i][j] != "." and not visited[i][j]:
                que = deque()
                que.append((i,j))

                color = field[i][j]
                group = [(i,j)]
                visited[i][j] = True

                while que:
                    x, y = que.popleft()

                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >= 12 or ny < 0 or ny >= 6:
                            continue

                        if not visited[nx][ny] and color == field[nx][ny]:
                            que.append((nx, ny))
                            group.append((nx,ny))
                            visited[nx][ny] = True
                
                if len(group) >= 4:
                    boom = True
                    while group:
                        x, y = group.pop()
                        field[x][y] = '.'
    
    if boom == True:
        chain += 1
        puyo()
        bfs()

def puyo():
    for i in range(10,-1,-1):
        for j in range(5,-1,-1):
            if field[i][j] != '.' and field[i+1][j] == '.':
                que = deque()
                que.append((i,j))
                while que:
                    x, y = que.popleft()

                    if x + 1 < 12 and field[x+1][y] == '.':
                        field[x+1][y] = field[x][y]
                        field[x][y] = '.'
                        que.append((x+1,y))

bfs()
print(chain)